def solve(numheads, numlegs):
    numOfRabbits = int(numlegs / 4)
    numOfChickens = numheads - numOfRabbits
    print("Number of chickens: ", numOfRabbits, "; Number of rabbits: ", numOfChickens)

numheads = 35
numlegs = 94
solve(numheads, numlegs)