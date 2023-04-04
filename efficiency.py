import numpy as np
from math import pi
from numpy import sin
import rays
import time


def efficiency(N,M,I,J,ray_values, range_particle):
    """
    Computes the efficiency of a cylindrical Radon detector using Lenzen's proposal.
    """
    #distances = rays.rays(R,L,N,M,I,J)
    w = np.ones((I,J,N,M))
    effi = np.zeros((I,J))
    #Effi = np.zeros((I,J))
    effiNormal = np.zeros((I,J))
    dphi = 2 * pi / N
    dtheta = pi / (M-1)
    mm = np.linspace(0,M-1,M)
    w[:] = -2 * dphi * sin(dtheta / 2) * sin(mm*dtheta)

    for i in range(I):
        for j in range(J):
            #w[i,j,:,:] = -2 * dphi * sin(dtheta / 2) * sin(mm*dtheta)
            for n in range(N):  
                for m in range(M):   
                    if ray_values[i,j,n,m] <= range_particle: 
                    #w[i,j,n,m] = -2 * dphi * sin(dtheta / 2) * sin( m*dtheta ) 
                    #w[i,j,n,m] = -( cos(m*dtheta + dtheta/2) - cos(m*dtheta - dtheta/2)) * dphi
                    #Effi[i,j] += w[i,j,n,m]           
                    # and ( m * dtheta ) >= thetaCritic1( i * dx , j * dz ) and ( m * dtheta ) <= thetaCritic2( i * dx, j * dz):
                        effi[i,j] +=  w[i,j,n,m] 
                #print(w[i,j,n,:])
                #time.sleep(2)
                #mm=np.linspace(0,M-1,M)
                #w[i,j,n,:] = -2 * dphi * sin(dtheta / 2) * sin(mm*dtheta)
                
    # Normalizing efficiency and mean effi
    #w[:,:,:,:] = -2 * dphi * sin(dtheta / 2) * sin(mm*dtheta)
    Effi = np.ones((I,J)) * (-2*dphi*sin(dtheta/2)*N*sin((M+1)*dtheta/2)*sin(M*dtheta/2)/sin(dtheta/2))
    effiMean = 0
    aux = 0
    for i in range(I):
        for j in range(J):
            effiNormal[i,j] = effi[i,j] / Effi[i,j] 
            #effiNormal[i,j] = int(effiNormal[i,j]*100)/100
            effiMean += i * effiNormal[i,j]
            aux += 1
            


    return 2*effiMean/(I**2*J), effiNormal, effi, w#, distances
#effiMean *= 2/(I**2*J)
          
if __name__ == "__name__":
     efficiency(R,L,N,M,I,J,ray_values, range_particle=40e-3)