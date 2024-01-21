import numpy as np
import matplotlib.pyplot as plot


figure = plot.figure(figsize=(8, 4.125))

l = np.pi
x = np.linspace(-l, l, 500)
y = x #f(x)


a_0 = 1/l * np.trapz(y, x, dx = 1/100)

y_fourier = np.zeros(len(x)) + a_0/2

for n in range(1, 300):

    error = np.sqrt(   np.trapz( np.abs(np.add(y_fourier, -y))**2, x, dx = 1/100  )   )

    figure.clear()

    axis = figure.subplots()

    axis.plot(x, y_fourier, color='black', label='Fourier Approximation')
    axis.plot(x, y, '--',color='red', label='Periodic Function')    

    axis.set_title('Evaluation f(x) = x with fourier having: {} terms.\n Mean Squarred Error : {}'.format(n+1, error))
    axis.set_xlabel('x')
    axis.set_ylabel('f(x) - Using Fourier')
    plot.xlim(1.2*min(x), 1.2*max(x))
    plot.ylim(1.2*min(y), 1.2*max(y))
    plot.grid()
    plot.legend()
    plot.draw()
    plot.pause(0.05)

    

    a_n = 1/l * np.trapz(y*np.cos(np.pi*n*x/l), x, dx = 1/100)
    b_n = 1/l * np.trapz(y*np.sin(np.pi*n*x/l), x, dx = 1/100)

    fourier_term = a_n*np.cos(np.pi*n*x/l) + b_n*np.sin(np.pi*n*x/l)

    y_fourier = np.add(fourier_term, y_fourier)


plot.show()



