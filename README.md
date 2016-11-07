# cmps166a-simulation
Toy simulation of shifting outputs, modeling the symbiotic relationship between a mycorrhizal fungus and a tree. "Payoff" to a player is determined by multiple weights of level of content with past engagements, need for resources, and personal health. Environmental factors can be changed and will affect players' needs.

    (for Game Theory and Applications (CMPS/TIM/ECON 166A) project, Fall 2016)

Files:

    tree.py 
        defines tree class, viable moves, and equations that determine its responses and shifting satisfaction
        
    fungus.py 
        defines fungus class, viable moves, and equations that determine its responses and shifting satisfaction
        
    externalconditions.py 
        defines artificial climate/environment changes that impact output of each party/satisfaction levels.
        Occurs based on an rng, more can be added.
        
    runsimulation.py 
        runs each set of equations until they produce the same contribution (output) 20 times in a row, demonstrating
        stability. this number can be changed at will!



