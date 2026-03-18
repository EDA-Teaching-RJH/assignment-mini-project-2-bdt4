from game import Game
from stats import StatisticsManager

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

#create another game object
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

#test if total_games counts everything in the list
def test_total_games():
    games = [make_dirt4(), make_hogwarts()]
    stats = StatisticsManager(games)

    assert stats.total_games() == 2

#test if completed_games_count only counts completed games
def test_completed_games_count():
    games = [make_dirt4(), make_hogwarts()]
    stats = StatisticsManager(games)

    assert stats.completed_games_count() == 1

#test if in_progress_games_count only counts games in progress
def test_in_progress_games_count():
    games = [make_dirt4(), make_hogwarts()]
    stats = StatisticsManager(games)

    assert stats.in_progress_games_count() == 1

#test if wishlist_games_count returns 0 when there are no wishlist games
def test_wishlist_games_count():
    games = [make_dirt4(), make_hogwarts()]
    stats = StatisticsManager(games)

    assert stats.wishlist_games_count() == 0

#test if total_hours_played adds together all hours correctly
def test_total_hours_played():
    games = [make_dirt4(), make_hogwarts()]
    stats = StatisticsManager(games)

    assert stats.total_hours_played() == 74.2

#test if average_rating is worked out correctly
def test_average_rating():
    games = [make_dirt4(), make_hogwarts()]
    stats = StatisticsManager(games)

    assert stats.average_rating() == 8.0

#test if average_rating returns 0 when there are no positive ratings
def test_average_rating_zero_case():
    games = [
        Game("Game A", "Rpg", "Steam", "Owned", "Not Started", 0, 0.0, 0, "Low", "16/03/2026", ""),
        Game("Game B", "Action", "Steam", "Owned", "Not Started", 0, 0.0, 0, "Low", "16/03/2026", "")
    ]
    stats = StatisticsManager(games)

    assert stats.average_rating() == 0

#test if average_completion is worked out correctly
def test_average_completion():
    games = [make_dirt4(), make_hogwarts()]
    stats = StatisticsManager(games)

    assert stats.average_completion() == 75.0