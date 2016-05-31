#!/usr/bin/env python

import serial

# NB: Utiliser le channel *actif* sur l'oscillo pour recuperer les donnees en mode XY !!

class Tek222:
    def __init__(self,device):
        self.Buttons = {'CLEAR' : '1',
                        'Menu Item 0' : '2',
                        'Menu Item 1' : '3',
                        'Menu Item 2' : '4',
                        'Menu Item 3' : '5',
                        'OFF' : '6',
                        'Trigger SOURCE' : '9',
                        'Trigger MODE' : 'A',
                        'Trigger SLOPE' : 'B',
                        'CH2 SELECT' : 'C',
                        'CH1 SELECT' : 'D',
                        'AUTO SETUP' : 'E',
                        'Front-Panel Setup Menu' : '11',
                        'Trigger Position Menu' : '12',
                        'Auxiliary Functions Menu' : '13',
                        'Display Mode Menu' : '14',
                        'Save Waveform Menu' : '19',
                        'Recall Waveform Menu' : '1A',
                        'STORE/NONSTORE' : '1B',
                        'Acq Mode Menu' : '1C',
                        'X10 Mag' : '20',
                        'Variable Gain' : '21',
                        'AUTO LVL: PUSH' : '22'}
        self.SerialPort = serial.Serial(device,9600,timeout=None,xonxoff=1)
 
    def simulate_button(self,button):
        self.SerialPort.write('BUT %s\r'%(self.Buttons[button]))

    def get_id(self):
        self.SerialPort.write('ID?\r')
        return self.SerialPort.readline()[:-1]

    def get_status(self):
        self.SerialPort.write('STA?\r')
        return self.SerialPort.readline()[:-1]

    def get_trigger(self):
        self.SerialPort.write('TRG?\r')
        return self.SerialPort.readline()[:-1]

    def get_calibration(self):
        self.SerialPort.write('CAL?\r')
        return self.SerialPort.readline()[:-1]

    def print_curve(self,channel):
        # channel in {CH1, CH2, REF1, ..., REF4}
        self.SerialPort.write('CURV? %s\r'%(channel))
        res = self.SerialPort.readline()#[6+len(channel):-2]
        #print res
        ps = 6+len(channel)
        resp_pref = res[:ps]
        print resp_pref
        fp_data = res[ps:ps+10]
        print fp_data
        frame_nr = res[ps+10:ps+12]
        print frame_nr
        byte_count = res[ps+12:ps+16]
        wf_size = int(byte_count,16)
        print byte_count, wf_size
        waveform = res[ps+16:ps+16+2*wf_size]
        print waveform
        checksum = res[ps+16+2*wf_size:ps+18+2*wf_size]
        print checksum

    def get_curve(self,channel):
        self.SerialPort.write('CURV? %s\r'%(channel))
        res = self.SerialPort.readline()
        ps = 6+len(channel)
        byte_count = res[ps+12:ps+16]
        wf_size = int(byte_count,16)
        waveform = res[ps+16:ps+16+2*wf_size]
        return waveform

    def close():
        self.SerialPort.close()
