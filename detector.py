import sys
import numpy as np
import matplotlib.pyplot as plt
import betheblock as bb

max_step= float(sys.argv[1]) #0.5e-3
distance = float(sys.argv[2]) #40e-3
points = int(distance/max_step) 
energy, position = np.zeros(points), np.zeros(points)
position, energy = bb.absorption(distance)

plt.plot(position, energy)
plt.show()
