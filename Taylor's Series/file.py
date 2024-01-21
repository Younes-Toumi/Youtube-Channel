import numpy as np
from math import factorial
import matplotlib.pyplot as plot

x = np.linspace(-10, 10, 100)
y = np.zeros(len(x))
y_cos = np.cos(x)

figure = plot.figure()

for n in range(0, 40):
    #cos(x)
    taylor_term = (-1)**n * x**(2*n)/factorial(2*n)
    y = np.add(y, taylor_term)

    figure.clear()

    axis = figure.subplots()
    axis.plot(x, y)
    axis.set_xlabel('x')
    axis.set_ylabel('cos(x)')
    axis.set_title('Terms :{}'.format(n+1))

    plot.xlim(min(x), max(x))
    plot.ylim(-2, 2)

    plot.grid()
    plot.draw()

    plot.pause(0.05)


print(np.add(y, -y_cos))
plot.show()