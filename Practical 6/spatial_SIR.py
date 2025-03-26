'''
Import numpy and matplotlib libraries
Create a 100x100 grid of zeros to represent the population
Randomly select one cell to be the initial infected person
Set model parameters: infection probability, recovery probability, and number of time steps
Initialize a list to store the population state at each time step
Loop through each time step:
    Create a copy of the current population
    For each cell in the grid:
        If the cell is infected:
            Check all 8 neighboring cells
            For each susceptible neighbor:
                Infect it with probability beta
            Recover with probability gamma
    Update the population to the new state
    Store the new population state
Create a 2x2 grid of subplots
For each selected time point:
    Display the population state as an image
    Add a title and turn off axes
Adjust the layout and show the plot'''
import numpy as np
import matplotlib.pyplot as plt
population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3 
gamma = 0.05 
time_steps = 100  
population_history = [population.copy()]
for t in range(time_steps):
    new_population = population.copy()
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1: 
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue 
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 100 and 0 <= nj < 100:
                            if population[ni, nj] == 0: 
                                if np.random.rand() < beta:
                                    new_population[ni, nj] = 1
                if np.random.rand() < gamma:
                    new_population[i, j] = 2
    population = new_population
    population_history.append(population.copy())
fig, axes = plt.subplots(2,2, figsize=(10, 10))
time_points = [0, 10, 50, 99]
for ax, t in zip(axes.flatten(), time_points):
    ax.imshow(population_history[t], cmap='viridis', interpolation='nearest')
    ax.set_title(f'Time Step {t}')
    ax.axis('off')
plt.tight_layout()
plt.show()

