import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import pandas as pd

#'''
df = pd.read_excel("test_subject.xlsx", sheet_name = "1", usecols = "A, B")
xData = np.asarray(df["P1"])
yData = np.asarray(df["I1"])
'''
df = pd.read_excel("0930-test.xlsx", sheet_name = "1", usecols = "C, D")
xData = np.asarray(df["P2"])
yData = np.asarray(df["I2"])
#'''
plt.plot(xData, yData, 'r-',label = "Raw Data")
peaks, _ = signal.find_peaks(yData, height = 0)

plt.legend()
plt.show()