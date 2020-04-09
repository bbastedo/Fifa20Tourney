import pandas as pd
import random

randomizer = input("Enter number of times to shuffle the order: ")

print("")

# create list of players to shuffle
players = ['Ben','Cole','Dylan','Brennan','Tyler','Johnny Vodka','Luke D','Luna']

for x in range(0, int(randomizer)):
    random.shuffle(players)

#create df with order placement
df = pd.DataFrame({'Pick':['1','2','3','4','5','6','7','8']})

# create new column in df with shuffled players
df['Shuffle'] = players

# print out orders
print(df)

print("--------------------------------------------------")

# final shuffle for bracks and positioning
random.shuffle(players)

# find length of lsit
length = len(players)
# find the middle index for slicing of list
middle_index = length//2

# slicing the list in half and assigning results to new list
inglewood = players[:middle_index]
bompton = players[middle_index:]

# creating new dataFrame and creating our seedings
seedings = pd.DataFrame({'Seed':['1','2','3','4']})
seedings["Inglewood"] = inglewood
seedings["Bompton"] = bompton

print(seedings)
