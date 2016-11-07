from tree import Tree
from fungus import Fungus
from externalconditions import drought, heavy_rain
import random

player_tree = Tree()
player_fungus = Fungus()
equilibrium_reached = False
run_number = 0
next_fungus_strategy = 0
next_tree_strategy = 0
consistent_contribution_count = 0

while not equilibrium_reached:
    if player_fungus.isAlive is False:
        print "Tree has killed the fungus."
        equilibrium_reached = True

    curr_fungus_strategy = player_fungus.get_contribution()
    curr_tree_strategy = player_tree.get_contribution()

    print "We are on run number: %d" % run_number
    print "Tree gave this much: \n %d" % curr_tree_strategy
    print "Fungus gave this much: \n %d" % curr_fungus_strategy

    # external conditions: 1 = drought, 2 = heavy rain, 3 = standard weather
    weather_type = random.randint(1, 3)
    if weather_type is not 3:
        drought(player_tree, player_fungus) if weather_type is 1 else heavy_rain(player_tree, player_fungus)

    next_tree_strategy = player_tree.respond(curr_tree_strategy, curr_fungus_strategy)
    next_fungus_strategy = player_fungus.respond(curr_fungus_strategy, curr_tree_strategy,
                                                 player_tree.get_flooding())
    # natural replenishing of minerals in soil
    player_fungus.total_minerals += random.randint(0, 20)
    run_number += 1
    if curr_fungus_strategy is next_fungus_strategy and curr_tree_strategy is next_tree_strategy:
        consistent_contribution_count += 1
    else:
        consistent_contribution_count -= 1
    if consistent_contribution_count > 20:
        print "Equilibrium found at run number %d! Tree contribution = %d, Fungus contribution = %d" % (
            run_number, next_tree_strategy, next_fungus_strategy)
        equilibrium_reached = True
