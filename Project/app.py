# main app for the tracker

import re
from datetime import datetime

from game import Game
from stats import StatisticsManager
from recommend import (
    TopThreeBacklogRecommender,
    TopThreeWishlistRecommender,
    RandomBacklogRecommender,
)


class BacklogApp:
    # initialises the app with the backlog, storage handler and CSV
    def __init__(self, backlog, storage, filename):
        self.backlog = backlog
        self.storage = storage
        self.filename = filename

    # Runs the main app
    def run(self):
        while True:
            #main menu
            print("\n--- Game Backlog Tracker ---")
            print("1. View games")
            print("2. Search games")
            print("3. Manage games")
            print("4. Show statistics")
            print("5. Recommendations")
            print("6. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.view_menu()
            elif choice == "2":
                self.search_menu()
            elif choice == "3":
                self.manage_menu()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                self.recommend_menu()
            elif choice == "6":
                print("Goodbye.")
                break
            else:
                print(f'"{choice}" is not valid. Please choose 1-6.')

    #view submenu
    def view_menu(self):
        while True:
            print("\n--- View Menu ---")
            print("1. View all games")
            print("2. View completed games")
            print("3. View in progress games")
            print("4. View wishlist games")
            print("5. Return to main menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.display_games(self.backlog.get_all_games(), "All Games")
            elif choice == "2":
                self.display_games(self.backlog.completed_games(), "Completed Games")
            elif choice == "3":
                self.display_games(self.backlog.in_progress_games(), "In Progress Games")
            elif choice == "4":
                self.display_games(self.backlog.wishlist_games(), "Wishlist Games")
            elif choice == "5":
                break
            else:
                print(f'"{choice}" is not valid. Please choose 1-5.')

    #search submenu
    def search_menu(self):
        while True:
            print("\n--- Search Menu ---")
            print("1. Search by title")
            print("2. Search by genre")
            print("3. Search by status")
            print("4. Return to main menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.search_by_field("title", "title")
            elif choice == "2":
                self.search_by_field("genre", "genre")
            elif choice == "3":
                self.search_by_field("status", "status")
            elif choice == "4":
                break
            else:
                print(f'"{choice}" is not valid. Please choose 1-4.')

    #manage submenu
    def manage_menu(self):
        while True:
            print("\n--- Manage Menu ---")
            print("1. Add a game")
            print("2. Edit a game")
            print("3. Delete a game")
            print("4. Return to main menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_game()
            elif choice == "2":
                self.edit_game()
            elif choice == "3":
                self.delete_game()
            elif choice == "4":
                break
            else:
                print(f'"{choice}" is not valid. Please choose 1-4.')

    #recommendation submenu
    def recommend_menu(self):
        while True:
            print("\n--- Recommendation Menu ---")
            print("1. Top 3 backlog recommendations")
            print("2. Top 3 wishlist recommendations")
            print("3. Random backlog game")
            print("4. Return to main menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.show_top_backlog_recommendations()
            elif choice == "2":
                self.show_top_wishlist_recommendations()
            elif choice == "3":
                self.show_random_backlog_recommendation()
            elif choice == "4":
                break
            else:
                print(f'"{choice}" is not valid. Please choose 1-4.')

    #view feature
    

    #displays a list of games depending on the option chosen
    def display_games(self, games, heading):
        print(f"\n--- {heading} ---\n")

        if not games:
            print("No games found.")
            return

        for i, game in enumerate(games, start=1):
            print(f"{i}. {game.summary()}")
            print ("-" * 10)

    #search feature

    #searches for a game with chosen parameters
    def search_by_field(self, field_name, label):
        query = input(f"Enter {label} to search by: ")

        print(f'\nSearch results for "{query}"')
        print("--------------")

        try:
            results = self.backlog.search_by_field_regex(field_name, query, re)
            self.display_games(results, f"{label.title()} Search Results")
        except re.error:
            print(f'"{query}" is not a valid search term.')

    #manage feature

    #Adds a new game and saves it to CSV
    def add_game(self):
        print("\n--- Add a New Game ---")

        title = self.get_non_empty_input("Enter title: ")
        genre = self.get_non_empty_input("Enter genre: ")
        store = self.get_non_empty_input("Enter store: ")
        ownership = self.get_valid_choice(
            "Enter ownership (Owned, Wishlist): ",
            ["Owned", "Wishlist"]
        )
        status = self.get_valid_choice(
            "Enter status (Completed, In Progress, Not Started): ",
            ["Completed", "In Progress", "Not Started"]
        )
        rating = self.get_valid_int("Enter rating (0-10): ", 0, 10)
        hours_played = self.get_valid_float("Enter hours played: ", 0)
        completion_percentage = self.get_valid_int(
            "Enter completion percentage (0-100): ", 0, 100
        )
        priority = self.get_valid_choice(
            "Enter priority (Low, Medium, High): ",
            ["Low", "Medium", "High"]
        )
        notes = input("Enter notes (optional): ").strip()
        date_added = datetime.now().strftime("%d/%m/%Y")

        new_game = Game(
            title, genre, store, ownership, status,
            rating, hours_played, completion_percentage,
            priority, date_added, notes
        )

        self.backlog.add_game(new_game)
        self.storage.save_games(self.filename, self.backlog.get_all_games())

        print("\nGame added successfully:")
        print(new_game.details())

    #Edits a game and saves the changes
    def edit_game(self):
        if self.backlog.is_empty():
            print("There are no games to edit.")
            return

        game = self.select_game("Edit a Game")
        if game is None:
            return

        print(f'\nEditing "{game.title}"')
        print("1. Title")
        print("2. Genre")
        print("3. Store")
        print("4. Ownership")
        print("5. Status")
        print("6. Rating")
        print("7. Hours played")
        print("8. Completion percentage")
        print("9. Priority")
        print("10. Notes")

        field_choice = self.get_valid_int("Choose a field to edit (1-10): ", 1, 10)

        if field_choice == 1:
            game.title = self.get_non_empty_input("Enter new title: ")
        elif field_choice == 2:
            game.genre = self.get_non_empty_input("Enter new genre: ")
        elif field_choice == 3:
            game.store = self.get_non_empty_input("Enter new store: ")
        elif field_choice == 4:
            game.ownership = self.get_valid_choice(
                "Enter ownership (Owned, Wishlist): ",
                ["Owned", "Wishlist"]
            )
        elif field_choice == 5:
            game.status = self.get_valid_choice(
                "Enter status (Completed, In Progress, Not Started): ",
                ["Completed", "In Progress", "Not Started"]
            )
        elif field_choice == 6:
            game.rating = self.get_valid_int("Enter new rating (0-10): ", 0, 10)
        elif field_choice == 7:
            game.hours_played = self.get_valid_float("Enter new hours played: ", 0)
        elif field_choice == 8:
            game.completion_percentage = self.get_valid_int(
                "Enter new completion percentage (0-100): ", 0, 100
            )
        elif field_choice == 9:
            game.priority = self.get_valid_choice(
                "Enter priority (Low, Medium, High): ",
                ["Low", "Medium", "High"]
            )
        elif field_choice == 10:
            game.notes = input("Enter new notes: ").strip()

        self.storage.save_games(self.filename, self.backlog.get_all_games())

        print("\nGame updated successfully:")
        print(game.details())

    #Deletes a selected game after confirmation and saves the change
    def delete_game(self):
        if self.backlog.is_empty():
            print("There are no games to delete.")
            return

        index, game = self.select_game_with_index("Delete a Game")
        if game is None:
            return

        while True:
            confirm = input(
                f'Are you sure you want to delete "{game.title}"? (y/n): '
            ).strip().lower()

            if confirm == "y":
                deleted_game = self.backlog.remove_game(index)
                self.storage.save_games(self.filename, self.backlog.get_all_games())
                print(f'\n"{deleted_game.title}" was deleted successfully.')
                return
            elif confirm == "n":
                print("Deletion cancelled.")
                return
            else:
                print(f'"{confirm}" is not valid. Please enter y or n.')


    #Stats Feature

    #Displays stats for the current games
    def show_statistics(self):
        stats = StatisticsManager(self.backlog.get_all_games())

        print("\nGame Statistics")
        print("---------------")
        print(f"Total games: {stats.total_games()}")
        print(f"Completed games: {stats.completed_games_count()}")
        print(f"In progress games: {stats.in_progress_games_count()}")
        print(f"Wishlist games: {stats.wishlist_games_count()}")
        print(f"Total hours played: {stats.total_hours_played():.1f}")
        print(f"Average rating: {stats.average_rating():.1f}/10")
        print(f"Average completion: {stats.average_completion():.1f}%")

    #Recommendation Feature

    #Displays the top 3 recommended backlog games
    def show_top_backlog_recommendations(self):
        recommender = TopThreeBacklogRecommender()
        results = recommender.recommend(self.backlog.get_all_games())

        if not results:
            print("There are no backlog games available for recommendation.")
            return

        self.display_games(results, "Top 3 Backlog Recommendations")

    #Displays the top 3 recommended wishlist games
    def show_top_wishlist_recommendations(self):
        recommender = TopThreeWishlistRecommender()
        results = recommender.recommend(self.backlog.get_all_games())

        if not results:
            print("There are no wishlist games available for recommendation.")
            return

        self.display_games(results, "Top 3 Wishlist Recommendations")

    #Displays one random backlog recommendation
    def show_random_backlog_recommendation(self):
        recommender = RandomBacklogRecommender()
        result = recommender.recommend(self.backlog.get_all_games())

        if result is None:
            print("There are no backlog games available for recommendation.")
            return

        print("\n--- Random Backlog Recommendation ---\n")
        print(result.details())

    #Returns a selected game
    def select_game(self, heading):
        _, game = self.select_game_with_index(heading)
        return game

    #Returns the selected index and game
    def select_game_with_index(self, heading):
        print(f"\n--- {heading} ---")

        games = self.backlog.get_all_games()

        for index, game in enumerate(games, start=1):
            print(f"{index}. {game}")

        while True:
            user_input = input(f"Enter a number between 1 and {len(games)}: ")

            try:
                choice = int(user_input)

                if 1 <= choice <= len(games):
                    return choice - 1, games[choice - 1]

                print(f'"{user_input}" is not valid. Please enter a number between 1 and {len(games)}.')

            except ValueError:
                print(f'"{user_input}" is not valid. Please enter a number between 1 and {len(games)}.')

    #Validation

    #guard against empty text input
    def get_non_empty_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")

    #only allow listed options
    def get_valid_choice(self, prompt, valid_options):
        while True:
            value = input(prompt).strip().title()
            if value in valid_options:
                return value
            print(f"Invalid choice. Valid options are: {', '.join(valid_options)}")

    #only allow integer within range
    def get_valid_int(self, prompt, min_value, max_value):
        while True:
            value = input(prompt).strip()

            try:
                value = int(value)

                if min_value <= value <= max_value:
                    return value

                print(f"Enter a number between {min_value} and {max_value}.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    #only allow float within parameters
    def get_valid_float(self, prompt, min_value):
        while True:
            value = input(prompt).strip()

            try:
                value = float(value)

                if value >= min_value:
                    return value

                print(f"Enter a number greater than or equal to {min_value}.")

            except ValueError:
                print("Invalid input. Please enter a number.")