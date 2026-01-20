import numpy as np
import matplotlib.pyplot as plt

class jacobi:
    def __init__(self):
        self.grid = ic()
        
    #def plot(self):
    def plot(self):
        field = self.grid.copy()
        for _ in range(50):
            new_field = field.copy()
            for i in range(1,10):
                for j in range(1,10):
                    new_field[i,j]=0.25*(field[i,j-1]+field[i,j+1]+
                                         field[i+1,j]+field[i-1,j])
            plt.clf()
            plt.imshow(new_field)
            plt.pause(0.5)
            field = new_field.copy()
        plt.show()
    
def ic():
    init_array = np.zeros((11,11))
    init_array[:,0] = [x*10 for x in range(11)]
    init_array[10,:] = [100 - x*10 for x in range(11)]
    init_array[1:10,1:10] = 0.5*np.ones((9,9))
    return init_array
def main():
    grid = jacobi()
    grid.plot()


if __name__ == "__main__":
    main()