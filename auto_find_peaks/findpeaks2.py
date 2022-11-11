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

#scipy.signal.savgol_filter(x, window_length, polyorder)
#window_length即窗口长度。取值为奇数且不能超过len(x)。它越大，则平滑效果越明显；越小，则更贴近原始曲线。
#polyorder为多项式拟合的阶数。它越小，则平滑效果越明显；越大，则更贴近原始曲线。
y_smooth = signal.savgol_filter(yData, window_length = 5, polyorder = 3)
plt.plot(xData, y_smooth, 'r', label= "SG Data")

peaks, _ = signal.find_peaks(y_smooth, height = 0)
p_peaks = y_smooth[peaks]
p_peaks = p_peaks.tolist()

p_peaksmax_index1 = p_peaks.index(max(p_peaks))
p_peaksmax1 = peaks[p_peaksmax_index1]
p_peaks.pop(p_peaksmax_index1)

p_peaksmax_index2 = p_peaks.index(max(p_peaks))
p_peaksmax2 = peaks[p_peaksmax_index2]

if p_peaksmax1 > p_peaksmax2:
    hg_max = p_peaksmax1 + (p_peaksmax1 - p_peaksmax2)
elif p_peaksmax1 < p_peaksmax2:
    p_peaksmax2 = peaks[p_peaksmax_index2 + 1]
    hg_max = p_peaksmax2 + (p_peaksmax2 - p_peaksmax1)

centerline_height = int(yData[p_peaksmax1]) + 1
centerlinex = [hg_max] * centerline_height    
centerliney = np.arange(0,centerline_height)    

plt.plot(centerlinex, centerliney, "--", color = "black") #k = black

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
		
plt.plot(hg_peak2, y_smooth[hg_peak2], 'x', label = "hg-Peak", color = "black")


plt.legend()	
plt.show()