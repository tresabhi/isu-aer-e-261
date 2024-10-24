import math
import sys
from matplotlib import pyplot as plt
import numpy as np

# I am honestly unsure how many comments are expected from me. Though
# I don't see any comments other than the units necessary, I will try my best
# to explain everything no matter how trivial.

# given constants
C_D_0 = 0.017
K = 0.056
C_L_max = 1.37
S_wing = 22.9  # m^2
eta_pr = 0.9
W_0 = 16481  # N
P = 18e4  # W

# https://www.digitaldutch.com/atmoscalc/graphs.htm
# It would be childish to hardcode this in a function so I am making this
# data-driven.
# (m, K)[]
T_table = [
    (0.0, 288.15),
    (11e3, 216.65),
    (20e3, 216.65),
    (32e3, 228.65),
    (47e3, 270.65),
    (51e3, 270.65),
    (72e3, 212.65),
    (85e3, 186.95),
    (86e3, 186.95),
]


# Accepts altitude and returns Earthly temperature.
# m -> K
def temperature(h: int):
    # iterate through the table...
    for index in range(len(T_table) - 1):
        # ...to find an appropriate entry
        if h >= T_table[index][0] and h < T_table[index + 1][0]:
            # interpolate
            return T_table[index][1] + (
                (T_table[index + 1][1] - T_table[index][1])
                * (h - T_table[index][0])
                / (T_table[index + 1][0] - T_table[index][0])
            )

    # if the for loop never returns, the altitude is outside of our domain
    raise ValueError(f"Invalid altitude: {h}")


# https://en.wikipedia.org/wiki/Atmospheric_pressure
p_0 = 101325  # Pa
M = 0.0289644  # kg/mol
g = 9.80665  # m/s^2
R = 8.3144598  # J/(mol*K)
L = 0.00976  # K/m
T_0 = temperature(0)


# m -> Pa
def pressure(h: int):
    # applying the barometric formula
    return p_0 * (1 - (L * h) / T_0) ** ((g * M) / (R * L))


# m -> kg/m^3
def density(h: int):
    # applying the ideal gas law
    return (pressure(h) * M) / (R * temperature(h))


# m -> m/s
def v_stall(h: int):
    # applying the v_stall formula
    return math.sqrt((2 * W_0) / (density(h) * S_wing * C_L_max))


h_0 = 0  # m
h_1 = 25e3  # m
delta_h = 1  # m

# range of heights
x = np.arange(h_0, h_1, delta_h)
y = []

# turning this file into a mono-file CLI
if len(sys.argv) < 2:
    # gotta pass an argument or get wrecked lol
    raise ValueError(
        "No instruction provided on what to plot.\nHint: py index.py --plot=<temperature|pressure|density>"
    )

# catching all plot types
if sys.argv[1] == "--plot=temperature":
    y = [temperature(h) for h in x]
    plt.xlabel("Temperature (K)")
    plt.title("Temperature vs. Height")
elif sys.argv[1] == "--plot=pressure":
    y = [pressure(h) for h in x]
    plt.xlabel("Pressure (Pa)")
    plt.title("Pressure vs. Height")
elif sys.argv[1] == "--plot=density":
    y = [density(h) for h in x]
    plt.xlabel("Density (kg/m^3)")
    plt.title("Density vs. Height")
elif sys.argv[1] == "--plot=v_stall":
    y = [v_stall(h) for h in x]
    plt.xlabel("Velocity (m/s)")
    plt.title("Stall Velocity vs. Height")
# catching invalid plot types
else:
    raise ValueError(
        "Illegal plot argument. Run the command without arguments to see all plots types."
    )

# time for matplotlib to shine
plt.ylabel("Height (m)")
plt.plot(y, x)
plt.grid()
plt.show()
