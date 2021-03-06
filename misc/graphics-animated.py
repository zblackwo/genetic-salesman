from genetics2 import *
import pygame
import sys
import city_generator
import time
import greedy

numberOfCities = 50
populationCount = 100
generationsBeforeChange = 10
maxMutationRate = 0.05
minTournamentSize = 2
maxTournamentSize = 8
elitismMin = 1
elitismMax = 5

#tourmanager = city_generator.random(numberOfCities)
#tourmanager = city_generator.twenty_fixed()
#tourmanager = city_generator.clickForCities()
tourmanager = city_generator.fetch_fifty_files('fifty.pickle')

def runGreedy(tm):
    cityList = greedy.greedy_TSP(tm)

    tourmanager2 = TourManager()

    for i in range(len(cityList)):
        tourmanager2.addCity(cityList[i])

    tourmanager2.drawCities()
    tourmanager2.takeTour((0,255,0),1)

    text = "Using greedy algorithm, distance = "
    text += str(int(greedy.totalLength(tourmanager2)))
    writeText(text,(255,0,0), 0)

def runGenetic(tm):
    #Creates a "population" of candidates for best-tour (shortest path)
    pop = Population(tm, populationCount, True)
    #print("Got here!")
    pop.drawFittestTour((255,0,0),1)
    text = "After 0 generations, distance = "
    text += str(int(pop.getFittest().getDistance()))
    writeText(text,(255,0,0), 0)
    ga = GA(tm,tournamentSize=3)

    printLocation = 20
    generationCount = 0
    interval = 10
    currentShortest = int(pop.getFittest().getDistance())

    while(True):
        ev = pygame.event.get()
        # proceed events
        for event in ev:
            if event.type == pygame.QUIT:
                sys.exit(0)
        pop = ga.evolvePopulation(pop)
        generationCount += 1
        newShortest = int(pop.getFittest().getDistance())
        if(newShortest != currentShortest):
            window.fill((0,0,0))
            tm.drawCities()
            text = "After "
            text += str(generationCount)
            text += " generations, distance = "
            text += str(int(pop.getFittest().getDistance()))
            text += ", "
            text += str(currentShortest - newShortest)
            text += " units shorter"
            writeText(text,(255,255,255), printLocation)
            pop.drawFittestTour((255,255,255),1)
            pygame.display.flip()
            #time.sleep(0.1)
            currentShortest = newShortest
        #every N generation, change up the parameters of the GA
        if(generationCount%generationsBeforeChange==0):
            #pass
            mutation = random.random()*maxMutationRate
            tournament = random.randint(minTournamentSize,maxTournamentSize)
            elitism = random.randint(elitismMin,elitismMax)
            ga = GA(tm,mutation,tournament,elitism)

def main():
    window.fill((0,0,0))

    runGreedy(tourmanager)

    #runGenetic(tourmanager)

    while(True):
        ev = pygame.event.get()
        # proceed events
        for event in ev:
            if event.type == pygame.QUIT:
                sys.exit(0)



if __name__ == '__main__': main()