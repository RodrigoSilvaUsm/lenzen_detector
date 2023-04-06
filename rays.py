import math
import numpy as np
from math import sin, cos, atan


def rays(R,L,N,M,I,J,top):
    """
    Computes all the distances from the IJ plane to the surface cylinder in NM directions.
    Testing a change in vscode for git.
    """
    dphi = 2 * math.pi / N
    dtheta = math.pi / (M-1)
    dx = 2 * R / (I+2) # the plus 2 needs to be checked
    dz = L / (J+2)
    distances = np.zeros((I,J,N,M))
    for i in range(I):
        px = i * dx + dx
        for j in range(J):
            pz = j * dz + dz 
            for n in range(N):
                Dx = (R**2 - ((px-R)*sin(n*dphi))**2)**0.5 - ( px - R ) * cos( n * dphi )
                for m in range(M):
                    theta1 = atan( Dx / ( L - pz ) ) 
                    theta2 = math.pi - atan( Dx / pz )
                    if top:
                        if m * dtheta <= theta1:
                            distances[i,j,n,m] = ( L - pz ) / cos( m * dtheta )
                        elif m*dtheta>theta1 and m*dtheta<theta2:
                            distances[i,j,n,m] = Dx / sin( m * dtheta )
                        elif m*dtheta>=theta2:
                            distances[i,j,n,m] = math.inf #pz / cos( pi - m * dtheta )
                    else:
                        if m * dtheta <= theta1:
                            distances[i,j,n,m] = math.inf
                        elif m*dtheta>theta1 and m*dtheta<theta2:
                            distances[i,j,n,m] = Dx / sin( m * dtheta )
                        elif m*dtheta>=theta2:
                            distances[i,j,n,m] = math.inf                     
    return distances
    

#print(rays((95.25/2) * 1e-3, 50e-3, 6, 6, 4, 4))
if __name__ == "__main__":
    rays()
