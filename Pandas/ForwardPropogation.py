
import numpy as np


def dense_layer(a_in, W, b):
    # Perform the dot product between inputs and weights
    units = W.shape[0]
    a_out = np.zeros((units,))
    for i in range(units):
       z = np.dot(a_in, W[i]) + b[i]
       a_out[i] = g(z)

    return a_out

def g(a_in):
    # Apply the sigmoid activation function
    return 1 / (1 + np.exp(-a_in))  


W_1 = np.array([[0.2, 0.8, -0.5], [0.5, -0.91, 0.26], [-1.5, 0.3, 0.4]])
b_1 = np.array([0.5, -0.91, 0.26])
W_2 = np.array([[0.1, -0.2, 0.3], [0.4, 0.5, -0.6], [-0.7, 0.8, 0.9]])
b_2 = np.array([0.1, -0.2, 0.3])    
W_3 = np.array([[0.2, -0.3, 0.4], [0.5, 0.6, -0.7], [-0.8, 0.9, 1.0]])
b_3 = np.array([0.2, -0.3, 0.4])
a_in = np.array([1.0, 0.5, -1.5])  # Input to the first layer

def sequential():
    # Initialize the input layer
    a1 = dense_layer(a_in, W_1, b_1)
    a2 = dense_layer(a1, W_2, b_2)
    a_out = dense_layer(a2, W_3, b_3)  # Final output after all layers
    print("Output of the sequential model:", a_out)
    return a_out


sequential()