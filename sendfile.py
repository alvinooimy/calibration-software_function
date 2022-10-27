import serial, time

ser = serial.Serial()
ser.port = "COM4"
ser.baudrate = 115200 
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 0

mode = 0
	
def receivedata():
	ser.close()
	ser.open()
	ser.flushInput()
	ser.flushOutput()
	
	path = 'outputfile.txt'
	f = open(path,'w')
	print("mode1")
	while True:         
		response = "".join(ser.readline().decode('utf-8'))
		if response != '':
			if response == "<<EOF>>":
				print(response)
				f.close()
				break
			f.write(response) 

try:
    ser.open()
except Exception as ex:
    print ("open serial port error " + str(ex))
    exit()

hello = 'I'.encode('utf-8')

while True:
    if mode == 0:
        ser.write(hello)
        response = ser.readline().decode('utf-8',errors='replace')
        if response == "OK":
            mode = 1
    elif mode == 1:
        receivedata()
        mode = 2
    elif mode == 2:
        ser.close()
        break
    