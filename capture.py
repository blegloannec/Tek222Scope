#!/usr/bin/env python

from tek222 import *
import time

def main1d():
    Oscillo = Tek222('/dev/ttyUSB0')
    print Oscillo.get_id()
    print Oscillo.get_status()
    #print Oscillo.get_calibration()
    #print Oscillo.get_trigger()
    print Oscillo.get_curve('CH1')
    time.sleep(1)
    print Oscillo.get_curve('CH1')
    time.sleep(1)
    print Oscillo.get_curve('CH1')

def main2d():
    Oscillo = Tek222('/dev/ttyUSB0')
    data = []
    for _ in range(20):
        data.append(Oscillo.get_curve('CH2'))
        time.sleep(2)
    print ''.join(data)

main2d()
