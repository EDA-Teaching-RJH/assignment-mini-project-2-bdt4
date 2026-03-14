#Game class that prints out game entries, will be more complex later
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

#basic printout for menus and quick lists
    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.status}"
    
    #More detailed one line summary
    def summary(self):
        return (
            f"{self.title} | {self.genre} | {self.store} | {self.status} | "
            f"Rating: {self.rating}/10 | Hours: {self.hours_played} | "
            f"{self.completion_percentage}%"
        )

    # Full detail view
    def details(self):
        return (
            f"Title: {self.title}\n"
            f"Genre: {self.genre}\n"
            f"Store: {self.store}\n"
            f"Ownership: {self.ownership}\n"
            f"Status: {self.status}\n"
            f"Rating: {self.rating}/10\n"
            f"Hours Played: {self.hours_played}\n"
            f"Completion: {self.completion_percentage}%\n"
            f"Priority: {self.priority}\n"
            f"Date Added: {self.date_added}\n"
            f"Notes: {self.notes if self.notes else 'None'}"
        )