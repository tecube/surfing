import numpy as np

L = 2.0
T = 10.0
Nx = 51
Nstrings = 100
Nt = 1000

xs, dx = np.linspace(0, L, Nx, retstep=True)
ts, dt = np.linspace(0, T, Nt, retstep=True)

u = np.zeros([Nt, Nstrings, Nx])