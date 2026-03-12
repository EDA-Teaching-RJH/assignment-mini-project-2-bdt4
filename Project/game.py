class Game:
    def __init__(self, title, genre, store, ownership, status, rating, hours_played, completion_percentage, priority, date_added, notes):
        self.title = title
        self.genre = genre
        self.store = store
        self.ownership = ownership
        self.status = status
        self.rating = rating
        self.hours_played = hours_played
        self.completion_percentage = completion_percentage
        self.priority = priority
        self.date_added = date_added
        self.notes = notes

    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.status}"