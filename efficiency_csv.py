import csv 


def efficiency_csv(efficiency, effi_mean, filename="efficiencies_table.csv"):
    """
    Write the resulting efficiencies in a csv file
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["i [I="+str(len(efficiency[:,0]))+"]", "j [J="+str(len(efficiency[0,:]))+"]", "Efficiency [EffiMean = "+ str(int(10000*effi_mean)/100) + " %]"])
        for i in range(len(efficiency[:,0])):
            for j in range(len(efficiency[0,:])):
                writer.writerow([i, j, efficiency[i][j]])


if __name__ == "__main__":
    efficiency_csv()
