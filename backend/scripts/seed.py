from app.db.session import SessionLocal
from app.features.ideas.schemas import IdeaIn
from app.features.ideas.service import service
from app.features.cluster.service import rebuild_clusters
from app.models import Idea

# 5 clearly different themes x 5 ideas each = 25 ideas
SEED = [
    # --- Mental health & wellness ---
    ("Sleep Buddy", "Tracks sleep patterns and suggests small nightly habits to help students rest better.", "Maya Chen"),
    ("Calm Corner", "Guided breathing and meditation sessions designed for stressed students during exam week.", "Jordan Lee"),
    ("Mood Journal", "Daily check-ins that chart your mood over time and spot patterns with sleep and exercise.", "Priya Patel"),
    ("Study Break Coach", "Reminds you to take short walks and stretch breaks while studying, based on your schedule.", "Sam Rivera"),
    ("Peer Support Match", "Anonymously connects students going through similar struggles for supportive chats.", "Ava Johnson"),

    # --- Climate & sustainability ---
    ("Campus Compost Map", "A map of compost bins on campus with a tracker of how much food waste is diverted.", "Liam Brooks"),
    ("Dorm Energy Tracker", "Shows each dorm's electricity use in real time and runs friendly saving competitions.", "Nora Kim"),
    ("Bike Share Planner", "Helps students find the best bike routes and free bike racks around town.", "Ethan Wright"),
    ("Thrift Swap", "A campus marketplace for swapping clothes and furniture to cut down on waste.", "Zoe Martin"),
    ("Carbon Footprint Quiz", "A quick quiz that estimates your carbon footprint and suggests three easy changes.", "Omar Hassan"),

    # --- Education & learning ---
    ("Flashcard Duel", "Turn lecture notes into flashcards and quiz friends head to head in real time.", "Chloe Davis"),
    ("Tutor Finder", "Matches students with peer tutors by course, availability, and learning style.", "Noah Garcia"),
    ("Lecture Summarizer", "Records a lecture and produces a short summary with key terms and likely exam questions.", "Isla Nguyen"),
    ("Study Group Scheduler", "Finds a time that works for everyone in a study group and books a room automatically.", "Lucas Scott"),
    ("Code Kids", "Teaches middle schoolers programming basics through small game-building lessons.", "Emma Thompson"),

    # --- Personal finance & careers ---
    ("Student Budget Buddy", "Tracks spending by category and warns you before you run out of money for the month.", "Mason Clark"),
    ("Split It Fair", "Splits rent, groceries, and utilities between roommates and reminds people to pay.", "Harper Young"),
    ("Internship Tracker", "Keeps all your internship applications, deadlines, and interview stages in one board.", "Elijah Adams"),
    ("Resume Reviewer", "Gives specific feedback on student resumes based on the job description you paste in.", "Sofia Torres"),
    ("Scholarship Finder", "Lists scholarships you actually qualify for and tracks their deadlines.", "Benjamin Hill"),

    # --- Creative tools & media ---
    ("Beat Maker Lite", "A simple browser tool for making drum loops and sharing them with friends.", "Mia Foster"),
    ("Story Sketch", "Turns short story outlines into storyboards with auto-generated scene sketches.", "Henry Baker"),
    ("Campus Zine", "A collaborative digital magazine where students submit art, poems, and photos.", "Layla Ahmed"),
    ("Pocket Podcast", "Record, trim, and publish a podcast episode entirely from your phone.", "Jack Morgan"),
    ("Color Palette Finder", "Upload a photo and get a matching color palette for posters and slides.", "Ruby Evans"),
]


def main():
    db = SessionLocal()
    try:
        existing = db.query(Idea).count()
        if existing > 0:
            print(f"DB already has {existing} ideas. Run `python -m scripts.migrate --reset` first.")
            return

        svc = service()
        for i, (title, description, author) in enumerate(SEED, start=1):
            svc.create_idea(db, IdeaIn(
                title=title,
                description=description,
                author_name=author,
                contact=f"{author.lower().replace(' ', '.')}@school.edu",
                github_url=None,

            ))
            print(f"[{i}/{len(SEED)}] {title}")

        print("Building map and clusters...")
        k = rebuild_clusters(db)
        print(f"Done: {k} clusters")
    finally:
        db.close()


if __name__ == "__main__":
    main()