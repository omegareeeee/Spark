"""
Seed the database with 25 realistic student project ideas (5 themes x 5 ideas),
then build the clusters and the UMAP map.

Run from backend/:
    python -m scripts.seed          # seeds only if the ideas table is empty
    python -m scripts.seed --force  # seeds anyway (adds on top of existing rows)

Order matters:
  1. create_idea() embeds each idea and saves it. No map exists yet, so x/y
     and cluster_id stay empty. That is expected.
  2. rebuild_clusters() runs KMeans + UMAP once over everything, names the
     groups with Claude, and fills in x, y, and cluster_id for every idea.
"""
import sys

from app.db.session import SessionLocal
from app.models import Idea
from app.features.ideas.schemas import IdeaIn
from app.features.ideas.service import create_idea
from app.features.clusters.service import rebuild_clusters

SEED_IDEAS = [
    # ---------- Health & wellness ----------
    {
        "title": "SleepSync",
        "description": "A mobile app that tracks sleep with phone sensors and suggests small evening habit changes, like dimming lights or stopping caffeine, based on your own sleep data.",
        "github_url": "https://github.com/sleepsync/sleepsync",
        "contact": "maya#2041 (Discord)",
        "author_name": "Maya Patel",
    },
    {
        "title": "MoodMap",
        "description": "A daily mood journal that spots patterns between your mood, sleep, and activity, and gently flags when you have had several rough days in a row.",
        "github_url": None,
        "contact": "jordan.k@university.edu",
        "author_name": "Jordan Kim",
    },
    {
        "title": "PillPal",
        "description": "A medication reminder app for elderly relatives that lets family members confirm doses were taken and sends an alert if a dose is missed.",
        "github_url": "https://github.com/pillpal/pillpal",
        "contact": "sam_r#8832 (Discord)",
        "author_name": "Sam Rivera",
    },
    {
        "title": "CampusCalm",
        "description": "A guided breathing and stress relief tool for students that adapts exercise length to how close the next exam or deadline is.",
        "github_url": None,
        "contact": "priya.n@university.edu",
        "author_name": "Priya Nair",
    },
    {
        "title": "FormCheck",
        "description": "Uses a phone camera to check your posture during squats and push-ups and gives real-time feedback to prevent gym injuries.",
        "github_url": "https://github.com/formcheck/formcheck",
        "contact": "tyler#5510 (Discord)",
        "author_name": "Tyler Brooks",
    },

    # ---------- Education & learning ----------
    {
        "title": "StudyBuddy Match",
        "description": "Pairs students in the same course for study sessions based on schedule overlap and which topics each person finds hardest.",
        "github_url": "https://github.com/studybuddy/match",
        "contact": "elena#3376 (Discord)",
        "author_name": "Elena Garcia",
    },
    {
        "title": "FlashForge",
        "description": "Turns lecture notes or slides into spaced-repetition flashcards automatically and schedules reviews right before you would forget.",
        "github_url": None,
        "contact": "omar.h@university.edu",
        "author_name": "Omar Hassan",
    },
    {
        "title": "CodeCraft Kids",
        "description": "A game where middle schoolers learn programming basics by guiding a robot through puzzle levels, with a dashboard for teachers to track progress.",
        "github_url": "https://github.com/codecraftkids/game",
        "contact": "lily#9104 (Discord)",
        "author_name": "Lily Chen",
    },
    {
        "title": "OfficeHours Queue",
        "description": "A live queue for TA office hours so students can see wait times from their dorm and get a notification when they are next.",
        "github_url": "https://github.com/ohqueue/ohqueue",
        "contact": "devon.w@university.edu",
        "author_name": "Devon Walker",
    },
    {
        "title": "LinguaLoop",
        "description": "Language practice through short voice conversations with native-speaking volunteers, matched by the language you want and the language you can teach.",
        "github_url": None,
        "contact": "sofia#6627 (Discord)",
        "author_name": "Sofia Rossi",
    },

    # ---------- Climate & sustainability ----------
    {
        "title": "CarbonCart",
        "description": "A browser extension that shows the estimated carbon footprint of items in your online shopping cart and suggests lower-impact alternatives.",
        "github_url": "https://github.com/carboncart/extension",
        "contact": "noah#1187 (Discord)",
        "author_name": "Noah Fischer",
    },
    {
        "title": "FoodShare Fridge",
        "description": "A map of community fridges and pantries where people can post surplus food from events and dining halls before it gets thrown away.",
        "github_url": None,
        "contact": "aisha.b@university.edu",
        "author_name": "Aisha Bello",
    },
    {
        "title": "SolarScout",
        "description": "Estimates how much a rooftop could save with solar panels from a satellite image and local electricity prices, for renters and homeowners.",
        "github_url": "https://github.com/solarscout/estimator",
        "contact": "liam#7743 (Discord)",
        "author_name": "Liam O'Brien",
    },
    {
        "title": "TrashTracker",
        "description": "Lets people photograph waste and get instant guidance on whether it is recyclable, compostable, or trash under their city's local rules.",
        "github_url": "https://github.com/trashtracker/app",
        "contact": "hana.t@university.edu",
        "author_name": "Hana Tanaka",
    },
    {
        "title": "BikeBuddy Routes",
        "description": "Plans safer bike commutes by combining crowdsourced reports of dangerous intersections, bike lanes, and road hazards into one route planner.",
        "github_url": None,
        "contact": "marcus#4459 (Discord)",
        "author_name": "Marcus Johnson",
    },

    # ---------- Personal finance ----------
    {
        "title": "BudgetBuddy",
        "description": "A budgeting app for students that reads bank transactions, sorts spending into categories, and warns you before you overspend on food or subscriptions.",
        "github_url": "https://github.com/budgetbuddy/app",
        "contact": "ethan#2298 (Discord)",
        "author_name": "Ethan Park",
    },
    {
        "title": "SplitEasy",
        "description": "Splits shared apartment bills, groceries, and trips between roommates and tracks who owes whom, with reminders to settle up.",
        "github_url": None,
        "contact": "zoe.m@university.edu",
        "author_name": "Zoe Martin",
    },
    {
        "title": "LoanLens",
        "description": "Explains student loan terms in plain language and simulates how different repayment plans change what you pay over ten years.",
        "github_url": "https://github.com/loanlens/simulator",
        "contact": "isaac#8071 (Discord)",
        "author_name": "Isaac Thompson",
    },
    {
        "title": "FirstPaycheck",
        "description": "An interactive guide for first-time workers that breaks down taxes, withholding, and retirement contributions using their actual offer letter numbers.",
        "github_url": None,
        "contact": "nina.s@university.edu",
        "author_name": "Nina Sharma",
    },
    {
        "title": "SubTrim",
        "description": "Finds forgotten recurring subscriptions in your bank statements and helps you cancel them with one tap.",
        "github_url": "https://github.com/subtrim/subtrim",
        "contact": "carlos#3915 (Discord)",
        "author_name": "Carlos Mendez",
    },

    # ---------- Creative tools ----------
    {
        "title": "BeatBoard",
        "description": "A browser-based music maker where you build beats by dragging colorful blocks, designed for people with no music theory background.",
        "github_url": "https://github.com/beatboard/web",
        "contact": "jade#6482 (Discord)",
        "author_name": "Jade Williams",
    },
    {
        "title": "StoryForge",
        "description": "A collaborative writing tool where a group builds a story together, with each person controlling one character and a shared timeline of events.",
        "github_url": None,
        "contact": "felix.r@university.edu",
        "author_name": "Felix Romero",
    },
    {
        "title": "PaletteMate",
        "description": "Generates matching color palettes from any photo you upload and exports them as design tokens for websites and apps.",
        "github_url": "https://github.com/palettemate/palettemate",
        "contact": "amara#1633 (Discord)",
        "author_name": "Amara Okafor",
    },
    {
        "title": "SketchToApp",
        "description": "Lets designers draw a rough interface sketch on paper, take a photo, and get a clickable prototype they can share for feedback.",
        "github_url": "https://github.com/sketchtoapp/prototype",
        "contact": "kai#9250 (Discord)",
        "author_name": "Kai Nakamura",
    },
    {
        "title": "PixelPals",
        "description": "A pixel art editor with shared canvases, where friends can paint on the same sprite at once and animate it frame by frame.",
        "github_url": None,
        "contact": "riley.c@university.edu",
        "author_name": "Riley Cooper",
    },
]


def main() -> None:
    force = "--force" in sys.argv

    with SessionLocal() as db:
        existing = db.query(Idea).count()
        if existing and not force:
            print(f"Database already has {existing} ideas. Use --force to add anyway.")
            return

        # Step 1: embed + save every idea (no map yet, so x/y/cluster stay empty)
        for i, item in enumerate(SEED_IDEAS, start=1):
            create_idea(db, IdeaIn(**item))
            print(f"[{i}/{len(SEED_IDEAS)}] saved: {item['title']}")

        # Step 2: group everything, name the groups, and lay out the map once
        print("\nBuilding clusters and map...")
        k = rebuild_clusters(db)
        print(f"Done. Created {k} clusters.")


if __name__ == "__main__":
    main()