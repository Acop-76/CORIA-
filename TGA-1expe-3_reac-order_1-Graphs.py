#!/usr/bin/env python3
import numpy as np
import math
import matplotlib.pyplot as plt

fname="CORIA-wood-TGA-10K.csv" # ne doit pas contenir des labels de colonnes
print("lecture du fichier ",fname)
data=np.loadtxt(fname,delimiter=',',skiprows=1)
nbrData=data.shape[0]
print("*** nbr de data: ",nbrData)
Tp0=data[0][0]
Tpmax=data[nbrData-1][0]
print(" Tp initial :", Tp0,"  Tp final :",Tpmax)
print(" wood degradation mechanism: 3 parallel reactions")

# create figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# set labels
ax.set_xlabel('Tp (K)', fontsize=16)
ax.set_ylabel('mSurm0', fontsize=16)
ax.tick_params(axis='x', top='off')
ax.tick_params(axis='y', right='off')
# x and y limits
ax.set_xlim(0,1200)
ax.set_ylim(0,1)

# plot data
ax.plot(data[:,0],data[:,1],ls='solid', color = "black",linewidth=2, label="Tp_exp",alpha = 0.9)
ax.plot(data[:,0],data[:,2],ls='solid', color = "red",linewidth=2, label="Tp_cal",alpha = 0.9)
# tight layout    
plt.tight_layout()
# add grid
plt.grid()
# put legend
handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles,labels, loc=4, fontsize =13)
frame = legend.get_frame()
frame.set_facecolor('1.0')
frame.set_edgecolor('1.0')
plt.show()

