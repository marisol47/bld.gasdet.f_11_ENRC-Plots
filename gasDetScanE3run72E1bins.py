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

noNegNums = np.array(filter(lambda x: x > -1, e1pos)) #Filtering all of the negative numbers out
minNum = min(noNegNums)
maxNum = max(noNegNums)
minNum = math.floor(minNum*10)/10                                                                                           
maxNum = math.ceil(maxNum*10)/10
binBounds = np.linspace(minNum, maxNum, 21)
all_bins_wavs = []
all_bins_idx = []
gasDetectionData = h5['bld.gasdet.f_11_ENRC'][:] # all of the gas detection values
medianGDD = np.median(gasDetectionData)

gasinterval = gasDetectionData >= medianGDD #analyzing all of the point bigger than or equal to the gas detection data


for i in range(len(binBounds)-1): 
	e1bin = np.logical_and(e1pos >= binBounds[i], e1pos < binBounds[i+1])
	boolbin = np.logical_and(e1bin, idx3e2run72)
	boolbin = np.logical_and(boolbin, gasinterval)
	if sum(boolbin) >20: # checks that there are atleast 20 items on the array before creating a bin to plot
		ch0_e1_bin = w[boolbin, 0, :]
		bin_mean  = np.mean(ch0_e1_bin, axis = 0)
		all_bins_wavs += [bin_mean]
		all_bins_idx += [i]


mean = np.mean(all_bins_wavs, axis = 0)
plt.plot(mean, label = "mean of plots")



for idx,wv in zip(all_bins_idx ,all_bins_wavs): # a way to plot a list of arrays more efficiently
	
	plt.plot(wv, label = "bin %f " %binBounds[idx])
	
plt.legend()	
plt.show()

