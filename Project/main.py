#Main file where all functions and classes are called
from edit import add_game, delete_game, edit_game
from data_manager import load_games, save_games
from display import (
    display_games,
    display_completed_games,
    display_wishlist_games,
    display_backlog_games
)
from search import search_games_by_title

from stats import display_statistics



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
        print("6. Show statistics")
        print("7. Add a game")
        print("8. Edit a game")
        print("9. Delete a game")
        print("10. Exit")

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
            display_statistics(games)

        elif choice == "7":
            add_game(games)
            save_games("games.csv", games)
            print ("Changes saved.")

        elif choice == "8":
            edit_game(games)
            save_games("games.csv", games)
            print("Changes saved.")

        elif choice =="9":
            delete_game(games)
            save_games("games.csv", games)
            print("Changes saved.")

        elif choice == "10":
            print("Goodbye.")
            break

        #Invalid output handler with included choice
        else:
            print( f'Option "{choice}" is not valid, please choose a number between 1-9')


if __name__ == "__main__":
    #just in case I import main for some reason, this will stop automatic execution
    main()