#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import numpy as np
# import scipy as sp
# import matplotlib.pyplot as plt
from scipy import signal
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500, endpoint=False)
plt.plot(t, signal.square(2 * np.pi * 5 * t))
plt.ylim(-2, 2)
# def squareWave(N):
#     Fs = 200 # Sampling frequency
#     tmax = 3 # End time in seconds
#     t = np.linspace(0,tmax,Fs*tmax) # Create time array
#     mC = #implementing the above summation
#     plt.figure(1); plt.clf()
#     plt.plot(mC[1:200])
#     plt.show()
