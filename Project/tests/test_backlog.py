import re
from game import Game
from backlog import GameBacklog

#creating a game object to use for testing

def make_game(
    title="DiRT 4",
    genre="Racing",
    store="Steam",
    ownership="Owned",
    status="In Progress",
    rating=7,
    hours_played=28.7,
    completion_percentage=50,
    priority="Low",
    date_added="16/03/2026",
    notes="testtttttttting"
):
    return Game(
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

#test if adding a game increases the count and stores the game correctly
def test_add_game():
    backlog = GameBacklog()
    game = make_game()

    backlog.add_game(game)
    assert backlog.count() == 1
    assert backlog.get_game(0).title == "DiRT 4"

#test if removing a game works correctly
def test_remove_game():
    backlog = GameBacklog()
    game1 = make_game()
    game2 = make_game(
        title="Hogwarts Legacy",
        genre="Action",
        store="Steam",
        ownership="Owned",
        status="Completed",
        rating=9,
        hours_played=45.5,
        completion_percentage=100,
        priority="Low",
        notes="was aight" 
    )
    backlog.add_game(game1)
    backlog.add_game(game2)

    removed = backlog.remove_game(0)
    
    assert removed.title == "DiRT 4"
    assert backlog.count() == 1
    assert backlog.get_game(0).title == "Hogwarts Legacy"

#test if get_game returns the correct game
def test_get_game():
    backlog = GameBacklog()
    game1 = make_game()
    game2 = make_game(
        title="Hogwarts Legacy",
        genre="Action",
        store="Steam",
        ownership="Owned",
        status="Completed",
        rating=9,
        hours_played=45.5,
        completion_percentage=100,
        priority="Low",
        notes="was aight" 
    )
    backlog.add_game(game1)
    backlog.add_game(game2)
    
    game = backlog.get_game(1)
    
    assert game.title == "Hogwarts Legacy"
    assert game.genre == "Action"
    assert game.status == "Completed"

#test if completed_games only returns completed games
def test_completed_games():
    backlog = GameBacklog()
    backlog.add_game(make_game(title="Game A", status="Completed", completion_percentage=100))
    backlog.add_game(make_game(title="Game B", status="In Progress"))
    backlog.add_game(make_game(title="Game C", status="Not Started", hours_played=0.0, completion_percentage=0))

    completed = backlog.completed_games()

    assert len(completed) == 1
    assert completed[0].title == "Game A"

#test if in_progress_games only returns games in progress
def test_in_progress_games():
    backlog = GameBacklog()
    backlog.add_game(make_game(title="Game A", status="In Progress"))
    backlog.add_game(make_game(title="Game B", status="Completed", completion_percentage=100))
    backlog.add_game(make_game(title="Game C", status="Not Started", hours_played=0.0, completion_percentage=0))

    in_progress = backlog.in_progress_games()

    assert len(in_progress) == 1
    assert in_progress[0].title == "Game A"

#test if wishlist_games only returns wishlist games
def test_wishlist_games():
    backlog = GameBacklog()
    backlog.add_game(make_game(title="DiRT 4", ownership="Owned"))
    backlog.add_game(make_game(
        title="Forza Horizon 6",
        genre="Racing",
        ownership="Wishlist",
        status="Not Started",
        rating=10,
        hours_played=0.0,
        completion_percentage=0,
        priority="High",
        notes="Excited"
    ))
    backlog.add_game(make_game(title="Hogwarts Legacy", ownership="Owned", status="Completed", completion_percentage=100))

    wishlist = backlog.wishlist_games()

    assert len(wishlist) == 1
    assert wishlist[0].title == "Forza Horizon 6"
    assert wishlist[0].ownership == "Wishlist"

#test if regex search can find a title match
def test_regex_title():
    backlog = GameBacklog()
    backlog.add_game(make_game())
    backlog.add_game(make_game(
        title="Hogwarts Legacy",
        genre="Action",
        store="Steam",
        ownership="Owned",
        status="Completed",
        rating=9,
        hours_played=45.5,
        completion_percentage=100,
        priority="Low",
        notes="was aight" 
    ))

    result = backlog.search_by_field_regex("title", "hogwarts", re)

    assert len(result) == 1
    assert result[0].title == "Hogwarts Legacy"

#test if regex search can find a genre match
def test_regex_genre():
    backlog = GameBacklog()
    backlog.add_game(make_game())
    backlog.add_game(make_game(
        title="Hogwarts Legacy",
        genre="Action",
        store="Steam",
        ownership="Owned",
        status="Completed",
        rating=9,
        hours_played=45.5,
        completion_percentage=100,
        priority="Low",
        notes="was aight" 
    ))

    result = backlog.search_by_field_regex("genre", "action", re)

    assert len(result) == 1
    assert result[0].title == "Hogwarts Legacy"

#test if regex search returns nothing when there is no match
def test_regex_no_match():
    backlog = GameBacklog()
    backlog.add_game(make_game())
    backlog.add_game(make_game(title="Hogwarts Legacy",
        genre="Action",
        store="Steam",
        ownership="Owned",
        status="Completed",
        rating=9,
        hours_played=45.5,
        completion_percentage=100,
        priority="Low",
        notes="was aight" ))

    result = backlog.search_by_field_regex("title", "elden", re)

    assert result == []

#testing if regex search ignores case
def test_regex_case_insensitive():
    backlog = GameBacklog()
    backlog.add_game(make_game(
        title="Hogwarts Legacy",
        genre="Action",
        store="Steam",
        ownership="Owned",
        status="Completed",
        rating=9,
        hours_played=45.5,
        completion_percentage=100,
        priority="Low",
        notes="was aight" 
    ))

    result = backlog.search_by_field_regex("title", "HOGWARTS", re)

    assert len(result) == 1
    assert result[0].title == "Hogwarts Legacy"