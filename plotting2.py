import numpy as np
import matplotlib.pyplot as plt
import efficiency as effi


def plotting2(energy, R, L, I, J):
    dx = 2 * R / (I+2)
    dz = L / (J+2)
    equis = np.linspace(dx, 2*R-dx, I)    
    zeta = np.linspace(dz, L-dz, J)
    EQUIS, ZETA = np.meshgrid(equis, zeta, indexing='ij')
    plt.figure(figsize =(14, 9))
    #contours = plt.contour(EQUIS, ZETA, effiNormal[1], 20 ,cmap='viridis')
    #effiNormal = effi.efficiency(R,L,N,M,I,J,top=False, Range=40e-3)
    contours = plt.contour(EQUIS, ZETA, energy*1e-6, 12 ,cmap='viridis')
    plt.clabel(contours, inline=True, fontsize=12)
    plt.colorbar()
    plt.show()
    #plt.contour(EQUIS, ZETA, effi)  
    #plt.contour(energy)  


if __name__ == "__main__":
    plotting2()