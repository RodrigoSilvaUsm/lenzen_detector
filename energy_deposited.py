import csv
import numpy as np
from joblib import Parallel, delayed
import energy_key as ekey


def energy_deposited(effi_values, weights, ray_values, data2dict, range_particle, max_step):
    """
    Creates a CSV file with the deposited energies on a cylindrical Radon detector.
    """
    #energy_table = np.genfromtxt('energy_table.csv', delimiter=',', skip_header=1)
    #effi_table = np.genfromtxt('efficiencies_table.csv', delimiter=',', skip_header=1)
    #weight_table = np.genfromtxt('weights_table.csv', delimiter=',', skip_header=1)
    #rays_table = np.genfromtxt('rays_table.csv', delimiter=',', skip_header=1)
    I = weights.shape[0]
    J = weights.shape[1]
    N = weights.shape[2]
    M = weights.shape[3]
  
    energy_distribution = np.zeros((I,J))
    energy_mean = 0
    aux = 0
    for i in range(I):
        for j in range(J):
            for n in range(N):
                #energy_distribution[i,j] = Parallel(n_jobs=2)(delayed(+)(weights[i,j,n,m] * data2dict[ekey.energy_key(ray_values[i,j,n,m])]) for m in range(M))
                for m in range(M):
                    distance_key = ekey.energy_key(ray_values[i,j,n,m], range_particle, max_step)
                    energy_key = data2dict[distance_key]
                    energy_distribution[i,j] += weights[i,j,n,m] * energy_key
            if effi_values[i,j] != 0:
                energy_distribution[i,j] /= effi_values[i,j]
                energy_mean += energy_distribution[i,j]*i
                aux += 1
    return energy_distribution, energy_mean*2/(I**2*J)

if __name__=="__main__":    
    energy_deposited(effi_mean, effi_values, weights, ray_values, data2dict)
