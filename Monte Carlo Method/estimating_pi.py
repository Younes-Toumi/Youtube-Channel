import numpy as np
import matplotlib.pyplot as plt


def plot_construction():
    fig, axis = plt.subplots(1, 2, figsize=(10, 5))

    # Generated Dots
    axis[0].set_title('Random Generated Dots')
    axis[0].set_aspect('equal')
    axis[0].set_xlim([-1, 1])
    axis[0].set_ylim([-1, 1])

    # Plot of Approximation
    axis[1].set_title('Approximating π ~')
    axis[1].set_xlim([0, 1000])
    axis[1].set_ylim([0, 10])
    axis[1].grid()

    return axis

axis = plot_construction()

N_samples = np.arange(1, 100_000)
pi_counter = 0

dots_x = []
dots_y = []

dots_color = []
pi_array = []

scatter = axis[0].scatter(dots_x, dots_y, color=dots_color, marker='o', s=5)
plot, = axis[1].plot([], pi_array, 'black')

for N in N_samples:

    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)

    dots_x.append(x)
    dots_y.append(y)

    if np.sqrt(x**2+y**2) <= 1:
        pi_counter += 1
        dots_color.append('red')

    else:
        dots_color.append('blue')

    probability = pi_counter/N
    approx_pi = 4*probability

    pi_array.append(approx_pi)

    # Updating the plots
    if N%100 == 0:
        scatter.set_offsets(np.column_stack((dots_x, dots_y)))
        scatter.set_facecolors(dots_color)
        axis[0].set_title(f"Red Dots: {pi_counter}, Blue Dots:{N-pi_counter}")

        plot.set_data(range(1, N+1), pi_array)
        plot.set_color('black')

        if N%2000 == 0:
            axis[1].set_xlim([0, N+2000])
            axis[1].set_ylim([approx_pi-1/approx_pi, approx_pi+1/approx_pi])
            axis[1].set_title(f'Approximating π ~ {approx_pi:.5f}')


        plt.draw()
        plt.pause(0.01)

plt.show()
   
    