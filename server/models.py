from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    # add relationship
    appearances=db.relationship('Appearance', back_populates='episode')

    # add serialization rules
    serialize_rules=('-appearances.episode',)
    def __repr__(self):
        return f"<Episode{self.number}, {self.date}>"


class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    # add relationship
    appearances=db.relationship('Appearance', back_populates='guest')
    # add serialization rules
    serialize_rules=('-appearances.guest',)
    def __repr__(self):
        return f"<Guest: {self.name}, {self.occupation}>"


class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    # add relationships
    episode_id=db.Column(db.Integer, db.ForeignKey('episodes.id'))
    guest_id=db.Column(db.Integer, db.ForeignKey('guests.id'))

    guest=db.relationship('Guest', back_populates='appearances')
    episode=db.relationship('Episode', back_populates='appearances')
    # add serialization rules
    serialize_rules=('-episode.appearances','guest.appearances',)
    # add validation
    #@validates('rating')
    #def validate_rating(self):
         ##if not (1 <= self.rating <= 5):
           # raise ValueError("must have a `rating` between 1 and 5 ")
         #return self.rating

    def __repr__(self):
        return f"<Appearance: ${self.guest}, ${self.episode}>"