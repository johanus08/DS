import numpy as np
import pandas as pd
x = np.array([[12,3,21],[2,43,5],[5,32,53]])
y = np.array([[11,4,6],[21,7,9],[4,8,43]])
a = np.multiply(x,y)
b = np.add(x,y)
c = np.transpose(x)
d = np.transpose(y)
print("Multiplication of two matrices")
print(a)
print("Addition of two matrices")
print(b)
print("Transpose of two matrices")
print(c)
print(d)

