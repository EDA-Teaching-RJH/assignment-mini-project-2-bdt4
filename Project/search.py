#Implementing search for my games list

import re

def regex_field_search(games, field_name, query):

    found = False

    try:

        for game in games:
            value = str(getattr(game, field_name))

            if re.search(query, value, re.IGNORECASE):
                print(game.summary())
                found = True
            
        if not found:
            print(f'No games matching "{query}" were found.')

    except re.error:
        print(f'"{query}" is not a valid search term')

#create menu for search after the main menu
def search_menu(games):
    
    while True:
        print("\n ---Search Menu---")
        print("1. Search by title")
        print("2. Search by genre")
        print("3. Search by status")
        print("4. Search by notes")
        print("5. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            search_by_title(games)

        elif choice == "2":
            search_by_genre(games)

        elif choice == "3":
            search_by_status(games)

        elif choice == "4":
            search_by_notes(games)

        elif choice == "5":
            break
        
        else:
            print(f'"{choice}" is not valid. Please choose 1-5.')


#function to search by title
def search_by_title(games):

    #Ask user for a title to search
    query = input("Enter game title to search by: ")

    print(f'\nSearch results for "{query}"')
    print("--------------")

    regex_field_search(games, "title", query)

def search_by_genre(games):

    query = input("Enter genre to search by: ")

    print(f"\nGenre results for '{query}'")
    print("--------------------------")

    regex_field_search(games, "genre", query)

def search_by_status(games):

    query = input("Enter status to search by: ")

    print(f"\nStatus results for '{query}'")
    print("----------------------------")

    regex_field_search(games, "status", query)

def search_by_notes(games):

    query = input("Enter note text to search for: ")

    print(f"\nNotes results for '{query}'")
    print ("--------------------")

    regex_field_search(games, "notes", query)
