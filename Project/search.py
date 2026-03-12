#Implementing search for my games list

import re

def search_games_by_title(games):

    #Ask user for a title to search
    gamequery = input("Enter game title to search by: ")

    print(f'\nSearch results for "{gamequery}"')
    print("--------------")

    found = False

    try:

        #loop through all of the games to check for a match, while guarding against errors
        for game in games:
            if re.search(gamequery, game.title, re.IGNORECASE):
                print(game)
                found = True
        if not found:
            print(f'No games matching "{gamequery}" were found.')

    except re.error:
        print(f'"{gamequery}" is not a valid search term')