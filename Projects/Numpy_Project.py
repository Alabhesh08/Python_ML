import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

np.random.seed(8) # For reproducibility of random number generator.


# Creating time axis
t = np.linspace(0,1,1000)
# print(type(t))

signal = np.sin(2*np.pi*6*t)
# plt.plot(t,signal)
# plt.show()

# Creating gaussian Noise
Gnoise = random.normal(loc=0, scale=0.15, size=len(t))

signal_noisy = signal + Gnoise

# Creating uniform Noise
Unoise = random.uniform(low=-0.15, high=0.15, size=len(t))
signal_noisy = signal_noisy + Unoise


# Calculating and printing statistics
print(
    "Statistics of Noisy Signal:",
    "\nMean",np.mean(signal_noisy),  # Mean of the noisy signal
    "\nStandard Deviation",np.std(signal_noisy),   # Standard deviation of the noisy signal
    "\nVariance",np.var(signal_noisy),   # Variance of the noisy signal
    "\nMinimum Value",np.min(signal_noisy),   # Minimum value of the noisy signal
    "\nMaximum Value",np.max(signal_noisy),   # Maximum value of the noisy signal

    "\n\nStatistics of Clean Signal:",
    "\nMean",np.mean(signal),  # Mean of the clean signal
    "\nStandard Deviation",np.std(signal),   # Standard deviation of the clean signal
    "\nVariance",np.var(signal),   # Variance of the clean signal
    "\nMinimum Value",np.min(signal),   # Minimum value of the clean signal
    "\nMaximum Value",np.max(signal)   # Maximum value of the clean signal
)


# Preprocessing: Normalization, Clipping and Threshold based filtering

# Normalization
#cant do min max normalization as noise is gaussian and uniform, min max normalization is sensitive to outliars
# usinf Z-score normalization
mean = np.mean(signal_noisy)
std = np.std(signal_noisy)

signal_norm = (signal_noisy - mean)/std

# Clipping
signal_norm[-3*1>signal_norm] = -3 # std dev =1, and -3 for -3 time std dev is the bound
signal_norm[3*1<signal_norm] = 3 #same
signal_preprocessed = signal_norm

# Threshold filtering


# Plotting the signals
plt.plot(t,signal)
plt.plot(t,signal_noisy)
plt.plot(t,signal_norm)
plt.plot(t,signal_preprocessed)
plt.xlabel('Time [S]')
plt.ylabel('Amplitude [V]')
plt.legend(['Clean signal','Noisy signal','Normalized','Clipped'])
plt.title("Signal with Noise")
plt.show()
