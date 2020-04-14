import pandas as pd
import random

randomizer = input("Enter number of times to shuffle the order: ")
print("--------------------------------------------------")

print("")

# create list of players to shuffle
players = ['Ben B.','Blake Thib','Brennan W.','Cole D.','Dylan, Pretty','Jeremy','Johnny Vodka','Kyle','Lucas D','Erick "Guapo" Luna','Saul','Stan','Travis','Ty Webre','Tyler Bartz','Tyler Thompson']

for x in range(0, int(randomizer)):
    random.shuffle(players)

#create df with order placement
df = pd.DataFrame({'Pick':['1','2','3','4','5','6','7','8',9,10,11,12,13,14,15,16]})

# create new column in df with shuffled players
df['Shuffle'] = players

print("Draft Order: ")
print(" ")

# print out orders
print(df)

print("--------------------------------------------------")

seeds = input("Would you like to see the division breakdown? Y/N ")
print(" ")

if seeds.lower() == "y":

    # final shuffle for bracks and positioning
    random.shuffle(players)

    # find length of lsit
    length = len(players)
    # find the middle index for slicing of list
    middle_index = length//2

    # slicing the list in half and assigning results to new list
    vicecity = players[:middle_index]
    santos = players[middle_index:]

    # creating new dataFrame and creating our seedings
    seedings = pd.DataFrame({'Seed':['1','2','3','4','5','6','7','8']})
    seedings["Vice City"] = vicecity
    seedings["Los Santos"] = santos

    print("Division Breakdown:")
    print(" ")
    print(seedings)

else:
    print("Too bad!")
    print("--------------------------------------------------")
    print("Division Breakdown:")
    print(" ")
    
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
    seedings = pd.DataFrame({'Seed':['1','2','3','4','5','6','7','8']})
    seedings["Inglewood"] = inglewood
    seedings["Bompton"] = bompton

    print(seedings)
