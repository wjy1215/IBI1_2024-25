import numpy as np
import matplotlib.pyplot as plt

def run_sir_model(vaccination_percentage):
    N = 10000  
    vaccinated = int(N * vaccination_percentage)
    S = N - 1 - vaccinated  # Initial number of susceptible individuals
    if S < 0:
        S = 0
    I = 1      # Initial number of infected individuals
    R = 0      # Initial number of recovered individuals

    beta = 0.3  # Infection probability
    gamma = 0.05  # Recovery probability
    # Create arrays to track the evolution of S, I, and R over time
    time_steps = 1000
    S_history = [S]
    I_history = [I]
    R_history = [R]

    for t in range(time_steps):
        # Calculate the infection probability for each susceptible individual
        if S > 0:
            infection_prob = beta * (I / N)
        else:
            infection_prob = 0
        
        # Randomly select susceptible individuals to become infected
        new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob])
        num_new_infections = np.sum(new_infections)
        
        # Randomly select infected individuals to recover
        recovery_prob = gamma
        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - recovery_prob, recovery_prob])
        num_new_recoveries = np.sum(new_recoveries)
        
        # Update the counts
        S -= num_new_infections
        I = I - num_new_recoveries + num_new_infections
        R += num_new_recoveries
        
        # Record the current state
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)

    return I_history

# Test different vaccination percentages
vaccination_percentages = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1.0]
infected_curves = []

for vp in vaccination_percentages:
    print(f"Running simulation with {vp*100}% vaccination")
    infected = run_sir_model(vp)
    infected_curves.append(infected)

# Plot the results
plt.figure(figsize=(10, 6), dpi=100)
i=0
for vp in vaccination_percentages:
    plt.plot(infected_curves[i], label=f'{vp*100}% vaccinated')
    i+=1

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('Impact of Vaccination on Disease Spread')
plt.legend()
plt.show()