import numpy as np
from numpy.random import randn, normal


class Synthetic_Measurement:
    
    def __init__(self, σ_m, σ_r, count = 100, breakpoints = [], manoeuvres = [] ):
        #print("Synthetic Measurements are ready.")
        self.count  = count
        self.σ_m    = σ_m
        self.σ_r    = σ_r
        
        self.breakpoints = breakpoints
        self.manoeuvres  = manoeuvres
        
        assert len(self.breakpoints) == len(self.manoeuvres)
        
        self.x_true = []
        self.v_true = []
        self.a_true = []
        
        self.x_meas = []
        self.v_meas = []
        #self.a_meas = []
        
    def meas_sim(self, dt, start_pos = 0, start_vel = 0, start_acc = 0, pprint = False):
        x = start_pos
        v = start_vel
        a = start_acc
        bpc = 0
        time = 0.
        for i in range(int(self.count/dt)):
            x = x + v*dt
            self.x_true.append(x + normal(0,self.σ_m))
            self.x_meas.append(x + normal(0,self.σ_r))

            if float(time) in self.breakpoints:
                
                a = self.manoeuvres[bpc]
                if pprint : print(f"Manoeuvre={a} at time = {time}")
                bpc = bpc+1
            
            v= v + dt*a
            self.v_true.append(v+normal(0,self.σ_m))
            self.v_meas.append(v+normal(0,self.σ_r))
            self.a_true.append(a)
            time= time + dt
        return np.array(self.x_meas), np.array(self.v_meas)
    
    def combined_state_vector_measurements(self):
        combined=[]
        
        for (i,j) in zip(self.x_meas,self.v_meas) :
            combined.append([i,j])
        
        return np.array(combined)
