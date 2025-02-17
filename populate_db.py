import os
import django
from faker import Faker
import random
from events.models import Category, Participant, Event  # Replace 'your_app' with your actual app name

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')  # Replace 'your_project' with your actual project name
django.setup()

# Function to populate the database
def populate_db():
    # Initialize Faker
    fake = Faker()

    # Create Categories
    categories = [Category.objects.create(
        name=fake.word().capitalize(),
        description=fake.text()
    ) for _ in range(6)]
    print(f"Created {len(categories)} categories.")

    # Create Participants
    participants = [Participant.objects.create(
        name=fake.name(),
        email=fake.unique.email()
    ) for _ in range(10)]
    print(f"Created {len(participants)} participants.")

    # Create Events
    events = []
    for _ in range(15):
        event = Event.objects.create(
            name=fake.sentence(nb_words=3).replace('.', ''),
            description=fake.paragraph(),
            date=fake.date_between(start_date="-30d", end_date="+30d"),
            time=fake.time(),
            location=fake.city(),
            category=random.choice(categories)
        )
        event.participant.set(random.sample(participants, k=random.randint(1, len(participants))))
        events.append(event)
    print(f"Created {len(events)} events.")

    print("Database populated successfully!")

# Run the function
populate_db()
