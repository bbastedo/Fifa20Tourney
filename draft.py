import pandas as pd
import random

randomizer = input("Enter number of times to shuffle the order: ")

# create list of players to shuffle
players = ['Ben','Cole','Dylan','Brennan','Tyler','Johnny Vodka','Luke D','Luna']

for x in range(0, int(randomizer)):
    random.shuffle(players)

#create df with order placement
df = pd.DataFrame({'Order':['1','2','3','4','5','6','7','8']})

# create new column in df with shuffled players
df['Shuffle'] = players

# print out orders
print(df)
