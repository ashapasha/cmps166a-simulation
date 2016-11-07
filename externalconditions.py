from tree import Tree
from fungus import Fungus
import random


def drought(tree, fungus):
    # tree has a increased desperation for nutrients
    tree.desperation += 3
    # fungus struggles and gives fewer minerals, has fewer itself
    fungus.percent_minerals_given = max(fungus.percent_minerals_given - 5, 10)
    fungus.total_minerals = max(15, fungus.total_minerals - 10)


def heavy_rain(tree, fungus):
    # more minerals sink to fungus's reach, fungus less concerned
    fungus.total_minerals = max(50, fungus.total_minerals + 20)
    if fungus.desperation > 0:
        fungus.desperation -= 1
        # tree more willing to barter
        tree.sugar_given += random.randint(2, 5)
    else:
        # overall happier
        fungus.happiness = min(10, fungus.happiness + 1)
        tree.happiness = min(10, tree.happiness + 1)

