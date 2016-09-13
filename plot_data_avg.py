#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

## Plotting functions
def plot2d(data,avg_rad):
    xdata,ydata = [],[]
    for i in xrange(0,len(data),4):
        ydata.append(int(data[i:i+2],16))
        xdata.append(int(data[i+2:i+4],16))
    #plt.axis('scaled')
    plt.axis([0,255,0,255])
    plt.plot(moving_avg(xdata,avg_rad),moving_avg(ydata,avg_rad),linewidth=0.1)


def moving_avg(data,w):
    avgdata = []
    for i in xrange(w,len(data)-w):
        avgdata.append(sum(data[i-w:i+w+1])/(2.*w+1.))
    return avgdata


## Main
def main2d():
    if len(sys.argv)!=3:
        print >> sys.stderr, 'usage: %s avg_radius data_file' % (sys.argv[0])
        sys.exit(1)
    avg_rad = int(sys.argv[1])
    fich = sys.argv[2]
    f = open(fich,'r')
    fdata = f.read().strip()
    f.close()
    # IMPORTANT: Stupid hardcoded stuff below
    # "20" below is the number of waveforms to plot
    # (we assume here that the dataset contains at least
    # 20 waveforms and that we only plot the first 20)
    # NB: Recall that the scope cannot send data and measure at
    # the same time, hence there are time jumps in the datasets.
    # A proper moving average plotting requires the different
    # waveforms to be treated separately.
    # NB2: This hardcoded setting is valid for dataset xydata3
    for i in xrange(20):
        plot2d(fdata[i*2040:(i+1)*2040],avg_rad)
    plt.savefig(fich+'.pdf')
    plt.show()

main2d()
