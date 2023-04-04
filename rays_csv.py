import csv 


def rays_csv(rays_values, filename="rays_table.csv"):
    """
    Write the resulting weights in a csv file
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["i", "j", "n", "m", "ray[m]"])
        for i in range(len(rays_values[0,:,:,:])):
            for j in range(len(rays_values[0,:,0,0])):
                for n in range(len(rays_values[0,0,:,0])):
                    for m in range(len(rays_values[0,0,0,:])):
                        writer.writerow([i,j,n,m,rays_values[i,j,n,m]])
            
            
if __name__ == "__main__":
    rays_csv()
