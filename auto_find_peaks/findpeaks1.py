import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import numpy as np
import pandas as pd

#'''
df = pd.read_excel("0930-test.xlsx", sheet_name = "hg-ar", usecols = "A, E")
xData = np.asarray(df["P1"])
yData = np.asarray(df["I1"])
'''
df = pd.read_excel("0930-test.xlsx", sheet_name = "hg-ar", usecols = "G, L")
xData = np.asarray(df["P2"])
yData = np.asarray(df["I2"])
#'''
plt.plot(xData, yData)
peaks, _ = find_peaks(yData, height = 0)

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
    
plt.plot(hg_max,0, "+")
peak = []
pdata = []
peak1 = []
pdata1 = []

for i in range(len(peaks)-1):
    if yData[peaks[i]] > yData[peaks[i+1]]:
        peak.append(peaks[i])
        pdata.append(yData[peaks[i]])

while len(peak1) < 10:
    maxpos = pdata.index(max(pdata))
    if peak[maxpos] < hg_max:
        peak1.append(peak[maxpos])
    peak.pop(maxpos)
    pdata.pop(maxpos)
    
#print(peak1)  
#plt.plot(peak1, yData[peak1], 'x')  

peak2 = []
i = 0
while peak1:
    p = peak1[0]
    if len(peak1) > 1:
        peak_diff = peak1[0]-peak1[1]
        if peak_diff > -5 and peak_diff < 5:
            p = int(abs((peak1[i]+peak1[i+1])/2))
            peak1.pop(1)
    peak1.pop(0)
    peak2.append(p)
    
peak2.sort()
#print(peak2)  
#plt.plot(peak2, yData[peak2], 'o')

peak3 = []
peak_1 = yData[peak2[0]]

while peak2:
    if yData[peak2[0]] >= peak_1:
        peak3.append(peak2[0])
    peak2.pop(0)

peak4 = []
for i in range(len(peak3)):
    if i > 0 and i < 4:
        peak4.append(peak3[i])
        
plt.plot(peak4, yData[peak4], 'X')
plt.show()