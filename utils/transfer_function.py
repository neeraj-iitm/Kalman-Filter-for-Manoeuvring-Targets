#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
from numpy import exp
def transfer_function(α,T):
    
    phi = np.array([
        
        [1, T, (1/α**2)*(-1 + exp(-α*T) + α*T)],
        [0,1, (1/α)*(1-exp(-α*T))],
        [0,0, exp(-α*T)]
        
    ])
    return phi

def tranfer_function_approximated(T):
    
    phi = np.array([
        
        [1,T,T**2 /2],
        [0,1, T],
        [0,0,1]
        
    ])


# In[ ]:




