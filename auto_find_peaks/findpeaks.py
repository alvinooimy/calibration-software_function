import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy.optimize import curve_fit, leastsq
import sys

np.set_printoptions(threshold = sys.maxsize)
 
#df = pd.read_excel("0930-test.xlsx", sheet_name = "laser", usecols = "A, C")
df = pd.read_excel("0930-test.xlsx", sheet_name = "hg-ar", usecols = "A, E")
xData = np.asarray(df["P"])
yData = np.asarray(df["I"])

plt.plot(xData, yData, 'o', label = 'data')

def gaus(x, A, B):    
    return A*np.exp(-1*B*x**2)

def lorentzian( w, w0, w_p, gam ):
    return w * gam * pow(w_p,2) / ( (w*gam)**2 + ( pow(w,2) - pow(w0,2) )**2)

def multi_lorentz( x, params ):
    off = params[0]
    paramsRest = params[1:]
    assert not ( len( paramsRest ) % 3 )
    return off + sum( [ lorentzian( x, *paramsRest[ i : i+3 ] ) for i in range( 0, len( paramsRest ), 3 ) ] )

def res_multi_lorentz( params, xData, yData ):
    diff = [ multi_lorentz( x, params ) - y for x, y in zip( xData, yData ) ]
    return diff
  
generalWidth = 1
yDataLoc = yData

startValues = [ min( yData ) ]
counter = 0

while max( yDataLoc ) - min( yDataLoc ) >1:
    print(counter)
    counter += 1
    if counter > 10: ### max 20 peak...emergency break to avoid infinite loop
        break
    maxP = np.argmax( yDataLoc )
    maxY = yData[ maxP ]
    x0 = xData[ maxP ]
    startValues += [ x0, np.sqrt(maxY*x0), generalWidth ]
    popt, ier = leastsq( res_multi_lorentz, startValues, args=( xData, yData ) )
    yDataLoc = [ y - multi_lorentz( x, popt ) for x,y in zip( xData, yData ) ]
    #if ier == 6, find 6 set of lorentzian parameters 

testData = [ multi_lorentz(x, popt ) for x in xData ]
plt.plot(xData, testData)
'''  
parameters, covariance = curve_fit(gaus, x, y)
print(parameters)
fit_A = parameters[0]
fit_B = parameters[1] 

fit_y = gaus(x, fit_A, fit_B)
plt.plot(x, fit_y, '-', label='fit')
plt.legend()

peaks, _ = find_peaks(y)

plt.plot(x1,y1)
plt.plot(x1[peaks], y1[peaks], "x")
'''
plt.xlabel("Pixel")
plt.ylabel("Intensity")
print('done')
plt.show()