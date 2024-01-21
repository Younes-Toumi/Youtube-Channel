import numpy as np
import matplotlib.pyplot as plt

N_samples = 100_000
N_random_samples = 1000
I_array = []

x_sample = np.random.uniform(0, 1, N_samples)
y_sample = np.random.uniform(0, 1, N_samples)
z_sample = np.random.uniform(0, 1, N_samples)

for i in range(1, 100_000):

    x = np.random.choice(x_sample, N_random_samples)
    y = np.random.choice(x_sample, N_random_samples)
    z = np.random.choice(x_sample, N_random_samples)

    func = np.exp(-(x**2 + y**2 + z**2)) * np.sin(x*y) * np.cos(z) #Modelling

    I = (1-0)**3 * np.sum(func)/N_random_samples

    I_array.append(I)

final_I = np.average(I_array)
print(f"The integral between [0, 1] is: {final_I}")

fig, axis = plt.subplots()

histogram = plt.hist(I_array, bins=50, color ='green', alpha = 0.7, edgecolor='black')
axis.set_xlim([min(I_array), max(I_array)])
axis.set_title(f"Integral of f(x, y, z) between [0, 1] is: {np.average(I_array):.5f}")

plt.show()



