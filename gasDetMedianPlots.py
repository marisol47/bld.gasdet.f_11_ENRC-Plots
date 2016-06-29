from psana import *
import math
import matplotlib.pyplot as plt
import numpy as np
import h5py
h5 = h5py.File('/reg/d/ana01/temp/davidsch/molecular_runs_all.h5', 'r') # this is to get the file that I need
idxrun72 = h5['run'][:] ==72
idx3 = h5['predict_enPeaks'][:] == 3 
idx3 = np.logical_and(idxrun72, idx3) 
e2pos = h5['regr_predict_acq.e2.pos'][:]
e2Bounds = np.logical_and(e2pos >= 2.0, e2pos < 4.3)
idx3e2run72 = np.logical_and(e2Bounds, idx3)
w = h5['acq.waveforms']
e1pos = h5['regr_predict_acq.e1.pos'][:]
e1Bounds = np.logical_and(e1pos >= 3.6, e1pos < 5.8)
all_bins_wavs = []
all_bins_idx = []
gasDetectionData = h5['bld.gasdet.f_11_ENRC'][:]
medianGDD = np.median(gasDetectionData)
gasIntBig = gasDetectionData >= medianGDD
gasIntSml = gasDetectionData < medianGDD

gasIntBig = np.logical_and(gasIntBig, e1Bounds)
gasIntBig = np.logical_and(gasIntBig,idx3e2run72)
gas_det_big_bin = w[gasIntBig, 0, :]
big_mean_wav  = np.mean(gas_det_big_bin, axis = 0)
plt.plot(big_mean_wav/np.max(big_mean_wav), label = "Bigger Median")

gasIntSml = np.logical_and(gasIntSml, e1Bounds)
gasIntSml = np.logical_and(gasIntSml,idx3e2run72)
gas_det_sml_bin = w[gasIntSml, 0, :]
sml_mean_wav  = np.mean(gas_det_sml_bin, axis = 0)
plt.plot(sml_mean_wav/np.max(sml_mean_wav), label = "Smaller Median")
plt.title("Run 72 Class 3 all values High Low Medians Gas Detector Normalized")

plt.legend()
plt.show()




