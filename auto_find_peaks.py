import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import pandas as pd

hg_max = 0
centerline_height = []
hg_data = []
hg_peak = []
ar_data = []
ar_peak = []
dist = 0

def find_hgar_dividerpoint():
    try:
        global hg_max, hg_data, hg_peak, ar_data, ar_peak, centerline_height, dist
        
        '''
        df = pd.read_excel("test_subject.xlsx", sheet_name = "1", usecols = "A, B")
        xData = np.asarray(df["P1"])
        yData = np.asarray(df["I1"])
        #'''
        '''
        df = pd.read_excel("test_subject.xlsx", sheet_name = "1", usecols = "C, D")
        xData = np.asarray(df["P2"])
        yData = np.asarray(df["I2"])
        #'''
        #'''
        df = pd.read_excel("test_subject.xlsx", sheet_name = "1", usecols = "E, F")
        xData = np.asarray(df["P3"])
        yData = np.asarray(df["I3"])
        #'''
        
        #plt.plot(xData, yData, 'b', label= "Raw Data")
        
        y_smooth = signal.savgol_filter(yData, window_length = 21, polyorder = 3)
        #plt.plot(xData, y_smooth, 'r', label= "SG Data")

        peaks, _ = signal.find_peaks(y_smooth, height = 0)
        p_peaks = y_smooth[peaks]
        p_peaks = p_peaks.tolist()

        p_peaksmax_index1 = p_peaks.index(max(p_peaks))
        p_peaksmax1 = peaks[p_peaksmax_index1]
        p_peaks.pop(p_peaksmax_index1)

        p_peaksmax_index2 = p_peaks.index(max(p_peaks))
        p_peaksmax2 = peaks[p_peaksmax_index2]

        if p_peaksmax1 > p_peaksmax2:
            dist = p_peaksmax1 - p_peaksmax2
            hg_max = p_peaksmax1 + dist
        elif p_peaksmax1 < p_peaksmax2:
            p_peaksmax2 = peaks[p_peaksmax_index2 + 1]
            dist = p_peaksmax2 - p_peaksmax1
            hg_max = p_peaksmax2 + dist

        centerline_height = int(yData[p_peaksmax1]) + 1
        centerlinex = [hg_max] * centerline_height    
        centerliney = np.arange(0,centerline_height)    

        plt.plot(centerlinex, centerliney, "-", color = "black") #k = black
        
        for i in peaks:
            if i < hg_max:
                hg_peak.append(i)
            else:
                ar_peak.append(i-hg_max)

        hg_data = y_smooth[:hg_max]
        ar_data = y_smooth[hg_max:]
        
        plt.plot(xData[:hg_max], hg_data, 'r', label= "HG")
        plt.plot(xData[hg_max:], ar_data, 'b', label= "AR")
        
        return 1
    except Exception as e:
        print("Error line: {}\nError: {}".format(e.__traceback__.tb_lineno, e))
        return 0

def find_hg_peaks():
    try:
        hg_pdata = hg_data[hg_peak].tolist()
        hg_peak1 = []
        while len(hg_peak1) < 5:
            maxpos = hg_pdata.index(max(hg_pdata))
            hg_peak1.append(hg_peak[maxpos])
            hg_peak.pop(maxpos)
            hg_pdata.pop(maxpos)

        hg_peak1.sort()
        hg_peak2 = []
        
        for i in range(len(hg_peak1)):
            if i > 0 and i < 4:
                hg_peak2.append(hg_peak1[i])
                
        plt.plot(hg_peak2, hg_data[hg_peak2], 'rx', label = "hg-Peak")

        return 1
    except Exception as e:
        print("Error line: {}\nError: {}".format(e.__traceback__.tb_lineno, e))
        return 0

def find_ar_peaks():
    try:
        ar_pdata = ar_data[ar_peak].tolist()	
        ar_peak1 = []
        ar_q1_peak = []
        ar_q2_peak = []
        ar_q3_peak = []
        
        #find q2 peak
        maxpos = ar_pdata.index(max(ar_pdata))
        ar_peak1.append(ar_peak[maxpos])
        
        #find q1 peak
        ar_q1 = (ar_peak[maxpos])/2

        for i in ar_peak:
            if i < ar_q1:
                ar_q1_peak.append(i)
                
        ar_q1_peaks = ar_data[ar_q1_peak].tolist()
        q1_peak = ar_q1_peaks.index(max(ar_q1_peaks))
        ar_peak1.append(ar_peak[q1_peak])
        
        #find q3 peak
        ar_q3 = ar_peak[maxpos] + dist
        
        for i in ar_peak:
            if i > ar_q3:
                ar_q3_peak.append(i)
                
        q3_pos = (len(ar_peak)) - (len(ar_q3_peak))       
        ar_q3_peaks = ar_data[ar_q3_peak].tolist()
        q3_peak = ar_q3_peaks.index(max(ar_q3_peaks))
        ar_peak1.append(ar_peak[q3_peak + q3_pos])
        
        #find q2 peak
        ar_q2 = dist * 1.1
        
        for i in ar_peak:
            if i > ar_q2 and i < ar_q3:
                ar_q2_peak.append(i)
                
        q2_pos = (len(ar_peak) - len(ar_q2_peak) - len(ar_q3_peak))       
        ar_q2_peaks = ar_data[ar_q2_peak].tolist()
        q2_peak = ar_q2_peaks.index(max(ar_q2_peaks))
        ar_peak1.append(ar_peak[q2_peak + q2_pos])
        
        ar_q1_line = [(ar_q1 + hg_max)]  * centerline_height
        ar_q2_line = [(ar_q2 + hg_max)]  * centerline_height
        ar_q3_line = [(ar_q3 + hg_max)]  * centerline_height
        liney = np.arange(0,centerline_height)     
        plt.plot(ar_q1_line, liney, '-.', label = "hg-q1", color = "green")        
        plt.plot(ar_q2_line, liney, '--', label = "hg-q2", color = "green")        
        plt.plot(ar_q3_line, liney, ':', label = "hg-q3", color = "green")   
        plt.plot(ar_peak1 + hg_max, ar_data[ar_peak1], 'x', label = "hg-Peak", color = "blue")        
        return 1
    except Exception as e:
        print("Error line: {}\nError: {}".format(e.__traceback__.tb_lineno, e))
        return 0
        
def main():
    try: 
        check = find_hgar_dividerpoint()
        if check != 1:
            raise
        check = find_hg_peaks()
        if check != 1:
            raise
        check = find_ar_peaks()
        if check != 1:
            raise
        plt.legend()
        plt.show()
    except:
        raise Exception
        
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error line: {}\nError: {}".format(e.__traceback__.tb_lineno, e))
