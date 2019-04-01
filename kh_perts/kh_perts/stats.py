from numpy import *
from scipy.optimize import minimize
import matplotlib
matplotlib.use('Agg')
import sys
for p in sys.path:
    if 'netcdf' in p.lower() or 'matplotlib' in p.lower():
        sys.path.remove(p)

print("TIME INTEGRATED")

import netCDF4
matplotlib.rcParams['savefig.dpi'] = 300
import matplotlib.pyplot as plt
import glob
import sys

with netCDF4.Dataset(sys.argv[1]) as f:
    for sample in range(1024):
        d = f.variables['sample_%d_rho' % sample][:,:,0]
        plt.pcolormesh(d)
        plt.savefig('plot_%d.png' % sample)
        plt.close('all')
