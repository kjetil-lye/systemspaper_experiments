from numpy import *
import os
import os.path
import scipy.optimize
import sys
for p in sys.path:
    if 'netcdf' in p.lower():
        sys.path.remove(p)

import netCDF4
import matplotlib
matplotlib.rcParams['savefig.dpi'] = 300
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from itertools import product
import h5py


import matplotlib2tikz
import PIL
import ot

import time
def writeMetadata(filename, data):
    im = PIL.Image.open(filename)
    
    meta = PIL.PngImagePlugin.PngInfo()

    for key in data.keys():
        meta.add_text(key, data[key])
    im.save(filename, "png", pnginfo=meta)
    
def showAndSave(name):
    fig = plt.gcf()
    ax = plt.gca()
    ax.text(0.95, 0.01, 'By Kjetil Olsen Lye\nkjetil.o.lye@gmail.com',
         fontsize=3, color='gray',
         ha='right', va='bottom', alpha=0.5, transform=ax.transAxes)

    matplotlib2tikz.save(name + '.tikz',
           figureheight = '\\figureheight',
           figurewidth = '\\figurewidth')
    
    savenamepng = name + '.png'
    plt.savefig(savenamepng)
    
    writeMetadata(savenamepng, {'Copyright' : 'Copyright, Kjetil Olsen Lye kjetil.o.lye@gmail.com'
                               })
    plt.close('all')


def load(f, sample):
    
    with netCDF4.Dataset(f) as d:
        return d.variables['sample_%d_rho' % sample][:,:,0]

def wasserstein_point_fast(data1, data2, i, j, a, b, xs, xt):
    N = data1.shape[2]
    #xs = zeros((N, 1))
    xs[:,0] = data1[i,j,:]
    #xt = zeros((N,1))
    xt[:,0] = data2[i,j,:]


    M = ot.dist(xs, xt, metric='euclidean')
    G0 = ot.emd(a,b,M)

    return sum(G0*M)


    
def wasserstein_point(data1, data2, i, j):
    M = data1.shape[2]
    matrix = zeros((M, M))
    for k1 in range(M):
        for k2 in range(M):
            matrix[k1,k2] = abs(data1[i,j, k1]-data2[i,j,k2])/M
    row_ind, col_ind = scipy.optimize.linear_sum_assignment(matrix)

    return matrix[row_ind, col_ind].sum()

def wasserstein(data1, data2):

    N = data1.shape[0]
    a = ones(N)/N
    b = ones(N)/N
    xs = zeros((N, 1))
    xt = zeros((N, 1))

    distance = zeros((N,N))
    firstTime = time.time()
    for i in range(N):

        for j in range(N):
            distance[i,j] = wasserstein_point_fast(data1, data2, i,j, a,b, xs, xt)


        currentTime = time.time()
        elapsedTime = currentTime - firstTime
        work = (i+1)*N
        remainingWork = N*N-work
        remainingTime = (float(elapsedTime)/work) * remainingWork
        print("Remaining time: %d : %d : %d : (%f)" % (int(remainingTime/(60*60)), int(remainingTime/60)%60, int(remainingTime)%60, remainingTime))
    

    x,y = mgrid[0:1:N*1j, 0:1:N*1j]

    plt.pcolormesh(x,y,distance)
    plt.colorbar()
    plt.title("Wasserstein distance between %d and %d" % (N, int(N/2)))
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    showAndSave('wasserstein_%d' %N)


    return sum(distance)/N**2

def wasserstein_point2_fast(data1, data2, i, j, ip, jp, a, b, xs, xt):
    N = data1.shape[2]
    #xs = zeros((N, 2))
    xs[:,0] = data1[i,j,:]
    xs[:,1] = data1[ip, jp, :]

    #xt = zeros((N,2))
    xt[:,0] = data2[i,j, :]
    xt[:,1] = data2[ip, jp, :]

    #a = ones(N)/N
    #b = ones(N)/N

    M = ot.dist(xs, xt, metric='euclidean')
    G0 = ot.emd(a,b,M)

    return sum(G0*M)


def wasserstein_point2(data1, data2, i, j, ip, jp):

    M = data1.shape[2]
    matrix = zeros((M, M))
    
    for k1 in range(M):
        for k2 in range(M):
            matrix[k1,k2] = sqrt(abs(data1[i,j, k1]-data2[i,j, k2])**2+abs(data1[ip,jp, k1]-data2[ip,jp, k2])**2)/M
    row_ind, col_ind = scipy.optimize.linear_sum_assignment(matrix)

    return matrix[row_ind, col_ind].sum()

