#Testing the game class

from game import Game
#creating a  game object to use for testing
def make_game():
    return Game(
        "DiRT 4", #change this game to something else
        "Racing",
        "Steam",
        "Owned",
        "In Progress",
        7,
        28.7,
        50,
        "Low",
        "16/03/2026""
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

def test_game_summary()
    game = make_game()
    summary = game.summary()

    assert "DiRT 4" in summary
    assert "Racing" in summary
    assert "Steam" in summary
    assert "In Progress" in summary   

def test_game_details()
    game = make_game()
    details = game.details()

    assert "Title: DiRT 4" in details
    assert "Genre: Racing" in details
    assert "Status: In Progress" in details

def test_game_to_dict():
    game = make_game()
    data = game.to_dict()

    assert data["title"] == "DiRT 4"
    assert data["genre"] == "Racing"
    assert data["rating"] == 7
    assert data["completion_percentage"] == 50

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

    assert game.title == "Portal 2"
    assert game.rating == 10
    assert game.hours_played == 12.5
    assert game.completion_percentage == 100

def test_game_csv_fields():
    field = Game.csv_fields()
    assert fields == [
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