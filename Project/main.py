#Game Backlog Tracker

from backlog import GameBacklog
from storage import CSVStorage
from app import BacklogApp


def main():
    filename = "games.csv"

    #Load saved games from the CSV file
    storage = CSVStorage()
    games = storage.load_games(filename)

    #Create the backlog and load it with games
    backlog = GameBacklog()
    for game in games:
        backlog.add_game(game)

    #Start the app
    app = BacklogApp(backlog, storage, filename)
    app.run()


if __name__ == "__main__":
    main()