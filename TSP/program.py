"""
How to Run:
python program.py <name of input file> <name of dataset>
a new best order and distance will keep being calculated
record the latest best order and distance when you are satisfied
quit the program with ctrl-c
"""

import sys
import math
import random

points = []
populationSize = 200
mutationChance = 0.03
population = []
fitness = [None for i in range(populationSize)]
smallestDistance = float("inf")
bestOrder = None
currBest = None


def getPoints():
    global points, numpoints
    dataset = sys.argv[2]
    fin = open(sys.argv[1], "r")
    lines = fin.readlines()
    for i in range(len(lines)):
        if len(lines[i].split(",")) == 2:
            if lines[i].split(",")[0] == dataset:
                header = i
                break
    numpoints = len(lines[header + 3].split(","))
    xvals = [int(x) for x in lines[header + 1].split(",")]
    yvals = [int(y) for y in lines[header + 2].split(",")]
    for i in range(numpoints):
        points.append([xvals[i], yvals[i]])


def makeOrdered(order):
    ordered = [points[i] for i in order]
    return ordered


def calcDistance(order):
    ordered = makeOrdered(order)
    ordered.append(ordered[0])
    sum = 0
    for i in range(len(ordered) - 1):
        distance = math.sqrt(
            (ordered[i + 1][0] - ordered[i][0]) ** 2
            + (ordered[i + 1][1] - ordered[i][1]) ** 2
        )
        sum += distance
    return sum


def createPopulation():
    numpoints = len(points)
    initial = [i for i in range(numpoints)]
    for i in range(populationSize):
        shuffled = random.sample(initial, numpoints)
        population.append(shuffled)


def calcFitness():
    global bestOrder, currBest, smallestDistance
    curr = float("inf")
    for i in range(populationSize):
        distance = calcDistance(population[i])
        if population[i][0] == 0 and distance < smallestDistance:
            smallestDistance = distance
            bestOrder = population[i]
        if distance < curr:
            curr = distance
            currBest = population[i]
        fitness[i] = 1 / (distance ** 10)


def normFitness():
    global fitness
    sum = 0
    for val in fitness:
        sum += val
    fitness = [val / sum for val in fitness]


def choose(values, probability):
    i = 0
    rand = random.random()
    while rand > 0:
        rand = rand - probability[i]
        i += 1
    i -= 1
    return values[i][:]


def crossover(first, second):
    start = random.randint(0, len(first) - 1)
    end = random.randint(start + 1, len(first)) % numpoints
    new = first[start:end]
    for i in range(len(second)):
        point = second[i]
        if point not in new:
            new.append(point)
    return new


def mutate(order, probability):
    for i in range(numpoints):
        if random.random() < probability:
            j = random.randint(0, len(order) - 1)
            h = (j + 1) % numpoints
            temp = order[j]
            order[j] = order[h]
            order[h] = temp


def nextPopulation():
    global population
    newPopulation = [None for i in range(populationSize)]
    for i in range(len(population)):
        first = choose(population, fitness)
        second = choose(population, fitness)
        order = crossover(first, second)
        mutate(order, mutationChance)
        newPopulation[i] = order
    population = newPopulation


def calcBest():
    calcFitness()
    normFitness()
    nextPopulation()


def main():
    global bestOrder
    if len(sys.argv) != 3:
        print("invalid number of arguments")
        return
    getPoints()
    createPopulation()
    while True:
        oldBest = bestOrder
        calcBest()
        if bestOrder != oldBest:
            print("NEW BEST:")
            print(",".join([str(i) for i in bestOrder]))
            print(smallestDistance)
            print()


main()
