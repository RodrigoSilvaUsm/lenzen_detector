import csv 


def weights_csv(weights, filename="weights_table.csv"):
    """
    Write the resulting weights in a csv file.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["i", "j", "n", "m", "weigth"])
        for i in range(len(weights[0,:,:,:])):
            for j in range(len(weights[0,:,0,0])):
                for n in range(len(weights[0,0,:,0])):
                    for m in range(len(weights[0,0,0,:])):
                        writer.writerow([i,j,n,m,weights[i,j,n,m]])
            
            
if __name__ == "__main__":
    weights_csv()
