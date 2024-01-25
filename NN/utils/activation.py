#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:25:54 2024

@author: ole
"""
import numpy as np

class activation:
    
    def __init__(self, activation):
        assert activation == 'relu'  #Will only implement relu; feel free to add more choices
        self.activation = activation
        
    def __call__(self, x):
        if self.activation == 'relu':
            return np.maximum(0, x)
        
    def derivative(self, x):
        if self.activation == 'relu':
            return np.maximum(0, np.sign(x))