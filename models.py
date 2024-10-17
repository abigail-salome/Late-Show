from flask_sqlalchemy import SQLAlchemy
from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship(
        "Appearance", backref="episode", cascade="all, delete-orphan"
    )


class Guest(db.Model):
    __tablename__ = "guests"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    appearances = db.relationship(
        "Appearance", backref="guest", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
        }


class Appearance(db.Model):
    __tablename__ = "appearances"
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "episode_id": self.episode_id,
            "guest_id": self.guest_id,
            "episode": self.episode.to_dict(),
            "guest": self.guest.to_dict(),
        }

    @validates("ratings")
    def validate_rating(self, key, rating):
        if rating > 5 and rating < 1:
            raise ValueError({"error ": "rating can only be between 1 and  5"})
