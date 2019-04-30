import random


class Game:
    def score(self):
        score = 0

        for x in range(10):
            score = str(random.randint(0, 301))

        return score
