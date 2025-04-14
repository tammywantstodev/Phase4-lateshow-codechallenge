#!/usr/bin/env python3

from app import app
from models import db, Episode, Guest, Appearance
from datetime import datetime

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Episode.query.delete()
    Guest.query.delete()
    Appearance.query.delete()

    print("Creating episodes...")

    episode1 = Episode(date=datetime.strptime("1/11/99", "%m/%d/%y").date(), number=1)
    episode2 = Episode(date=datetime.strptime("1/12/99", "%m/%d/%y").date(), number=2)
    episode3 = Episode(date=datetime.strptime("1/13/99", "%m/%d/%y").date(), number=3)
    episode4 = Episode(date=datetime.strptime("1/14/99", "%m/%d/%y").date(), number=4)
    episode5 = Episode(date=datetime.strptime("1/18/99", "%m/%d/%y").date(), number=5)
    episode6 = Episode(date=datetime.strptime("1/19/99", "%m/%d/%y").date(), number=6)
    episode7 = Episode(date=datetime.strptime("1/20/99", "%m/%d/%y").date(), number=7)
    episodes = [episode1, episode2, episode3, episode4, episode5, episode6, episode7]

    print("Creating guests...")

    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")
    guest4 = Guest(name="Gillian Anderson", occupation="film actress")
    guest5 = Guest(name="David Alan Grier", occupation="actor")
    guest6 = Guest(name="William Baldwin", occupation="actor")
    guest7 = Guest(name="Michael Stipe", occupation="Singer-lyricist")
    guests = [guest1, guest2, guest3, guest4, guest5, guest6, guest7]

    print("Creating appearances...")

    appearance1 = Appearance(episode=episode1, guest=guest1, rating=3)
    appearance2 = Appearance(episode=episode2, guest=guest2, rating=3)
    appearance3 = Appearance(episode=episode3, guest=guest3, rating=3)
    appearance4 = Appearance(episode=episode4, guest=guest4, rating=3)
    appearance5 = Appearance(episode=episode5, guest=guest5, rating=3)
    appearance6 = Appearance(episode=episode6, guest=guest6, rating=3)
    appearance7 = Appearance(episode=episode7, guest=guest7, rating=3)
    appearances = [appearance1, appearance2, appearance3, appearance4, appearance5, appearance6, appearance7]

    # Add all records to session
    db.session.add_all(episodes)
    db.session.add_all(guests)
    db.session.add_all(appearances)

    # Commit to the database
    db.session.commit()

    print("Seeding done!")
