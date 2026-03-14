# View menu for different game list filters
def view_menu(games):

    while True:
        print("\n--- View Menu ---")
        print("1. View all games")
        print("2. View completed games")
        print("3. View in progress games")
        print("4. View wishlist")
        print("5. View backlog")
        print("6. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_games(games)

        elif choice == "2":
            display_completed_games(games)

        elif choice == "3":
            display_in_progress_games(games)

        elif choice == "4":
            display_wishlist_games(games)

        elif choice == "5":
            display_backlog_games(games)

        elif choice == "6":
            break

        else:
            print(f'"{choice}" is not valid. Please choose 1-6.')

#Displays every game in the list
def display_games(games):
    print("\n All Games")
    print("-----------")

    found = False

    for game in games:
        print(game.summary())
        print("-")
        found = True

    if not found:
        print("There are currently no games in the backlog manager")

#Displays games that have been completed
def display_completed_games(games):
    print("\n Completed Games")
    print("-----------------")

    found = False

    for game in games:
        if game.status == "Completed":
            print(game.details())
            print("--")
            found = True

    if not found:
        print("There are currently no completed games")
    

#Displays backlog games (owned but not started)
def display_backlog_games(games):
    print("\n Backlog Games")
    print("---------------")

    found = False

    for game in games:
        if game.ownership != "Wishlist" and game.status == "Not Started":
            print(game.details())
            print("--")
            found = True

    if not found:
        print("There are currently no backlog games")
            
#Displays games on the wishlist
def display_wishlist_games(games):
    
    print("\n Wishlist Games")
    print("----------------")

    found = False

    for game in games:
        if game.ownership == "Wishlist":
            print(game.details())
            print("--")
            found = True

    if not found:
        print("There are currently no wishlist games")

#Displays games that are in progress
def display_in_progress_games(games):

    print("\n In Progress Games")
    print("------------------")

    found = False

    for game in games:
        if game.status == "In Progress":
            print(game.details())
            print("--")
            found = True

    if not found:
        print("There are currently no games in progress.")