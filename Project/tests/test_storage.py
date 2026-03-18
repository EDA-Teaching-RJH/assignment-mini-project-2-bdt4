#Testing the storage class

from game import Game
from storage import CSVStorage

#create a game object 
def make_dirt4():
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

def make_hogwarts():
    return Game(
        "Hogwarts Legacy",
        "Action",
        "Steam",
        "Owned",
        "Completed",
        9,
        45.5,
        100,
        "Low",
        "16/03/2026",
        "was aight"
    )

def make_forza():
    return Game(
        "Forza Horizon 6",
        "Racing",
        "Steam",
        "Wishlist",
        "Not Started",
        10,
        0.0,
        0,
        "High",
        "16/03/2026",
        "Excited"
    )

#create a wishlist game
def make_borderlands():
    return Game(
        "Borderlands 4",
        "Shooter",
        "Steam",
        "Wishlist",
        "Not Started",
        10,
        0.0,
        0,
        "High",
        "16/03/2026",
        "Looks good"
    )

#test if saving and loading games keeps the data intact
def test_save_and_load_games(tmp_path):
    filename = tmp_path / "test_games.csv"

    games = [
        make_dirt4(),
        make_hogwarts(),
        make_forza(),
        make_borderlands()
    ]

    storage = CSVStorage()

    storage.save_games(filename, games)
    loaded_games = storage.load_games(filename)

    assert len(loaded_games) == 4
    assert loaded_games[0].title == "DiRT 4"
    assert loaded_games[1].title == "Hogwarts Legacy"
    assert loaded_games[2].title == "Forza Horizon 6"
    assert loaded_games[3].title == "Borderlands 4"

    assert loaded_games[0].hours_played == 28.7
    assert loaded_games[1].completion_percentage == 100
    assert loaded_games[2].ownership == "Wishlist"
    assert loaded_games[3].rating == 10


#test if saving and loading an empty list still works
def test_save_and_load_empty_list(tmp_path):
    filename = tmp_path / "empty_games.csv"

    games = []

    storage = CSVStorage()

    storage.save_games(filename, games)
    loaded_games = storage.load_games(filename)

    assert loaded_games == []