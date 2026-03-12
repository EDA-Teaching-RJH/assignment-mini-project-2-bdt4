#Main file where all functions and classes are called
from data_manager import load_games
from display import (
    display_games,
    display_completed_games,
    display_wishlist_games,
    display_backlog_games
)
from search import search_games_by_title

def main():
    #loads all the games from the CSV
    games = load_games("games.csv")

    #Main program loop keeps running until user exits
    while True:
        print("\n---Game Backlog Tracker---\n")
        print("1. View all games")
        print("2. View completed games")
        print("3. View wishlist") 
        print("4. View backlog")
        print("5. Search games by title")
        print("6. Exit")

        #user input for the choice
        choice = input("\nChoose an option: \n")

        #run the choice based on chosen option
        if choice == "1":
            display_games(games)

        elif choice == "2":
            display_completed_games(games)
        
        elif choice == "3":
            display_backlog_games(games)

        elif choice == "4":
            display_wishlist_games(games)   

        elif choice == "5":
            search_games_by_title(games)    

        elif choice == "6":
            print("Goodbye.")
            break

        #Invalid output handler with included choice
        else:
            print( f'Option "{choice}" is not valid, please choose a number between 1-5')


if __name__ == "__main__":
    #just in case I import main for some reason, this will stop automatic execution
    main()