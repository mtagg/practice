#Practice for learning how a FFT works?

# Example code: 
# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.03-Fast-Fourier-Transform.html
# Youtube vid: 
# https://www.youtube.com/watch?v=Ty0JcR6Dvis&ab_channel=Reducible



import matplotlib.pyplot as plt
import numpy as np
# plt.style.use('seaborn-poster')

 
 
 
def generateSignal(sample_rate, frequency):
  sample_time = float(1/sample_rate)
  time = np.arange(0,1,sample_time)
  return 3*np.sin(2*np.pi*frequency*time)


"""
A recursive implementation of 
the 1D Cooley-Tukey FFT, the 
input should have a length of 
power of 2. 
"""
    
def FFT(x):
  n = len(x)
  
  if n == 1:
    return x

  xEven = FFT(x[::2])
  xOdd = FFT(x[1::2])
  factor = np.exp(-2j*np.pi*np.arange(n)/n)
  
  X = np.concatenate([xEven + factor[:int(n/2)] * xOdd,
                      xEven + factor[int(n/2):] * xOdd])
  return X





def main():
  
  sr = 2048
  st = float(1/sr)

  freq = 1
  x = generateSignal(sr, freq)
  
  freq = 4
  x += generateSignal(sr, freq)

  freq = 7   
  x += generateSignal(sr, freq)
  
  freq = 111
  x += generateSignal(sr, freq)


  t = np.arange(0,1,st)
  plt.figure(figsize = (8, 6))
  plt.plot(t, x, 'r')
  plt.ylabel('Amplitude')

  # plt.show()
  # xList = list(x)
  
  ##Use FFT to find the frequencies:
  # xLen = int(len(xList))
  # print(xLen)
  # for i in range(int(xLen/2)):
  #   print (str(xList[i]) + " , " + str(xList[i+int(xLen/2)]))
  
  
  X=FFT(x)
  N = len(X)
  T = 1/sr
  n = np.arange(N)
  freq = n/T
  
  #New figure
  plt.figure(figsize = (12, 6))
  
  #subplot 1
  plt.subplot(121)
  plt.stem(freq, abs(X), 'b', markerfmt=" ", basefmt="-b")
  plt.xlabel('Freq (Hz)')
  plt.ylabel('FFT Amplitude |X(freq)|')
  
  #subplot 2
  n_half = N//2
  freq_lower = freq[:n_half]
  plt.subplot(122)
  plt.stem(freq_lower, abs(X[:n_half])/n_half, 'b', markerfmt=" ", basefmt="-b")
  plt.xlabel('Freq (Hz)')
  plt.ylabel('Normalized FFT Amplitude')
  plt.tight_layout()
  
  plt.show()
  
  
  
  
  
  
main()
