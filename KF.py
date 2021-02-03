#---- Local Imports
from utils.PQ_matrices import P_cov, Q_cov
from utils.transfer_function import *
import utils.syntheticmeasurements as sms
from utils.mkf_internal import plot_track
from book_plots import reset_figsize

#---- Library Imports
import numpy as np
from matplotlib.pyplot import text
# from numpy import exp
from numpy.random import randn
from scipy.linalg import inv

#---- Plot imports
import matplotlib.pyplot as plt


def KFsim(σ_m,σ_r,α,T,Amax):
    
    P = P_cov(σ_r,σ_m,α,T)
    Q = Q_cov(σ_m, α,T)
    R = np.array([[σ_r**2]])

    F = transfer_function(α,T)
    H = np.array([[1., 0., 0.]])
    x = np.array([[0, 1000, 0 ]]).T
    dt = 0.1

    breakpoints = [0., 50.,  60.,  200.,   210.,  250.,  280.] 
    manoeuvres =  [0,  Amax, 0,    0.0,   -Amax,  Amax,   0]

    sm = sms.Synthetic_Measurement(σ_m,
                                   σ_r,
                                   breakpoints = breakpoints, 
                                   manoeuvres = manoeuvres,
                                   count=600)

    xm,vm =sm.meas_sim(1, 
                      start_pos=6000)


    xs =[]
    cov= []
    Ps= []
    
    for z in xm:
        # predict
        x = F @ x
        P = F @ P @ F.T + Q

        #update
        S = H @ P @ H.T + R
        K = P @ H.T @ inv(S)
        y = z - H @ x
        x += K @ y
        P = P - K @ H @ P
        Ps.append(P)
        xs.append(x)
        cov.append(P)

    xs, cov = np.array(xs), np.array(cov)
    # reset_figsize(15,10)
    #plot_track(xs[:, 0], sm.x_true, xm, cov, plot_P=0,title="Kalman Filter with Singer Model")
    
    
    return Ps, cov