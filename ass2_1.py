#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:31:32 2020

@author: florian
"""
import numpy as np
import matplotlib.pyplot as plt

class Ortho:
    
    def __init__(self,A):
        self.A = A
        self.m = np.shape(A)[0]
        self.n = np.shape(A)[1]
    
    # help function     
    def normalize(self,v):
        norm = np.linalg.norm(v)
        if norm == 0: 
            return v
        return v / norm
    
    # projection
    def project(self,u,v):
        return (v@u)/(u@u) * u

    def gramschmidt(self):
        A = self.A
        ortList = []
        for k in range(0,self.n):
            v_k = A[:,k]
            p_sum = np.zeros((self.m,))
            for i in range(k):
                p_sum += self.project(ortList[i],v_k)
            u_k = v_k - p_sum
            ortList.append(self.normalize(u_k))
        return np.array(ortList).T
    
    def test(self):
        Q = self.gramschmidt()
        Z = Q.T @ Q
        norm1 = (np.linalg.norm(Q,2)-1)/self.n *self.m
        norm2 = (np.linalg.norm(np.eye(self.n) - Z, 2))/self.n *self.m
        eig1 = np.max(np.abs(np.linalg.eig(Z)[0]-np.ones(self.n))) 
        det = np.abs(np.abs(np.linalg.det(Z))-1)
        return norm1,norm2,eig1,det
            

N = [1,10,100,500,1000,2000]
data =  []
for n in N:
    A = np.random.rand(n+2,n)
    Ort1 = Ortho(A)
    data.append(Ort1.test())
    print(n)

for i in range(len(data)):
    data[i]=list(data[i])

data= np.array(data)

plt.figure(0)
plt.plot(N, data[:,0],'x', label="2-norm")
plt.xlabel("Dimension")
plt.ylabel("Difference of 2-norm to 1")
plt.legend()

plt.figure(1)
plt.plot(N, data[:,1],'x', label="Derivation from Identity")
plt.xlabel("Dimension")
plt.ylabel("Difference of to Identity")
plt.legend()

plt.figure(2)
plt.plot(N, data[:,2],'x', label="Biggest mistake in eigenvalue")
plt.xlabel("Dimension")
plt.ylabel("Difference to eigenvalue 1")
plt.legend()
        
plt.figure(3)
plt.plot(N, data[:,3],'x', label="Determinant")
plt.xlabel("Dimension")
plt.ylabel("Difference to determinant")
plt.legend()
        
        
        
        
        
        
        

        