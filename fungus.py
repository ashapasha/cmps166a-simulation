import random
import math


class Fungus:
    def __init__(self):
        # status of fungus, alive or dead
        self.isAlive = True
        # can be at max 10, begin at average happiness
        self.happiness = 5
        # can be at max 10, begin with no desperation
        self.desperation = 0
        # can be at max 10, at min 0, begin with no pain
        self.pain = 0
        # can be at max 100, at min 0, start with at least enough to sustain self, and similar padding to max
        self.total_minerals = random.randint(10, 90)
        # can be at max 100, at min 0, start with a random % contribution on the same scale as tree (divide by 5)
        self.percent_minerals_given = random.randint(5, 95)

    # wrapper functions
    def get_contribution(self):
        return math.ceil(float((self.total_minerals * self.percent_minerals_given)/100))

    # Fungus move set
    def withhold(self, amount_given, current_flooding):
        return max(0, amount_given-current_flooding, amount_given-self.pain, 0)

    def concede(self, amount_given):
        return max(amount_given * self.pain, 90)

    def starved(self):
        # unbearable starvation pain, die, if not dead already
        if not self.isAlive:
            return 0
        else:
            self.isAlive = False
            self.percent_minerals_given = 100
            return self.get_contribution()

    def satisfied(self, amount_given):
        if self.happiness < 10:
            self.happiness += 1
        if self.desperation is not 0:
            self.desperation -= 1
        if self.pain is not 0:
            self.pain -= 1
        return amount_given

    def dissatisfied(self, amount_given, current_flooding):
        self.pain += current_flooding
        if self.happiness > 0:
            self.happiness -= 1
        else:
            self.desperation = max(self.desperation + 1, 10)
        if self.desperation < 4 or self.pain < 8:
            return self.withhold(amount_given, current_flooding)
        if self.desperation > 4:
            self.pain += 1
        if self.pain > 8:
            # give as much as possible without dying
            return self.concede(amount_given)
        if self.pain >= 10:
            return self.starved()

    def respond(self, amount_given, amount_received, current_flooding):
        self.total_minerals = max(10 + amount_received, 0)
        if self.total_minerals is 0:
            self.percent_minerals_given = max(0, self.percent_minerals_given)
            return self.dissatisfied(amount_given, current_flooding)
        # if fungus contributions at most = tree's contributions (factoring in desperation and goodwill and pain)
        if amount_given <= (amount_received + self.desperation + self.happiness - current_flooding):
            return self.satisfied(amount_given)
        else:
            return self.dissatisfied(amount_given, current_flooding)
