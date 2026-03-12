#game backlog tracker, which allows me to double dip, using it as my project but also for my personal uses

import csv
from game import Game

def load_games(filename):
    games = []

    with open(filename, newline="", encoding ="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            game = Game(
                row ["title"],
                row["genre"],
                row["store"],
                row["ownership"],
                row["status"],
                row["rating"],
                row["hours_played"],
                row["completion_percentage"],
                row["priority"],
                row["date_added"],
                row["notes"]
            )
            
            games.append(game)

        return games