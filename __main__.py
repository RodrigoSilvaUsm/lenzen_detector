<<<<<<< HEAD
import numpy as np
from collections import OrderedDict
import time
import matplotlib.pyplot as plt
import math

import betheblock as bb
import energy_csv as ecsv
import efficiency as effi
import efficiency_csv as efficsv
import weigths_csv as wcsv
import energy_deposited as ened
import rays_csv as rcsv
import plotting as plt1
import plotting2 as plt2
import rays


#measuring computing time
t0 = time.time()
#parameters
R = (55/2)*1e-3 #radius of the detector
L = 72e-3 #length of the detector
N = 180 #points of phi angle 
M = 90 #points of theta angle
I = 20 #initial points in x axis
J = 20 #initial points in z axis
top = True #there is detection at the top when True, our detector top=False, Lenzen's detector top=True
range_particle = 70e-3 #mm
E0 = 7.7e6
max_step = 1e-4
#generating variables
distance, energy = bb.absorption(range_particle, E0, max_step)#generates the table of energy for a given atom, such as Rn222, Po218, Po214
#print(distance.shape, energy.shape)
#print(distance, energy)

distance = np.append(distance, [math.inf]) #This two lines fo code close the energy list with an inf distance and a zero energy
energy = np.append(energy, [0])             #This two lines fo code close the energy list with an inf distance and a zero energy

#print(distance.shape, energy.shape)
#print(distance, energy)
#energy_table = np.array([[distance,],[energy,]])
#print(energy_table)
ecsv.energy_csv(distance, energy) #save energy table as a csv file, IMPROVING: still only reading from file, it should have both, as a variable and as a file, still working the variable alternative
energy_table = np.genfromtxt('energy_table.csv', delimiter=',', skip_header=1) #read energy table from a csv file

#print("shape from genfromtext: ", energy_table.shape)
#energy_table = np.column_stack((distance,energy))
#print("shape from concatenate two cols: ", distance.shape)

#print(energy_table)
#print("table shape: ", energy_table.shape)
data2dict = OrderedDict(energy_table) #transform the energy table to an ordered dictionary so can be access later 
ray_values = rays.rays(R,L,N,M,I,J, top)
effi_mean, effi_normal, effi_values, weights = effi.efficiency(N,M,I,J, ray_values, range_particle)
energy_distribution, energy_mean = ened.energy_deposited(effi_values, weights, ray_values, data2dict, range_particle, max_step)

#efficsv.efficiency_csv(effi_values, effi_mean)
#wcsv.weights_csv(weights)
#rcsv.rays_csv(ray_values)
#efficsv.efficiency_csv(effi_values, effi_mean)

print("elapsed time", int(10*(time.time()-t0))/600, "minutes")
plt1.plotting(effi_normal, R, L, I, J)
plt2.plotting2(energy_distribution, R, L, I, J)
#print(data2dict)
print("efficiency mean: ", int(10000*effi_mean)/100,"%, energy mean: ", int(1000 * energy_mean*1e-6)/1000, "MeV.\n")

#some_effi = np.array([62.75,38.99,23.47,16.32,11.93])
#some_energy = np.array([2.509,1.993,1.518,1.180,0.943])
#along_x = np.array([57.15,66.675,76.2,85.725,95.25,104.775,114.3,123.825,133.35])
#along_y = np.array([555.5555556,408.1632653,312.5,246.9135802,200,165.2892562,138.8888889,118.3431953,102.0408163])
#plt.plot(along_x,along_y, '.')
=======
import numpy as np
from collections import OrderedDict
import time
import matplotlib.pyplot as plt
import math

import betheblock as bb
import energy_csv as ecsv
import efficiency as effi
import efficiency_csv as efficsv
import weigths_csv as wcsv
import energy_deposited as ened
import rays_csv as rcsv
import plotting as plt1
import plotting2 as plt2
import rays


#measuring computing time
t0 = time.time()
#parameters
R = (55/2)*1e-3 #radius of the detector
L = 72e-3 #length of the detector
N = 180 #points of phi angle 
M = 90 #points of theta angle
I = 20 #initial points in x axis
J = 20 #initial points in z axis
top = True #there is detection at the top when True, our detector top=False, Lenzen's detector top=True
range_particle = 70e-3 #mm
E0 = 7.7e6
max_step = 1e-4
#generating variables
distance, energy = bb.absorption(range_particle, E0, max_step)#generates the table of energy for a given atom, such as Rn222, Po218, Po214
#print(distance.shape, energy.shape)
#print(distance, energy)

distance = np.append(distance, [math.inf]) #This two lines fo code close the energy list with an inf distance and a zero energy
energy = np.append(energy, [0])             #This two lines fo code close the energy list with an inf distance and a zero energy

#print(distance.shape, energy.shape)
#print(distance, energy)
#energy_table = np.array([[distance,],[energy,]])
#print(energy_table)
ecsv.energy_csv(distance, energy) #save energy table as a csv file, IMPROVING: still only reading from file, it should have both, as a variable and as a file, still working the variable alternative
energy_table = np.genfromtxt('energy_table.csv', delimiter=',', skip_header=1) #read energy table from a csv file

#print("shape from genfromtext: ", energy_table.shape)
#energy_table = np.column_stack((distance,energy))
#print("shape from concatenate two cols: ", distance.shape)

#print(energy_table)
#print("table shape: ", energy_table.shape)
data2dict = OrderedDict(energy_table) #transform the energy table to an ordered dictionary so can be access later 
ray_values = rays.rays(R,L,N,M,I,J, top)
effi_mean, effi_normal, effi_values, weights = effi.efficiency(N,M,I,J, ray_values, range_particle)
energy_distribution, energy_mean = ened.energy_deposited(effi_values, weights, ray_values, data2dict, range_particle, max_step)

#efficsv.efficiency_csv(effi_values, effi_mean)
#wcsv.weights_csv(weights)
#rcsv.rays_csv(ray_values)
#efficsv.efficiency_csv(effi_values, effi_mean)

print("elapsed time", int(10*(time.time()-t0))/600, "minutes")
plt1.plotting(effi_normal, R, L, I, J)
plt2.plotting2(energy_distribution, R, L, I, J)
#print(data2dict)
print("efficiency mean: ", int(10000*effi_mean)/100,"%, energy mean: ", int(1000 * energy_mean*1e-6)/1000, "MeV.\n")

#some_effi = np.array([62.75,38.99,23.47,16.32,11.93])
#some_energy = np.array([2.509,1.993,1.518,1.180,0.943])
#along_x = np.array([57.15,66.675,76.2,85.725,95.25,104.775,114.3,123.825,133.35])
#along_y = np.array([555.5555556,408.1632653,312.5,246.9135802,200,165.2892562,138.8888889,118.3431953,102.0408163])
#plt.plot(along_x,along_y, '.')
>>>>>>> 1c43e0cb3d2d7e6cd5a77040c56f2d9cf614b318
#plt.show()