#Testing the game class

from game import Game
#creating a  game object to use for testing
def make_game():
    return Game(
        "DiRT 4",
        "Racing",
        "Steam",
        "Owned",
        "In Progress",
        7,
        28.7,
        50,
        "Low",
        "16/03/2026",
        "testtttttttting"
    )

def test_game_creation():
    game = make_game()

    assert game.title == "DiRT 4"
    assert game.genre == "Racing"
    assert game.store == "Steam"
    assert game.ownership == "Owned"
    assert game.status == "In Progress"
    assert game.rating == 7
    assert game.hours_played == 28.7
    assert game.completion_percentage == 50
    assert game.priority == "Low"
    assert game.date_added == "16/03/2026"
    assert game.notes == "testtttttttting"

#Testing the short output
def test_game_str_output():
    game = make_game()

    assert str(game) == "DiRT 4 (Racing) - In Progress"

#tests the summary and details outputs
def test_game_summary():
    game = make_game()
    summary = game.summary()

    assert "DiRT 4" in summary
    assert "Racing" in summary
    assert "Steam" in summary
    assert "In Progress" in summary   
    assert "7/10" in summary
    assert "28.7" in summary
    assert "50%" in summary

def test_game_details():
    game = make_game()
    details = game.details()

    assert "Title: DiRT 4" in details
    assert "Genre: Racing" in details
    assert "Store: Steam" in details
    assert "Ownership: Owned" in details
    assert "Status: In Progress" in details
    assert "Rating: 7/10"
    assert "Hours Played: 28.7" in details
    assert "Completion: 50%" in details

#testing to see if the game reads and writes correctly
def test_game_to_dict():
    game = make_game()
    data = game.to_dict()

    assert data["title"] == "DiRT 4"
    assert data["genre"] == "Racing"
    assert data["store"] == "Steam"
    assert data["ownership"] == "Owned"
    assert data["status"] == "In Progress"
    assert data["rating"] == 7
    assert data["hours_played"] == 28.7
    assert data["completion_percentage"] == 50
    assert data["priority"] == "Low"
    assert data["date_added"] == "16/03/2026"
    assert data["notes"] == "testtttttttting"

def test_game_from_dict():
    data = {
        "title": "DiRT 4",
        "genre": "Racing",
        "store": "Steam",
        "ownership": "Owned",
        "status": "In Progress",
        "rating": "7",
        "hours_played": "28.7",
        "completion_percentage": "50",
        "priority": "Low",
        "date_added": "16/03/2026",
        "notes": "testtttttttting"
    }

    game = Game.from_dict(data)

    assert game.title == "DiRT 4"
    assert game.genre == "Racing"
    assert game.store == "Steam"
    assert game.ownership == "Owned"
    assert game.status == "In Progress"
    assert game.rating == 7
    assert game.hours_played == 28.7
    assert game.completion_percentage == 50
    assert game.priority == "Low"
    assert game.date_added == "16/03/2026"
    assert game.notes == "testtttttttting"

#testing to see if the csv fields line up correctly to the games in the csv
def test_game_csv_fields():
    field = Game.csv_fields()
    assert field == [
        "title",
        "genre",
        "store",
        "ownership",
        "status",
        "rating",
        "hours_played",
        "completion_percentage",
        "priority",
        "date_added",
        "notes"
    ]