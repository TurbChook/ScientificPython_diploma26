import numpy as np
import matplotlib.pyplot as plt
class gof:
    def __init__(self,data):
        self.field = np.genfromtxt(data).transpose()
    def loop(self,N):
        field = self.field
        n,m = field.shape
        new_field = np.zeros((n+2,m+2))
        new_field[1:n+1,1:m+1] = field.copy()
        for i in range(N):
            new_field[0, 1:m+1]   = new_field[n, 1:m+1]     
            new_field[n+1, 1:m+1] = new_field[1, 1:m+1]     
            new_field[1:n+1, 0]   = new_field[1:n+1, m]     
            new_field[1:n+1, m+1] = new_field[1:n+1, 1]     
            new_field[0, 0]       = new_field[n, m]
            new_field[0, m+1]     = new_field[n, 1]
            new_field[n+1, 0]     = new_field[1, m]
            new_field[n+1, m+1]   = new_field[1, 1]
            temporal = new_field.copy()
            for i in range(1,n+1):
                for j in range(1,m+1):
                    individual_area = new_field[i-1:i+2,j-1:j+2]
                    temporal[i,j] = isalive(individual_area)
            new_field = np.zeros((n+2,m+2))
            new_field[1:n+1,1:m+1] = temporal[1:n+1,1:m+1]
            plt.imshow(new_field[1:n+1,1:m+1])
            plt.pause(0.1)
        plt.show()
def isalive(matrix):
    #the matrix will be a square matrix 3x3
    n,m = matrix.shape
    counter = 0
    for i in range(n):
        for j in range(m):
            if i == 1 and j == 1:
                pass
            elif matrix[i][j] == 1:
                counter += 1
    if matrix[1,1] == 1:
        if counter == 2 or counter == 3:
            return 1
        else:
            return 0
    else:
        if counter == 3:
            return 1
        else:
            return 0
def main():
    gof_test = gof("data/ships.txt")
    N = 70
    gof_test.loop(N)
if __name__ == "__main__":
    main()
    #test()
    #test1()