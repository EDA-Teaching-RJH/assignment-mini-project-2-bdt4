#Allows me to display stats about the game backlog

#setting the base stats to be updated from the csv later
def display_statistics(games):
    total_games = len(games)
    completed_games = 0
    in_progress_games = 0
    wishlist_games = 0
    backlog_games = 0
    total_hours = 0
    ratings = []
    completion_values = []

    for game in games:
        total_hours += float(game.hours_played)

        if game.rating > 0:
            ratings.append(int(game.rating))

        completion_values.append(game.completion_percentage)

        if game.status == "Completed":
            completed_games += 1

        if game.status == "In Progress":
            in_progress_games += 1

        if game.ownership == "Wishlist":
            wishlist_games += 1

        if game.ownership != "Wishlist" and game.status == "Not Started":
            backlog_games += 1

    #calculate average rating
    if len(ratings) > 0:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = 0
    #calculate average completion %
    if len(completion_values) > 0:
        average_completion = sum(completion_values) / len(completion_values)
    else:
        average_completion = 0

    #printing stats
    print("\nGame Statistics")
    print("---------------")
    print(f"{'Total games':25} {total_games}")
    print(f"{'Completed games':25} {completed_games}")
    print(f"{'In progress games':26}{in_progress_games}")
    print(f"{'Backlog games':25} {backlog_games}")
    print(f"{'Wishlist games':25} {wishlist_games}")
    print(f"{'Total hours played':25} {total_hours:.1f}")
    print(f"{'Average rating':25} {average_rating:.1f}/10")
    print(f"{'Average completion:':26}{average_completion:.1f}%")