########### SETUP DRINK ###########

import random

random.seed()  # init random num gen

liquors = []
liqueurs = []
mixers = []
garnishes = []
directions = []
glassware = []
recipe = []
garnishFlag = random.randint(0, 1)

# populate list of liquors
with open('liquors.txt', 'r') as f:
    for line in f:
        liquors.append(line.rstrip())

# populate list of liqueurs
with open('liqueurs.txt', 'r') as f:
    for line in f:
        liqueurs.append(line.rstrip())

# populate list of mixers
with open('mixers.txt', 'r') as f:
    for line in f:
        mixers.append(line.rstrip())

# populate list of directions
with open('directions.txt', 'r') as f:
    for line in f:
        directions.append(line.rstrip())
        
# populate list of garnishes
with open('garnishes.txt', 'r') as f:
    for line in f:
        garnishes.append(line.rstrip())

# populate list of glassware
with open('glassware.txt', 'r') as f:
    for line in f:
        glassware.append(line.rstrip())

# build random cocktail structure
# numLiquids = random.randint(3, 6)
# drinkStructure = random.sample(range(0, len(liquors)), numLiquids)
# for x in range(0, len(drinkStructure)):
#    recipe.append(liquors[drinkStructure[x]])
totalings = random.randrange(3, 6)
sample = random.randrange(1, 2)
recipe += (random.sample(liquors, sample))
if totalings - sample > 0:
    totalings -= sample
else:
    totalings = 0

recipe += (random.sample(liqueurs, random.randrange(0, totalings)))
if totalings - sample > 0:
    totalings -= sample
else:
    totalings = 0

recipe += (random.sample(mixers, random.randrange(0, totalings)))

########### DISPLAY RECIPE ###########

for i in range(0, len(recipe)):
    n = random.randint(1, 4)
    if n < 2:
        grammar = ' part '
    if n >= 2:
        grammar = ' parts '
    if (('bitters' in recipe[i].lower()) and (n < 2)):
        grammar = ' dash '
    if (('bitters' in recipe[i].lower()) and (n >= 2)):
        grammar = ' dashes '
    output = str(n) + grammar + recipe[i]
    print output

output = random.choice(directions)
print output

if garnishFlag == 1:
    inOrOnEdge = random.randint(1, 4)  # 0 for in drink, 1 for on edge
    if inOrOnEdge == 1:
        output = 'Garnish with ' + random.choice(garnishes) + ' on the edge of the glass.'
    elif inOrOnEdge == 2:
        output = "Place " + random.choice(garnishes) + " adjacent to glass."
    elif inOrOnEdge == 3:
        output = "Light on fire." #sounded redundant coming before the glassware line
    elif inOrOnEdge == 4:
        output = "Wave near " + random.choice(garnishes) + "."
    else:
        output = 'Garnish with ' + random.choice(garnishes) + ' in the cocktail.'
    print output

output = 'Serve in ' + random.choice(glassware)
print output