from models import db, Episode, Guest, Appearance
from flask import current_app
from config import app  # Make sure you're importing your Flask app
import csv


def seed_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        episode_number = 1

        for row in reader:
            # Create or find the guest
            guest_name = row["Raw_Guest_List"]
            guest_occupation = row["GoogleKnowlege_Occupation"]

            guest = Guest.query.filter_by(name=guest_name).first()
            if not guest:
                guest = Guest(name=guest_name, occupation=guest_occupation)
                db.session.add(guest)

            # Create the episode
            episode_date = row["Show"]
            episode = Episode(date=episode_date, number=episode_number)
            db.session.add(episode)
            episode_number += 1

            # Create the appearance
            appearance = Appearance(rating=5, episode=episode, guest=guest)
            db.session.add(appearance)

        db.session.commit()


# Running inside the application context
if __name__ == "__main__":
    with app.app_context():
        seed_data("seed.csv")