def wasserstein2pt(data1, data2):

    N = data1.shape[0]
    a = ones(N)/N
    b = ones(N)/N
    xs = zeros((N,2))
    xt = zeros((N,2))
    distance = 0
    firstTime = time.time()
    for i in range(N):
        for j in range(N):

            for ip in range(N):
                for jp in range(N):
                    distance += wasserstein_point2_fast(data1, data2, i,j, ip, jp, a, b, xs, xt)

            currentTime = time.time()
            elapsedTime = currentTime-firstTime
            work = i*N+(j+1)
            remainingWork = N*N-work
            remainingTime = (float(elapsedTime)/work) * remainingWork
            print("2pt: Remaining time: %d : %d : %d : (%f)" % (int(remainingTime/(60*60)), int(remainingTime/60)%60, int(remainingTime)%60, remainingTime))

    
    return distance / N**4




def wasserstein2pt_fast(data1, data2):

    N = data1.shape[0]
    a = ones(N)/N
    b = ones(N)/N
    xs = zeros((N,2))
    xt = zeros((N,2))
    distance = 0
    firstTime = time.time()

    points = 0.1*array(range(0,10))
    for (n,x) in enumerate(points):
        for y in points:

            for xp in points:
                for yp in points:
                    i = int(x*N)
                    j = int(y*N)
                    ip = int(xp*N)
                    jp = int(yp*N)
                    distance += wasserstein_point2_fast(data1, data2, i,j, ip, jp, a, b, xs, xt)

        currentTime = time.time()
        elapsedTime = currentTime-firstTime
        work = (n+1)*N
        remainingWork = N*N-work
        remainingTime = (float(elapsedTime)/work) * remainingWork
        print("2pt: Remaining time: %d : %d : %d : (%f)" % (int(remainingTime/(60*60)), int(remainingTime/60)%60, int(remainingTime)%60, remainingTime))

    
    return distance / len(points)**4

def plot_histograms(data):
    points = [0.5, 0.7, 0.8]
    N = data.shape[0]
    M = data.shape[2]
    for x in points:
        for y in points:
            values = []
            i = int(x*N)
            j = int(y*N)
            for k in range(M):
                values.append(data[i,j,k])
            
            plt.hist(values, bins=40, normed=True)
            plt.xlabel('Value of $\\rho$')
            plt.ylabel('Probability')
            plt.title('Histogram at resolution %d, at $(%.2f, %.2f)$' % (N, x, y))

            showAndSave('hist_%d_%d_%d' %(N, i, j))


def plot_histograms2(data):
    points = [0.5, 0.7, 0.8]
    N = data.shape[0]
    M = data.shape[2]
    for x in points:
        for y in points:
            for xp in points:
                for yp in points:
                    valuesx = []
                    valuesy = []
                    i = int(x*N)
                    j = int(y*N)
                    ip = int(xp*N)
                    jp = int(xp*N)
                    for k in range(M):
                        valuesx.append(data[i,j,k])
                        valuesy.append(data[ip,jp,k])
            
                    plt.hist2d(valuesx, valuesy, bins=20, normed=True)
                    plt.colorbar()
                    plt.xlabel('Value of $\\rho(%.2f,%.2f)$' % (x,y))
                    plt.ylabel('Value of $\\rho(%.2f,%.2f)$' % (xp,yp))
                    plt.title('Histogram at resolution %d, between $(%.2f, %.2f)$ and $(%.2f, %.2f)$' % (N, x,y,xp,yp))
                    
                    showAndSave('hist2pt_%d_%d_%d_%d_%d' %(N, i, j, ip, jp))


resolutions = [64,128, 256, 512, 1024]

basename = 'n%d/euler_brownian_1.nc'
errors = []
wasserstein1pt = []
wasserstein2pterrors = []
for r in resolutions:
    filename = basename % r

    data1 = zeros((r,r,1024))
    for k in range(1024):
        d1 = load(filename, k)
        data1[:,:,k] = d1


    plot_histograms(data1)
    plot_histograms2(data1)


for r in resolutions[1:]:
    filename = basename % r
    filename_coarse = basename % int(r/2)
    data1 = zeros((r,r,r))
    data2 = zeros((r,r,r))
    for k in range(r):
        d1 = load(filename, k)
        d2 = repeat(repeat(load(filename_coarse, k), 2,0), 2,1)
        data1[:,:,k] = d1
        data2[:,:,k] = d2

    wasserstein2pterrors.append(wasserstein2pt_fast(data1, data2))
    print("wasserstein2pterrors=%s" % wasserstein2pterrors)
    

plt.loglog(resolutions[1:], wasserstein2pterrors, '-o')
plt.xlabel("Resolution")
plt.ylabel('$||W_1(\\nu^{\\Delta x}, \\nu^{\\Delta x/2})||_{L^1(D\\times D)}$')
plt.title("Wasserstein convergence for second correlation marginal")
showAndSave('wasserstein_convergence_2pt')
