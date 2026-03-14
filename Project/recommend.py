import random

#Calculates a recommendation score for owned games
def calculate_owned_game_score(game):

    #Rating has the strongest influence
    score = game.rating * 2

    #Bonus depending on priority
    if game.priority == "High":
        score += 10
    elif game.priority == "Medium":
        score += 5

    #Reduce score based on completion percentage, favouring games that are lower in completion
    score -= game.completion_percentage
    return score

#recommendation for wishlist games
def calculate_wishlist_score(game):
    
    #Wishlist recommendation focuses on rating and priority only
    score = game.rating * 2

    if game.priority == "High":
        score +=10
    elif game.priority == "Medium":
        score += 5
    return score

#Finds games owned games that are not completed
def get_owned_recommendable_games(games):
    recommendable_games = []

    for game in games:
        if game.ownership == "Owned" and game.status != "Completed":
            recommendable_games.append(game)
    return recommendable_games

#Returns wishlist games only
def get_wishlist_games(games):
    wishlist_games = []

    for game in games:
        if game.ownership == "Wishlist":
            wishlist_games.append(game)

    return wishlist_games

#Shows the top 3 owned recommendations based on score
def recommend_top_three_owned(games):
    print("\n---Top 3 Owned Recommendations---")

    recommendable_games = get_owned_recommendable_games(games)

    #Guard against no valid games
    if len(recommendable_games) == 0:
        print("There are no owned or unfinished games available to recommend")
        return
    
    #Sort games by score in descending order
    sorted_games = sorted(
        recommendable_games,
        key=calculate_owned_game_score,
        reverse=True
    )

    #Display the top 3
    top_games = sorted_games[:3]

    print()

    for index, game in enumerate(top_games, start=1):
        print(f"{index}.")
        print(game.summary())
        print(f"Score: {calculate_owned_game_score(game)}")
        print("--")

#Top 3 wishlish recommendations based on rating and priority
def recommend_top_three_wishlist(games):
    print("\n--- Top 3 Wishlist Recommendations ---")

    wishlist_games = get_wishlist_games(games)

    #Guard against no results
    if len(wishlist_games) == 0:
        print("There are no wishlist games to recommend")
        return
    
    #Sorting wishlist in descending order
    sorted_wishlist = sorted(
        wishlist_games,
        key=calculate_wishlist_score,
        reverse=True
    
    )

    #Show top 3
    top_wishlist = sorted_wishlist[:3]

    print()

    for index, game in enumerate(top_wishlist, start =1):
        print(f"{index}.")
        print(game.summary())
        print(f"Wishlist Score: {calculate_wishlist_score(game)}")
        print("--")

#Choose a random owned unfinished game
def recommend_random_owned_game(games):
    print("\n--- Random Owned Recommendation ---")

    recommendable_games = get_owned_recommendable_games(games)

    #Guard against no games shown
    if len(recommendable_games) == 0:
        print("There are no owned unfinished games available for recommendation")
        return
    
    random_game = random.choice(recommendable_games)

    print("\nRandomly selected game:")
    print()
    print(random_game.details())

def recommend_menu(games):
    while True:
        print("\n--- Recommendation Menu ---")
        print("1. Show top 3 owned recommendations")
        print("2. Show top 3 wishlist recommendations")
        print("3. Choose a random owned game")
        print("4. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            recommend_top_three_owned(games)

        elif choice == "2":
            recommend_top_three_wishlist(games)

        elif choice == "3":
            recommend_random_owned_game(games)

        elif choice == "4":
            break

        else:
            print(f'"{choice}" is not valid. Please choose 1-4')
