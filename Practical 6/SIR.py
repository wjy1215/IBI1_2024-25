import numpy as np
import matplotlib.pyplot as plt
N=10000
beta=0.3
gamma=0.05
N = 10000  
S = N - 1  
I = 1     
R = 0 
time_steps = 1000
S_history = [S]
I_history = [I]
R_history = [R]
for i in range(time_steps):
    infection_prob = beta*(I/N)
    new_infections = np.random.choice([0, 1], S, p=[1 - infection_prob, infection_prob])
    num_new_infections = np.sum(new_infections)
    recovery_prob = gamma
    new_recoveries = np.random.choice([0, 1], I, p=[1 - recovery_prob, recovery_prob])
    num_new_recoveries = np.sum(new_recoveries)
    S -= num_new_infections
    I = I - num_new_recoveries + num_new_infections
    R += num_new_recoveries
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(S_history, label='Susceptible')
plt.plot(I_history, label='Infected')
plt.plot(R_history, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()