from psana import *
import math
import matplotlib.pyplot as plt
import numpy as np
import h5py
h5 = h5py.File('/reg/d/ana01/temp/davidsch/molecular_runs_all.h5', 'r') # this is to get the file that I need
idxrun72 = h5['run'][:] ==72
idx3 = h5['predict_enPeaks'][:] == 3 
idx3 = np.logical_and(idxrun72, idx3) #Already includes 72
e2pos = h5['regr_predict_acq.e2.pos'][:]
e2Bounds = np.logical_and(e2pos >= 2.0, e2pos < 4.3)
idx3e2run72 = np.logical_and(e2Bounds, idx3)
w = h5['acq.waveforms']
e1pos = h5['regr_predict_acq.e1.pos'][:]

noNegNums = np.array(filter(lambda x: x > -1, e1pos)) #Filtering all of the nega

