# genetic-salesman
Solving the Travelling Salesman problem with a genetic algorithm

This one is from a research project I did this summer involving Genetic Algorithms. In essence, the purpose of the program is to compare 3 solutions to the Travelling Salesman Problem:

1. A basic greedy algorithm, which I borrowed from another source
2. A basic genetic algorithm which I borrowed from another source and modified (to include periodic variability in mutation rates, etc.)
3. A hybrid algorithm in which I used the solution generated by the greedy algorithm as a seed value for the genetic algorithm

I then added code to run all three and compare them in terms of runtime and ultimate solution, and to collect data from a large number of runs and save it to a file. I also used PyGame to create a visual interface which shows the genetic algorithms working out solutions, then displays and compares the final solutions. 

**REQUIRES PYGAME TO RUN**
