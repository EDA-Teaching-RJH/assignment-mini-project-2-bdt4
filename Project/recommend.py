import random


class Recommender:
    def recommend(self, games):
        raise NotImplementedError("Subclasses must implement recommend().")


#Recommends the top 3 backlog games using a scoring system
class TopThreeBacklogRecommender(Recommender):

    #Calculates the score for one backlog game
    def score(self, game):
        score = game.rating * 2

        if game.priority == "High":
            score += 10
        elif game.priority == "Medium":
            score += 5

        score -= game.completion_percentage
        return score

    #Returns the top 3 recommended backlog games
    def recommend(self, games):
        candidates = [
            game for game in games
            if game.ownership == "Owned" and game.status != "Completed"
        ]

        ranked = sorted(candidates, key=self.score, reverse=True)
        return ranked[:3]


#Recommends the top 3 wishlist games using rating and priority
class TopThreeWishlistRecommender(Recommender):

    # Calculates the score for one wishlist game
    def score(self, game):
        score = game.rating * 2

        if game.priority == "High":
            score += 10
        elif game.priority == "Medium":
            score += 5

        return score

    #Returns the top 3 recommended wishlist games
    def recommend(self, games):
        candidates = [game for game in games if game.ownership == "Wishlist"]

        ranked = sorted(candidates, key=self.score, reverse=True)
        return ranked[:3]


#Returns one random unfinished backlog game
class RandomBacklogRecommender(Recommender):

    #Returns one random backlog recommendation
    def recommend(self, games):
        candidates = [
            game for game in games
            if game.ownership == "Owned" and game.status != "Completed"
        ]

        if not candidates:
            return None

        return random.choice(candidates)