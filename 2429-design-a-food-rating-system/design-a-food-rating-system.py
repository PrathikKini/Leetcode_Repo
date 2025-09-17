from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        # cuisine -> sorted list of (-rating, food)
        self.cuisine_ratings = defaultdict(SortedList)
        # food -> cuisine
        self.food_cuisine = {}
        # food -> rating
        self.food_rating = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.cuisine_ratings[c].add((-r, f))
            self.food_cuisine[f] = c
            self.food_rating[f] = r

    def changeRating(self, food, newRating):
        cuisine = self.food_cuisine[food]
        oldRating = self.food_rating[food]

        # remove old rating
        self.cuisine_ratings[cuisine].remove((-oldRating, food))
        # add new rating
        self.cuisine_ratings[cuisine].add((-newRating, food))

        # update
        self.food_rating[food] = newRating

    def highestRated(self, cuisine):
        # first element is max rating, lexicographically smallest food
        return self.cuisine_ratings[cuisine][0][1]
