import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def multiply(
        a: float,
        b: float
) -> float:
    """
    Use this function when the user wants to multiply two number, or for example asks for a times b, a * b or a x b.. etc.
    
    Args:
        a `float`: first number
        b `float`: second number

    Returns:
        `float` the result of the multiplication of a times b.
    
    """

    return a * b

def save_result(a: float, b:float, result: float) -> str:
    """
    Use this function when the user wants to save the result of a multiplication in file.    
    """
    with open("results/result.txt", "w") as file:
        file.write(f"the result of {a} * {b} = {result}")

    return f"saved {result} under results/result.txt"


def _solve(
    projectile_mass_kg: float,
    projectile_radius_m: float,
    initial_velocity_m_s: float,
    initial_angle_deg: float,
    air_density_kg_m3: float = 1.225,
    initial_position_m: list[float] = [0.0, 0.0],
    gravity_acceleration_m_s2: float = 9.81,
    drag_coefficient: float = 0.47,
) -> dict:
    """Solver for the simulation of a spherical projectile with quadratic air drag in two dimensions.

    Args:
        projectile_mass_kg: Mass of the projectile in kilograms.
        projectile_radius_m: Radius of the spherical projectile in meters.
            Used to compute the cross-sectional area.

        initial_velocity_m_s: Launch speed in meters per second.
        initial_angle_deg: Launch angle above the horizontal in degrees,
            between 0 and 90.

        air_density_kg_m3: Air density in kg/m^3. Default is sea level air.
        initial_position_m: Launch position [x, y] in meters. Use [0, 0]
            unless the question states otherwise.

        gravity_acceleration_m_s2: Gravitational acceleration in m/s^2.
            Default is Earth.

        drag_coefficient: Dimensionless drag coefficient. Default is 0.47,
            which is typical for a sphere.

    Returns:
        A dictionary with:
        range_m (horizontal position at landing in meters),
        peak_height_m (maximum height in meters)
        flight_time_s (time until landing in seconds).
    """
    theta = np.radians(initial_angle_deg)
    rho = air_density_kg_m3
    C_d = drag_coefficient
    r = projectile_radius_m
    A = np.pi * r**2
    m = projectile_mass_kg
    g = gravity_acceleration_m_s2
    v0 = initial_velocity_m_s


    initial_position = np.array(initial_position_m)
    initial_velocity = np.array([v0 * np.cos(theta), v0 * np.sin(theta)])
    initial_conditions = np.array([initial_position, initial_velocity]).ravel()

    def system_odes(t, s):
        r_x, r_y, v_x, v_y = s

        dv_x_dt =  -1/2 * rho * C_d * A / m * np.sqrt(v_x**2 + v_y**2) * v_x
        dv_y_dt =  -1/2 * rho * C_d * A / m * np.sqrt(v_x**2 + v_y**2) * v_y - g

        return np.array([v_x, v_y, dv_x_dt, dv_y_dt])

    def hit_ground(t, s):
        return s[1] # r_y crosses zero at landing

    hit_ground.terminal = True
    hit_ground.direction = -1    # only downward crossings, so the start at r_y = 0 is ignored

    def apex(t, s):
        return s[3] # v_y, crosses zero at the highest point

    apex.direction = -1          # not terminal, it only records
    
    simulation_time = 100

    # Solve the ODE system using solve_ivp
    solution = solve_ivp(
        fun=system_odes,        # Function defining the system of ODEs
        t_span=(0, simulation_time),  # Time range for the simulation
        y0=initial_conditions,  # Initial conditions (positions and velocities)
        events=[apex, hit_ground],
        dense_output=True,
        rtol=1e-6,
        atol=1e-6
    )

    return solution


