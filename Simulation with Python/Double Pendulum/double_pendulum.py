# -------  Importing Libraries ------- #

import numpy as np
from scipy.integrate import odeint
import sympy as sm

# -------  Defining Symbols & Variables ------- #

t = sm.symbols('t')
m_1, m_2, g = sm.symbols('m_1 m_2 g', positive=True)

the1, the2 = sm.symbols(r'\theta_1, \theta_2', cls=sm.Function) # sm.Function states that the position is a function

the1 = the1(t) # Specifying the variable
the2 = the2(t)

x1 = sm.sin(the1)
y1 = -sm.cos(the1)

x2 = x1 + sm.sin(the2)
y2 = y1 + -sm.cos(the2)


# -------  Defining Derivatives ------- #

the1_d = sm.diff(the1, t) # Angular Velocity
the1_dd = sm.diff(the1_d, t) # Angular Acceleration

x1_d = sm.diff(x1, t)
y1_d = sm.diff(y1, t)

the2_d = sm.diff(the2, t) # Angular Velocity
the2_dd = sm.diff(the2_d, t) # Angular Acceleration

x2_d = sm.diff(x2, t)
y2_d = sm.diff(y2, t)


# -------  Defining Energies & Lagrange ------- #

T_1 = 1/2 * m_1 * ((x1_d)**2+(y1_d)**2)
T_2 = 1/2 * m_2 * ((x2_d)**2+(y2_d)**2)
V_1 = m_1 * g * y1
V_2 = m_2 * g * y2
L = T_1 + T_2 - (V_2 + V_1)



# -------  Defining Lagrange's Equations ------- #

LE1 = sm.diff(sm.diff(L, the1_d), t) - sm.diff(L, the1) # use .simplyfy() if necessary
LE2 = sm.diff(sm.diff(L, the2_d), t) - sm.diff(L, the2) # use .simplyfy() if necessary

LE1 = LE1.simplify()
LE2 = LE2.simplify()


# -------  Solving the System of Equations & Lambdifying ------- #

solutions = sm.solve([LE1, LE2], the1_dd, the2_dd)
LEF1 = sm.lambdify((the1, the2, the1_d, the2_d, t, m_1, m_2, g), solutions[the1_dd])
LEF2 = sm.lambdify((the1, the2, the1_d, the2_d, t, m_1, m_2, g), solutions[the2_dd])



# -------  Solving the System Numerically ------- #

# Initial conditions & Constants
initial_conditions = [1.0, 10.0, -1.0, 3.0]  # Angle_1, Velocity_1, Angle_2, Velocity_2, 
m1_val = 2
m2_val = 2
g_val = 9.81

# Function representing the system of first-order ODEs
def system_of_odes(y, t, m_1, m_2, g):
    the1, the1_d, the2, the2_d = y

    the1_dd = LEF1(the1, the2, the1_d, the2_d, t, m_1, m_2, g)
    the2_dd = LEF2(the1, the2, the1_d, the2_d, t, m_1, m_2, g)

    return [the1_d, the1_dd, the2_d, the2_dd]

# Time points for numerical solution
time_points = np.linspace(0, 40, 1001)

# Solve the system of ODEs
solution = odeint(system_of_odes, initial_conditions, time_points, args=(m1_val, m2_val, g_val))

# Extract position and velocity from the solution
the1_sol = solution[:, 0]
the1_d_sol = solution[:, 1]

the2_sol = solution[:, 2]
the2_d_sol = solution[:, 3]

x1_pendulum = np.sin(the1_sol)
y1_pendulum = -np.cos(the1_sol)

x2_pendulum = x1_pendulum + np.sin(the2_sol)
y2_pendulum = y1_pendulum + -np.cos(the2_sol)




# -------  Animating the solutions ------- #

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 1)
plt.grid()


def update(frame):
    
    pendulum1.set_data([0, x1_pendulum[frame]], [0, y1_pendulum[frame]])
    mass1.set_data([x1_pendulum[frame]], [y1_pendulum[frame]])

    pendulum2.set_data([x1_pendulum[frame], x2_pendulum[frame]], [y1_pendulum[frame], y2_pendulum[frame]])
    mass2.set_data([x2_pendulum[frame]], [y2_pendulum[frame]])

    return pendulum1, mass1, pendulum2, mass2

pendulum1, = ax.plot([0, x1_pendulum[0]], [0, y1_pendulum[0]], lw=2)
mass1, = ax.plot([x1_pendulum[0]], [y1_pendulum[0]], 'o', markersize=4*int(m1_val)+1, color='red')

pendulum2, = ax.plot([x1_pendulum[0], x2_pendulum[0]], [y1_pendulum[0], y2_pendulum[0]], lw=2)
mass2, = ax.plot([x2_pendulum[0]], [y2_pendulum[0]], 'o', markersize=4*int(m2_val)+1, color='red')

animation = FuncAnimation(fig, update, frames=len(time_points), interval=25, blit=True)

plt.show()