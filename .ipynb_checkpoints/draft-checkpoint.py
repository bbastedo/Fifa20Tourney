import pandas as pd
import random
import pprint

pp = pprint.PrettyPrinter(indent=2)

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
    uno = players[:middle_index]
    dos = players[middle_index:]
    
    length = len(uno)
    middle_index=length//2
    
    divone = uno[:middle_index]
    divtwo = uno[middle_index:]
    divthree = dos[:middle_index]
    divfour = dos[middle_index:]

    # creating new dataFrame and creating our seedings
    seedings = pd.DataFrame({'Seed':['1','2','3','4']})
    seedings["Liberty City"] = divone
    seedings["Alderney"] = divtwo
    seedings["San Andreas"] = divthree
    seedings["Los Santos"] = divfour

    print("Division Breakdown:")
    print(" ")
#     print("Divison One:")
    pp.pprint(seedings["Liberty City"])
    print("--------------------------------------------------")
#     print("Divison Two:")
    pp.pprint(seedings["Alderney"])
    print("--------------------------------------------------")
#     print("Divison Three:")
    pp.pprint(seedings["San Andreas"])
    print("--------------------------------------------------")
#     print("Divison Four:")
    pp.pprint(seedings["Los Santos"])
    print("--------------------------------------------------")
    

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
    uno = players[:middle_index]
    dos = players[middle_index:]
    
    length = len(uno)
    middle_index=length//2
    
    divone = uno[:middle_index]
    divtwo = uno[middle_index:]
    divthree = dos[:middle_index]
    divfour = dos[middle_index:]

    # creating new dataFrame and creating our seedings
    seedings = pd.DataFrame({'Seed':['1','2','3','4']})
    seedings["Liberty City"] = divone
    seedings["Alderney"] = divtwo
    seedings["San Andreas"] = divthree
    seedings["Los Santos"] = divfour

    #     print("Divison One:")
    pp.pprint(seedings["Liberty City"])
    print("--------------------------------------------------")
#     print("Divison Two:")
    pp.pprint(seedings["Alderney"])
    print("--------------------------------------------------")
#     print("Divison Three:")
    pp.pprint(seedings["San Andreas"])
    print("--------------------------------------------------")
#     print("Divison Four:")
    pp.pprint(seedings["Los Santos"])
    print("--------------------------------------------------")
