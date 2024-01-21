import numpy as np

import matplotlib.pyplot as plot

#trying to kill a sin function after some time t_d
#                      0   if x1 < a
#heaviside(x1-a, x2) =  x2   if x1 == a
#                      1   if x1 > a


a = 15
x = np.linspace(0, 30, 3000)

y = np.sin(x)
y_dead = (- np.heaviside(x-a, 0) + 1)*np.sin(x) + np.heaviside(x-a, 0)*np.exp(-5*(x-a)/a)*np.sin(x)



Figure1 = plot.figure('Plotting with python', figsize= (8,4))
axis = Figure1.subplots()


axis.plot(x, y, '--', label='Immortal signal')
axis.plot(x, y_dead, color='black', label='Dying signal')

axis.set_title('Plotting the function y = f(x) dying at x={}'.format(a))
axis.set_xlabel('Data x')
axis.set_ylabel('Data y')
axis.set_xlim(min(x), max(x))
axis.set_ylim(min(y), 2*max(y))
axis.grid()
axis.legend()


axis.plot([a, a], [min(y), 2*max(y) ], '--', color='r')
plot.annotate('Before Decay', xy = (2.5, 1.25), size=12)
plot.annotate('After Decay', xy = (2.5+a, 1.25), size=12) 

plot.draw()
plot.show()