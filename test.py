# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

from mantid import config
config['Q.convention'] = "Inelastic"
                       
ws = CreateSimulationWorkspace(Instrument='TOPAZ',
                               BinParams='1,100,10000',
                               UnitX='TOF')
                               
SetGoniometer(Workspace=ws, Axis0='30,0,1,0,1')      

# add peak
pws = CreatePeaksWorkspace(InstrumentWorkspace=ws, 
                           NumberOfPeaks=0, 
                           OutputWorkspace='peaks')
                           
SetUB('peaks', 2*np.pi, 2*np.pi, 2*np.pi, 90, 90, 90)

p = pws.createPeak([5,1,6]) 
pws.addPeak(p)

p = pws.createPeak([4,2,1]) 
pws.addPeak(p)

p = pws.createPeak([2,3,1]) 
pws.addPeak(p)

IndexPeaks(pws, Tolerance=1)

# integrate              
IntegrateEllipsoids(InputWorkspace=ws, 
                    PeaksWorkspace=pws, 
                    RegionRadius=0.14, 
                    SpecifySize=True, 
                    PeakSize=0.07, 
                    BackgroundInnerSize=0.09,
                    BackgroundOuterSize=0.11, 
                    OutputWorkspace=pws)