def projectile_simulation(
    projectile_mass_kg: float,
    projectile_radius_m: float,
    initial_velocity_m_s: float,
    initial_angle_deg: float,
    air_density_kg_m3: float = 1.225,
    initial_position_m: list[float] = [0.0, 0.0],
    gravity_acceleration_m_s2: float = 9.81,
    drag_coefficient: float = 0.47,
) -> dict:
    """Simulate a spherical projectile with quadratic air drag in two dimensions.

    Use this tool when a question asks how far, how high or how long a thrown
    or launched object travels through air. Gravity acts downward and
    drag opposes the velocity with a magnitude proportional to the speed
    squared. The simulation ends when the projectile returns to height zero.

    Args:
        projectile_mass_kg: Mass of the projectile in kilograms.
        projectile_radius_m: Radius of the spherical projectile in meters.
            Used to compute the cross-sectional area.

        initial_velocity_m_s: Launch speed in meters per second.
        initial_angle_deg: Launch angle above the horizontal in degrees,
            between 0 and 90.

        air_density_kg_m3: Air density in kg/m^3. Default is sea level air.
        initial_position_m: Launch position [x, y] in meters. Use [0, 0]
            unless the question states otherwise.

        gravity_acceleration_m_s2: Gravitational acceleration in m/s^2.
            Default is Earth.

        drag_coefficient: Dimensionless drag coefficient. Default is 0.47,
            which is typical for a sphere.

    Returns:
        A dictionary with:
        range_m (horizontal position at landing in meters),
        peak_height_m (maximum height in meters)
        flight_time_s (time until landing in seconds).
    """
    solution = _solve(projectile_mass_kg, projectile_radius_m, initial_velocity_m_s,
                      initial_angle_deg, air_density_kg_m3, initial_position_m,
                      gravity_acceleration_m_s2, drag_coefficient)
    
    t_apex, t_land = solution.t_events[0][0], solution.t_events[1][0]
    r_apex, r_land = solution.y_events[0][0][1], solution.y_events[1][0][0]

    return {
        "range_m":r_land,
        "peak_height_m":r_apex,
        "flight_time_s": t_land
    }

def plot_trajectories(
    vary: str, # initial_velocity_m_s
    values: list[float], # [10, 20, 30, 50]
    initial_velocity_m_s: float = 20.0,
    initial_angle_deg: float = 45.0,
    projectile_mass_kg: float = 0.057,
    projectile_radius_m: float = 0.033,
) -> dict:
    """Vary one parameter of a thrown ball while keeping the others fixed, and plot the trajectories.

    Use this tool when the user asks how changing a parameter affects the flight.
    The defaults describe a tennis ball thrown at 20 m/s and 45 degrees.

    Args:
        vary: The parameter to vary. One of initial_velocity_m_s,
            initial_angle_deg, projectile_mass_kg, projectile_radius_m.
        values: The values to try, for example [15, 30, 45, 60].
        initial_velocity_m_s: Launch speed in meters per second.
        initial_angle_deg: Launch angle in degrees.
        projectile_mass_kg: Mass of the ball in kilograms.
        projectile_radius_m: Radius of the ball in meters.

    Returns:
        The path of the saved plot and the range in meters for each value.
    """

    params = {
        "initial_velocity_m_s": initial_velocity_m_s,
        "initial_angle_deg": initial_angle_deg,
        "projectile_mass_kg": projectile_mass_kg,
        "projectile_radius_m": projectile_radius_m
    }

    plt.figure(figsize=(12, 5))

    ranges = {}
    for value in values:
        params[vary] = value # 10
        solution = _solve(**params)

        t = np.linspace(0, solution.t_events[1][0], 101)
        x, y = solution.sol(t)[:2]

        plt.plot(x, y, label=f"{vary} = {value}")
        ranges[value] = x[-1]

    plt.title(f"projectile simulation - influence of {vary}")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.grid()
    plt.legend()
    plt.savefig(f"parameter_study_{vary}.png")
    plt.close()

    return {"image": f"parameter_study_{vary}.png", "range_m": ranges}
