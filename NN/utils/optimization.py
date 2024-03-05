#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 08:47:33 2024

@author: ole
"""
import numpy as np

class optimization:
    
    def __init__(self, method):
        assert method in ['gradientDescent', 'momentum', 'Adam'] 
        self.method = method
        self.counter = 0

               
    def update(self, W, dW, learning_rate=1e-4, beta=0):
        if self.counter == 0:
            v = {}
            s = {}
            for key in W.keys():
                v[key] = np.zeros_like(W[key])
                s[key] = np.zeros_like(W[key])
            self.v = v
            self.s = s

        for key in W.keys():            
            if self.method == 'gradientDescent':
                W[key] = W[key] -learning_rate * dW["d" + key]
            
            if self.method == 'momentum':
                self.v[key] = beta*self.v[key] + (1-beta)*dW["d" + key]
                W[key] = W[key] -learning_rate * self.v[key]

            if self.method == 'Adam':
                self.v[key] = beta*self.v[key] + (1-beta)*dW["d" + key]
                self.s[key] = .999*self.s[key] + (1-.999)*dW["d" + key]**2
                
                vhat = self.v[key] / (1-beta)
                shat = self.s[key] / (1-.999)
                
                W[key] = W[key] - (learning_rate*vhat)/(np.sqrt(shat)+1e-8)*dW["d" + key]
        self.counter += 1        
        return W