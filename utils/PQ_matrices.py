#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
from numpy import exp 


# In[41]:


def q11(α, T):
    coeff = 0.5/(α**5)
    αT = α * T
    rest = 1 - exp(-2*αT) + 2*αT + αT**3 * 2/3 - αT**2 * 2 - 4*αT*exp(-αT)
    return rest*coeff

def q12(α, T):
    αT = α*T
    coeff = 0.5/(α**4)
    rest = exp(-2*αT) + 1 - 2*exp(-αT) + 2*αT*exp(-αT) - 2*αT + αT**2
    return rest*coeff

def q13(α,T):
    αT = α*T
    coeff = 0.5/(α**3)
    rest = 1 - exp(-2*αT) - 2*αT*exp(-αT)
    return rest*coeff
    
def q22(α,T):
    αT = α*T
    coeff = 0.5/(α**3)
    rest = 4*exp(-αT) - 3 - exp(-2*αT) + 2*αT
    return rest*coeff
    
def q23(α,T):
    αT = α*T
    coeff = 0.5/(α**2)
    rest = exp(-2*αT) + 1 -2*exp(-αT)
    return rest*coeff
    
def q33(α,T):
    αT = α*T
    coeff = 0.5/α
    rest = 1 - exp(-2*αT)
    return rest*coeff


# In[80]:


def Q_cov(σ_m, α=1e8,T=0.5):
    
    expectation_matrix = np.array([
        
        [q11(α,T), q12(α,T), q13(α,T)],
        [q12(α,T), q22(α,T), q23(α,T)],
        [q13(α,T), q23(α,T), q33(α,T)]
    
    ]) 
    
    return 2*α*expectation_matrix*(σ_m**2)
    
    


# In[78]:


def Q_approximated(σ_m, α=0.25,T=0.05):
    
    expectation_matrix = np.array([
        
        [T**5 /20, T**4 /20, T**3 /6],
        [T**4 /8 , T**3 /3 , T**2/2 ],
        [T**3 /6 , T**2 /2 , T]
        
    ])
    
    return 2*α*expectation_matrix*σ_m**2
    



def P22(σ_r,σ_m,α,T ):
    a = 2*(σ_r/T)**2 
    b = (σ_m / (α**2 * T))**2
    c = 2 - (α*T)**2 + (α*T)**3 *2/3 - 2*exp(-α*T) - 2 *α*T*exp(-α*T)
    return a + (b*c)

def P23(σ_r,σ_m,α,T):
    a = σ_m**2 /(T*α**2)
    b= (α*T)**3 *2/3 - 2*exp(-α*T) - 2 *α*T*exp(-α*T)
    return a*b



def P_cov(σ_r,σ_m,α,T):
    expectation_matrix = np.array([
        
        [σ_r**2, σ_r**2/T, 0],
        [σ_r**2/T,P22(σ_r,σ_m,α,T), P23(σ_r,σ_m,α,T)],
        [0,P23(σ_r,σ_m,α,T), σ_m**2]
        
    ])
    return expectation_matrix

