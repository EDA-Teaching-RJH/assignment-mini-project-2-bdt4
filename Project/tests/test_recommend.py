from game import Game
from recommend import (
    TopThreeBacklogRecommender,
    TopThreeWishlistRecommender,
    RandomBacklogRecommender
)

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

#test if the top 3 backlog recommender returns 3 games
def test_top_three_backlog_recommender():
    games = [
        make_dirt4(),
        Game("Game A", "RPG", "Steam", "Owned", "Not Started", 8, 0.0, 0, "High", "16/03/2026", ""),
        Game("Game B", "Action", "Steam", "Owned", "Not Started", 6, 0.0, 0, "Medium", "16/03/2026", ""),
        Game("Game C", "Puzzle", "Steam", "Owned", "Not Started", 9, 0.0, 0, "High", "16/03/2026", "")
    ]

    recommender = TopThreeBacklogRecommender()
    result = recommender.recommend(games)

    assert len(result) == 3

#test if the backlog recommender ignores completed and wishlist games
def test_top_three_backlog_returns_owned_unfinished():
    games = [
        make_dirt4(),
        make_hogwarts(),
        make_forza()
    ]

    recommender = TopThreeBacklogRecommender()
    result = recommender.recommend(games)

    assert len(result) == 1
    assert result[0].title == "DiRT 4"
    assert result[0].ownership == "Owned"
    assert result[0].status != "Completed"

#test if the wishlist recommender only returns wishlist games
def test_top_three_wishlist_returns_wishlist():
    games = [
        make_dirt4(),
        make_hogwarts(),
        make_forza(),
        make_borderlands()
    ]

    recommender = TopThreeWishlistRecommender()
    result = recommender.recommend(games)

    assert len(result) == 2
    assert result[0].ownership == "Wishlist"
    assert result[1].ownership == "Wishlist"

#test if the random backlog recommender gives back an owned unfinished game
def test_random_backlog_recommender():
    games = [
        make_dirt4(),
        make_hogwarts(),
        make_forza()
    ]

    recommender = RandomBacklogRecommender()
    result = recommender.recommend(games)

    assert result is not None
    assert result.ownership == "Owned"
    assert result.status != "Completed"

#test if the random backlog recommender returns None when there are no valid options
def test_random_backlog_recommender_none_case():
    games = [
        make_hogwarts(),
        make_forza()
    ]

    recommender = RandomBacklogRecommender()
    result = recommender.recommend(games)

    assert result is None