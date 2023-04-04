import scipy.integrate as scint
import numpy as np
import math
import absfuncs as afs
import constants as cts


#properties of the incident particle (ALPHA PARTICLE)
 #[kg], mass of alpha particle
 
#E0 = 5.3 * 1e6
#range_alpha = 40 * 1e-3 #max distance traveled by the particle, app 40mm for alpha particles with 10MeV of E0
#aEmean = 2.5e6

#absorption
def absorption(distance, E0, max_step, x0=0):
    """
    Returns two numpy arrays, the distance traveled by the particle and its energy in every point of its displacement. 
    Recieves the initial energy of the particle E0 in eV, the maximum step per computing in m and
    the initial position x0 of the particle in meters. Returns the position and the energy of the particle.
    """
    #max_step = 10**(-num_decimals)
    points = int(distance/max_step) + 1  
    beta0 = (1-(1+E0/(cts.M_ALPHA * cts.C**2/cts.Q_E))**(-2))**0.5
    solution = scint.RK45(afs.dbeta, x0, [beta0], distance, max_step)
    energy, position = np.zeros(points), np.zeros(points)
    energy[0]=E0
    position[0]=x0
    #decimals = str(max_step)[::-1].find('.') # returns the quantity of decimals of the step, this values is used to round the distance traveled, to avoid numbers like 0.010000001, which is meant to be 0.01
    #num_decimals = decimals.count_decimals(max_step)
    #num_decimals = 4
    #max_step = 10**(-num_decimals)
    #print("decimals in BB: ", num_decimals)
    for i in range(1,points):
        solution.step()
        #if solution.status == 'finished':
         #   break
        energy[i] = (afs.gamma(solution.y[0])-1) * cts.M_ALPHA * cts.C**2/cts.Q_E
        position[i] = round(position[i-1] + max_step, -int(math.log(max_step, 10)) + 1 )# float(('%.5f' % round(position[i-1] + max_step, 5)))
    return position, energy  #solution.y[0] returns the final value of Energy E 


if __name__ == "__main__":
    absorption()
