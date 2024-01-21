import numpy as np
import matplotlib.pyplot as plt


# Defining our problem

a = 110
length = 50 #mm
time = 4 #seconds
nodes = 20

# Initialization 

dx = length / nodes
dt = 0.5 * dx**2 / a
t_nodes = int(time/dt)

u = np.zeros(nodes) + 20 # Plate is initially as 20 degres C

# Boundary Conditions 

u[0] = 100
u[-1] = 100


# Visualizing with a plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])

# Simulating

counter = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes - 1):

        u[i] = dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2 + w[i]

    counter += dt

    print("t: {:.3f} [s], Average temperature: {:.2f} Celcius".format(counter, np.average(u)))

    # Updating the plot

    pcm.set_array([u])
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)


plt.show()













