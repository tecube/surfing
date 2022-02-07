import numpy as np

L = 2.0
T = 10.0
Nx = 51
Nstrings = 100
Nt = 1000

xs, dx = np.linspace(0, L, Nx, retstep=True)
ts, dt = np.linspace(0, T, Nt, retstep=True)

u = np.zeros([Nstrings, Nx])

for i, t in enumerate(ts):
    print(i)
    for s in range(Nstrings):
        u[s,:] = np.sin(xs*s*0.1 + t)

    np.savetxt(f'wave_data/u_{i:03}.dat', u)

#u = np.zeros([Nt, Nstrings, Nx])

#for i, t in enumerate(ts):
    #print(i)
    #for s in range(Nstrings):
        #u[i,s,:] = np.cos(i) * np.sin(xs*s)

#with open('wave_data/all.dat', 'a') as f:
    #for t in ts:
        #np.savetxt(f, u, header=f'{t}')