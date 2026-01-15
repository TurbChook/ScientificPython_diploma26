from module import MyMatrix
import numpy as np



def main():
    N=4
    matrix1=MyMatrix(N) #creates a square matrix
    matrix2=MyMatrix(N)
    print(matrix1.inverse())
    print(matrix1.determinant())
    print(matrix1.eigenvalues())
    print(matrix1+matrix2)
    print(matrix1*matrix2)



if __name__ == "__main__":
    main()