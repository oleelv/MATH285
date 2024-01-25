#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:30:39 2024

@author: ole
"""
import numpy as np
from utils.activation import activation as act_fcn

class ann:
    """
    A class for construction a feed forward neural network with an arbitrary number of 
    hidden layers.
    
    Parameters
    -----------------------------------
    hidden_layers : list
        specifies the number of neurons in each hidden layer, e.g.,
        hidden_layers = [16, 32, 16]
        will produce a neural network with three hidden layers containing 16, 32 and 16 neurons,
        respectively.
    """
    
    def __init__(self, hidden_layers):

        # Check if 'layers' is a list
        if not isinstance(hidden_layers, list):
            raise TypeError("'layers' must be a list")

        self.hidden_layers = hidden_layers
        self.num_layers = len(hidden_layers)
        self.neurons = {}
    
    def build(self, num_input_features=64, activation='relu'):
        """
        Build the neural network
        
        Parameters
        ---------------------------------
        num_input_features : int
            the number of features in the training data
        activation : str
            specify which activation function to use in the network. Only 'relu' implemented
            at the moment.
        """
        
        # Initialize the weights and biases with random numbers and store in the dict params. 
        self.params = {"W1": np.random.random((self.hidden_layers[0], num_input_features))}
        self.params["b1"] = np.random.random((self.hidden_layers[0],1))
        self.input_size = num_input_features
      
        for l in range(1, self.num_layers):
            self.params["W" + str(l+1)] = np.random.random((self.hidden_layers[l],
                                                            self.hidden_layers[l-1]))
            self.params["b" + str(l+1)] = np.random.random((self.hidden_layers[l],1))

        self.params["W" + str(self.num_layers+1)] = np.random.random((
            1, self.hidden_layers[self.num_layers-1]))
        self.params["b" + str(self.num_layers+1)] = np.random.random((1,1))

        self.activation = act_fcn(activation)
            
    def _forward_pass(self):
        """
        Run a forward pass of the neural network
        """
        # compute forward pass
        
        ## you should store the values of the neurons in the different layers
        ## in a dictionary
        ## initialize it by
        
        self.neurons["z0"] = self.X
         
        # and then add the neural values of layers v1, z1, v2, z2, .., etc and finally layer y
        # in a loop
        # finally, compute cost and return
        
        # YOUR CODE HERE
        
        cost = .5 * np.sum( np.power(self.neurons["y"] - self.Y, 2) ) / self.samples 
        
        return cost
    
    def _backward_pass(self):
        """
        Run a forward pass of the neural network
        
        Returns
        ----------------------------------
        gradients : dict
            the gradients of the weights and biases
        """
        
        # compute backward pass
        gradients = {}
        
        # YOUR CODE HERE (compute gradients of all weights and biases)
        
        return gradients
        
    def fit(self, X, Y, learning_rate=0.001, epochs=1000, quiet=False):
        """
        Train the neural network
        
        Parameters
        -------------------------------------
        X : np.array 
            of size num_input_features x number of training samples
        Y : np.array 
            of size 1 x number of training samples
        learning_rate : int
            the step size in the gradient descent
        epochs: int
            number of iterations of gradient descent
        quiet : bool
            whether to print information during training process
        """
        
        self.costs = []
        self.X = X
        self.Y = Y
        self.sample_size = len(Y)
        
        for epoch in range(epochs):
            cost = self._forward_pass()
            self.costs.append(cost)
            gradients = self._backward_pass()
            
            for key in self.params.keys():
                self.params[key] = self.params[key] - learning_rate * gradients["d" + key]
            
            if epoch % 100 == 0 and not quiet:
                print(f"Epoch: {epoch:3d}  |  Cost: {cost:.6f}")

            
    def predict(self, x):
        """
        Run inference on a new data sample 

        Parameters
        ----------
        x : np.array
            of size num_input_features x number of inference samples

        Returns
        -------
        y : np.array
            of 1 x number of inference samples
        """
        values = [x]
        
        for l in range(self.num_layers):
            v = self.params["W" + str(l+1)] @ values[l] + self.params["b" + str(l+1)].squeeze()
            z = self.activation(v)
            values.append(z)
            
        y = self.params["W" + str(self.num_layers+1)] @ z + self.params["b" + str(self.num_layers+1)].squeeze()
        
        return y