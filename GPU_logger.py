""" Descr:
      A how-to log power consumption of nvidia gpus in a system using python.
      After obtaining results, user can plot them using matplotlib.
    author: 
      Ioannis Athanasiadis (supernlogn)
"""
import numpy as np
from matplotlib import pyplot as plt
import subprocess
import time, datetime
import re

def read_nvidia_power(timeDuration, timeStep=1, numGPUs=2, logFile=""):
  """
    Descr: 
      Function used to return nvidia times per timeStep(default = 1).
    Args:
      timeDuration: duration in seconds.
      timeStep: the measurement time step in seconds (integer only > 1).
      numGPUs: number of nvidia GPUs in the system.
      logFile: file path to write results live.
    Returns: 
      A numpy array of 1+numGPUs collumns
      1-st collumn are the timestamps of the measurements.
      2-nd collumn are the power measurements in Watts of the 1st GPU.
      3-rd collumn are the power measurements in Watts of the 2nd GPU.
      ...
      (numGPUs+1)-th collumn are the power measurements in Watts of the (numGPUs)-th GPU.
  """
  time_start = time.time()
  timeStep = int(timeStep)
  p = subprocess.Popen("nvidia-smi -l " + str(timeStep), shell=True, stdout=subprocess.PIPE)    
  pattern = re.compile("[0-9]*?[W]{1,1}[\s]{1,1}[/]{1,1}[\s]{1,1}[0-9]*?[W]{1,1}")
  if( logFile != "" ):
    output_f = open(logFile, "w")
  else:
    output_f = None
  measurements = []
  i = 0
  with p.stdout as f:
    while( time.time() - time_start < timeDuration ):
      time.sleep(1)
      s = "123123123123123"
      while( len(s) >= 10 and time.time() - time_start < timeDuration ):
        s = f.readline()
        s = s.decode('utf-8')
        m = re.findall(pattern, s)
        if( len(m) != 0 ):
          measurement = float(m[0].partition('W /')[0])
          if( i == 0 ):
            measurements.append([datetime.datetime.now(), measurement])
          elif( i == numGPUs-1 and output_f != None):
            measurements[-1].append(measurement)
            output_f.write(str(measurements[-1]) +"\n")
          else:
            measurements[-1].append(measurement) 
          i = (i+1)%numGPUs
  # if the last row of measurements is incomplete, then use -1.0 to fill it
  if( not len(measurements) < 2 ):
    while( len(measurements[-1]) != len(measurements[-2]) ):
      measurements[-1].append(-1.0)
    p.kill()
  if( output_f != None ):
    output_f.close()
  return np.array(measurements)

if __name__ == "__main__":
  measurements = read_nvidia_power(200, logFile="nv-power.txt")
  # plt.plot(measurements[0,:], measurements[1,:])
  # plt.show()