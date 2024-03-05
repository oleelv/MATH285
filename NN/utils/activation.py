#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:25:54 2024

@author: ole
"""
import numpy as np

class activation:
    
    def __init__(self, activation):
        assert activation in ['tanh', 'sigmoid', 'relu']  # feel free to add more choices
        self.activation = activation
        
    def __call__(self, x):
    	if self.activation == 'tanh':
    	    return np.tanh(x)
        if self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-x))
        if self.activation == 'relu':
            return np.maximum(0, x)
        
    def derivative(self, x):
        if self.activative == 'tanh':
            return 1 / np.cosh(x)**2
        if self.activation == 'sigmoid':
            return self.activation(x)*(1-self.activation(x))
        if self.activation == 'relu':
            return np.maximum(0, np.sign(x))
