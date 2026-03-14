#Main file where all functions and classes are called
from edit import manage_menu
from data_manager import load_games, save_games
from display import view_menu
from search import search_menu
from stats import display_statistics



def main():
    #loads all the games from the CSV
    games = load_games("games.csv")

    #Main program loop keeps running until user exits
    while True:
        print("\n---Game Backlog Tracker---\n")
        print("1. View games menu")
        print("2. Search games menu")
        print("3. Manage games menu")
        print("4. Show statistics")
        print("5. Exit")

        #user input for the choice
        choice = input("\nChoose an option: \n")

        #run the choice based on chosen option
        if choice == "1":
            view_menu(games)

        elif choice == "2":
            search_menu(games)

        elif choice == "3":
            manage_menu(games)

        elif choice == "4":
            display_statistics(games)

        elif choice == "5":
            print("Goodbye.")
            break

        #Invalid output handler with included choice
        else:
            print( f'Option "{choice}" is not valid, please choose a number between 1-5')


if __name__ == "__main__":
    #just in case I import main for some reason, this will stop automatic execution
    main()