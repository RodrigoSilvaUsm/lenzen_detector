import math
import csv 


def energy_csv(distance, energy, filename="energy_table.csv"):
    """
    Write the resulting energies in a csv file
    Please consider the energies are given by betheblock.absorption() function.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["distance [m]", "Energy [eV]"])
        for i in range(len(distance)):
            writer.writerow([distance[i], energy[i]])
        #writer.writerow([math.inf, 0])    
            
if __name__ == "__main__":
    energy_csv()
