import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import pandas as pd

'''
df = pd.read_excel("test_subject.xlsx", sheet_name = "1", usecols = "A, B")
xData = np.asarray(df["P1"])
yData = np.asarray(df["I1"])
'''
df = pd.read_excel("test_subject.xlsx", sheet_name = "1", usecols = "C, D")
xData = np.asarray(df["P2"])
yData = np.asarray(df["I2"])
#'''

plt.plot(xData, yData, 'b', label= "Raw Data")

y_smooth = signal.savgol_filter(yData, window_length=9, polyorder=3, mode="nearest")
plt.plot(xData, y_smooth, 'r', label= "SG Data")

peaks, _ = signal.find_peaks(y_smooth, height = 0)
p_peaks = yData[peaks]
p_peaks = p_peaks.tolist()

p_peaksmax_index1 = p_peaks.index(max(p_peaks))
p_peaksmax1 = peaks[p_peaksmax_index1]
p_peaks.pop(p_peaksmax_index1)

p_peaksmax_index1 = p_peaks.index(max(p_peaks))
p_peaksmax2 = peaks[p_peaksmax_index1]

if p_peaksmax1 > p_peaksmax2:
    hg_max = p_peaksmax1 + (p_peaksmax1 - p_peaksmax2)
elif p_peaksmax1 < p_peaksmax2:
    hg_max = p_peaksmax2 + (p_peaksmax2 - p_peaksmax1)
    
plt.plot(hg_max,0, "k |") #k = black

peak = peaks.tolist()
hg_peak = []
ag_peak = []

for i in peaks:
	if i < hg_max:
		hg_peak.append(i)
	else:
		ag_peak.append(i)

hg_pdata = y_smooth[hg_peak].tolist()		
ag_pdata = y_smooth[ag_peak].tolist()
hg_peak1 = []
		
while len(hg_peak1) < 5:
    maxpos = hg_pdata.index(max(hg_pdata))
    if hg_peak[maxpos] < hg_max:
        hg_peak1.append(hg_peak[maxpos])
    hg_peak.pop(maxpos)
    hg_pdata.pop(maxpos)

hg_peak1.sort()
hg_peak2 = []

for i in range(len(hg_peak1)):
    if i > 0 and i < 4:
        hg_peak2.append(hg_peak1[i])
		
plt.plot(hg_peak2, y_smooth[hg_peak2], 'r x', label = "Peak")
plt.legend()	
plt.show()