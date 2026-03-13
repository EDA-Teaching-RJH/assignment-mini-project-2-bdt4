from datetime import datetime
from game import Game

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip().title()

        if value:
            return value
        print("Input cannot be empty. Please try again.")

def get_valid_choice(prompt, valid_options):
    while True:
        value = input(prompt).strip().title()

        if value in valid_options:
            return value
        
        print(f'Invalid choice. Valid options are: {", ".join(valid_options)}')

def get_valid_int(prompt, min_value, max_value):
    while True:
        value = input(prompt).strip()

        try: 
            value = int(value)

            if min_value <= value <= max_value:
                return value
        
            print(f"Enter a number between {min_value} and {max_value}.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_valid_float(prompt, min_value):
    
    while True:
        value = input(prompt).strip()

        try:
            value = float(value)

            if value >= min_value:
                return value
            
            print(f"Enter a number greater than or equal to {min_value}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


#Adds a new game to the current game list
def add_game(games):
    print("\n---Add a new game---")

    #collect game details from the user
    title = get_non_empty_input("Enter title: ")
    genre = get_non_empty_input("Enter genre: ")
    store = input("Enter store: ")

    ownership = get_valid_choice(
    "Enter ownership (Owned, Wishlist, Game Pass): ",
    ["Owned", "Wishlist", "Game pass"]
)

    status = get_valid_choice(
    "Enter status (Completed, In progress, Not Started): ",
    ["Completed", "In Progress", "Not Started"]
)

    rating = get_valid_int("Enter rating (0-10): ", 0, 10)
    hours_played = get_valid_float("Enter hours played: ", 0)
    completion_percentage = get_valid_int("Enter completion percentage (0-100): ", 0, 100) 

    priority = get_valid_choice(
    "Enter priority (Low, Medium, High): ",
    ["Low", "Medium", "High"]
)
    
    date_added = datetime.now().strftime("%d/%m/%Y")

    notes = input("Enter notes (optional): ").strip()

    #Create a new game object using the entered values
    new_game = Game(
        title,
        genre,
        store,
        ownership,
        status,
        rating,
        hours_played,
        completion_percentage,
        priority,
        date_added,
        notes
    )

    #Add the new game to the existing list
    games.append(new_game)

    print(f'\n"{title}" was added successfully.')

def delete_game(games):

    #check if there are any games in the manager
    if len(games) == 0:
        print("There are no games to delete")
        return
        
    print("\n ---Delete a Game ---")

    #Display games using a numbered system for deletion
    for index, game in enumerate(games, start=1):
        print(f"{index}. {game.title} ({game.genre}) - {game.status}")

    print(f"There are currently {len(games)} games.")

    while True:

        user_input = input(f"Enter a number between 1 and {len(games)}: ")       
                            
        try:
            choice = int(user_input)

             #Checking if the number chosen is valid
            if 1 <= choice <= len(games):
                deleted_game = games.pop(choice - 1)
                print(f'\n"{deleted_game.title}" was deleted successfully.')
                return
                        
            print(f'"{user_input}" is not valid. Please enter a number between 1 and {len(games)}.')

        except ValueError:
            print(f'"{user_input}" is not valid. Please enter a number between 1 and {len(games)}.')