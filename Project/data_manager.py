#game backlog tracker, which allows me to double dip, using it as my project but also for my personal uses
#responsible for loading the data from my csv and converts the rows to an object the game file can use
import csv
from game import Game

def load_games(filename):
    games = []

    with open(filename, newline="", encoding ="utf-8") as file:
        reader = csv.DictReader(file)

        #convert CSV values into correct python data types
        for row in reader:
            game = Game(
                row ["title"],
                row["genre"],
                row["store"],
                row["ownership"],
                row["status"],
                int(row["rating"]),
                float(row["hours_played"]),
                int(row["completion_percentage"]),
                row["priority"],
                row["date_added"],
                row["notes"]
            )
            
            games.append(game)
            #Add's a game to the list
        return games
        #returns all the games when the function is called

#function to save the file as csv, allowing editing from the terminal itself
def save_games(filename, games):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer =csv.writer(file)

        #write header row
        writer.writerow([
            "title",
            "genre",
            "store",
            "ownership",
            "status",
            "rating",
            "hours_played",
            "completion_percentage",
            "priority",
            "date_added",
            "notes"
        ])

        for game in games:
            writer.writerow([
                game.title,
                game.genre,
                game.store,
                game.ownership,
                game.status,
                game.rating,
                game.hours_played,
                game.completion_percentage,
                game.priority,
                game.date_added,
                game.notes
            ])