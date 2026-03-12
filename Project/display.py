#Displays every game in the list
def display_games(games):
    print("\n All Games")
    print("-----------")
    for game in games:
        print(game)

#Displays games that have been completed
def display_completed_games(games):
    print("\n Completed Games")
    print("-----------------")
    for game in games:
        if game.status == "Completed":
            print(game)

#Displays backlog games (owned but not started)
def display_backlog_games(games):
    print("\n Backlog Games")
    print("---------------")
    for game in games:
        if game.ownership != "Wishlist" and game.status == "Not Started":
            print(game)
            
#Displays games on the wishlist
def display_wishlist_games(games):
    print("\n Wishlist Games")
    print("----------------")
    for game in games:
        if game.ownership == "Wishlist":
            print(game)