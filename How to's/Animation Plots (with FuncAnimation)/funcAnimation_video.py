import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

m = 1 # kg
k = 1 # N/m
d = 0.6 # Unit of d

t = np.linspace(0, 40, 501)
w_d = np.sqrt((4*m*k - d**2)/(4*m**2))
x = np.exp(-d/(2*m) * t) * np.cos(w_d * t)

# - - - Creating a figure and Axis with Additionnal configurations and styling of the plot: - - - #

fig, axis = plt.subplots(1, 2)

animated_spring, = axis[0].plot([], [], color='blue') # ',' is used because axis.plot returns an array
animated_mass, = axis[0].plot([], [], 'o', markersize=20, color='red') # ',' is used because axis.plot returns an array

axis[0].set_xlim([-2, 2])
axis[0].set_ylim([-2, 2])
axis[0].grid()

animated_disp, = axis[1].plot([], [], color='red')

axis[1].set_xlim([min(t), max(t)])
axis[1].set_ylim([-2, 2])
axis[1].grid()

# - - - Defining our update function - - - #

def update(frame):
    animated_mass.set_data([x[frame]], [0]) # Updating the data across [frame]
    animated_spring.set_data([-2, x[frame]], [0, 0]) # Updating the data across [frame]

    animated_spring.set_linewidth(int(abs(x[frame]-2)*2))

    animated_disp.set_data(t[:frame], x[:frame])

    return animated_mass, animated_spring, animated_disp


animation = FuncAnimation(
                    fig=fig,
                    func=update,
                    frames=len(t),
                    interval=25,
                    blit=True,
                ) 

animation.save("cool_animation.gif")
plt.show() 