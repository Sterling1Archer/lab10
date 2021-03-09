import serial
import matplotlib.pyplot as plt
from drawnow import *

Data1 = [] # type: float
Data2 = [] # type: float

def PlotSignal():
    plt.ylim(0,4)
    plt.title('Ploting in Streaming AD0 from Arduino')
    plt.grid(True)
    
    plt.ylabel('Analog Signal AD0')
    plt.plot(Data1, 'r', label='Photoresistor voltage')
    plt.legend(loc='upper right')
    
    plt.ylabel('Analog Signal AD1')
    plt.plot(Data2, 'b', label='Thermistor voltage')
    plt.legend(loc='upper right')
    
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600)
    plt.ion()
    Dcounter = 0
    ser.flush()
    
    while True:
        
        while (ser.inWaiting()==0):
            pass # do nothing if no incoming data
        
        ardData = ser.readline().decode('utf-8')
        print(ardData)
        InputData = ardData.split(',')
        temp = float(InputData[0])
        Data1.append(temp)
        temp = float(InputData[1])
        Data2.append(temp)
        drawnow(PlotSignal)
        plt.pause(0.000001)
        Dcounter=Dcounter+1
        if(Dcounter>60):
            Dcounter=0
            Data1.pop(0)
            Data2.pop(0)
        
    ser.close()
