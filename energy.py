import energy_key as egr

def energy(distance, w, effi, I ,J, N, M):
    energyMean = 0          
    for i in range(I):
        for j in range(J):
            for n in range(N):
                for m in range(M):
                    energy[i,j] += w[i,j,n,m] * egr.energy_generator(distance[i,j,n,m])     
                    #if effi[i,j] != 0:
            if effi[i,j] != 0:
                energy[i,j] /= effi[i,j]
                energyMean += i * energy[i,j]            
    energyMean *= 2/(I**2*J)
    return energyMean, energy


if __name__ == "__main__":
    energy()
