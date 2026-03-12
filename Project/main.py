#Main file where all functions and classes are called
from data_manager import load_games

def main():
    #loads all the games from the CSV
    games = load_games("games.csv")

    print("Game Backlog Tracer\n")

    #simple function that dispolays each game in the terminal for testing
    for game in games:
        print(game)

if __name__ == "__main__":
    #just in case I import main for some reason, this will stop automatic execution
    main()