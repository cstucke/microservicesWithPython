import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app.database import SessionLocal, engine
from app.models import Base, Game

GAMES = [
    {"title": "The Witcher 3: Wild Hunt", "genre": "RPG",          "platform": "PC",     "release_year": 2015, "cover_url": None},
    {"title": "Hollow Knight",            "genre": "Metroidvania", "platform": "PC",     "release_year": 2017, "cover_url": None},
    {"title": "Celeste",                  "genre": "Platformer",   "platform": "Switch", "release_year": 2018, "cover_url": None},
    {"title": "Elden Ring",               "genre": "Soulslike",    "platform": "PS5",    "release_year": 2022, "cover_url": None},
    {"title": "Stardew Valley",           "genre": "Simulation",   "platform": "PC",     "release_year": 2016, "cover_url": None},
]

def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    imported = 0
    for data in GAMES:
        existing = db.query(Game).filter(Game.title == data["title"]).first()
        if existing:
            continue
        game = Game(
            title=data["title"],
            genre=data["genre"],
            platform=data["platform"],
            release_year=data["release_year"],
            cover_url=data["cover_url"],
        )
        db.add(game)
        imported += 1

    db.commit()
    db.close()
    print(f"Imported {imported} games.")

if __name__ == "__main__":
    run()
