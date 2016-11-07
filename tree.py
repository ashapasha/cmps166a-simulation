import random


class Tree:

    def __init__(self):
        # can be at max 10, begin at average happiness
        self.happiness = 2
        # can be at max 10, begin with no desperation
        self.desperation = 0
        # can be at max 20 and at min 0, begin giving a random amount above its minimum and below its maximum
        self.sugar_given = random.randint(1, 19)
        # can be at max 100, at min 0, begin at 0
        self.oxygen_flooding = 0

    # wrapper functions
    def get_contribution(self):
        return self.sugar_given

    def get_flooding(self):
        return self.oxygen_flooding

    # Tree's move set
    def threaten(self, amount_given):
        if self.oxygen_flooding < 8:
            self.oxygen_flooding += 2
        elif self.oxygen_flooding < 10:
            self.oxygen_flooding += 1
        return max(amount_given - self.desperation + self.happiness, 0)

    def beg(self, amount_given):
        return min(amount_given + self.desperation, 20)

    # Determine Tree's strategy after positive payoff (makes happiness/desperation adjustments, play same strategy)
    def satisfied(self, amount_given):
        # if it gave less than it needed to, and happiness wasn't at maximum, tree will be happier with relationship
        if self.happiness < 10:
            self.happiness += 1
        # desperation of the tree will also lessen with an exchange it benefits from
        if self.desperation is not 0:
            self.desperation -= 1
        if self.oxygen_flooding > 0:
            self.oxygen_flooding -= 1
        # after adjustments made to desperation and happiness, play the same strategy as last time
        self.sugar_given = amount_given
        return self.sugar_given

    # Determine Tree's strategy after negative payoff (makes happiness/desperation adjustments, plays modified strategy)
    def dissatisfied(self, amount_given):
        # happiness will decrease as much as possible
        self.happiness -= max(self.happiness - 1, 0)
        if self.happiness is 0:
            # if tree is unhappy with relationship and has suffered too much, it becomes desperate for resources
            self.desperation += 2
        if self.desperation > 3:
            # if tree is sufficiently desperate, it will start to offer more to beg for resources
            self.sugar_given = self.beg(amount_given)
            return self.sugar_given
        else:
            # if it was unhappy with the exchange but not sufficiently desperate to beg, it will try to bully the fungus
            # into giving more
            self.sugar_given = self.threaten(amount_given)
            return self.sugar_given

    # how Tree responds to strategy of Fungus
    def respond(self, amount_given, amount_received):
        # multiply amount given by 5 to be on the same scale as fungus contributions, then compare to
        # fungus contribution + how badly it was needed by tree + amount of goodwill in relationship from tree's view
        if (amount_given * 5) <= (amount_received + self.desperation + self.happiness):
            return self.satisfied(amount_given)
        else:
            # otherwise, if the tree didn't get as much as it gave, determine whether to beg or threaten
            return self.dissatisfied(amount_given)

