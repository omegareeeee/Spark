from app.db.session import SessionLocal
from app.models import Person

db = SessionLocal()

try:
    person = Person(
        name="Test User",
        handle="testuser",
    )

    db.add(person)
    db.commit()
    db.refresh(person)

    print(f"Person created! ID: {person.id}")

except Exception:
    db.rollback()
    raise

finally:
    db.close()