from data_manager import load_games

def main():
    games = load_games("games.csv")

    print("Game Backlog Tracer\n")

    for game in games:
        print(game)

if __name__ == "__main__":
    main()