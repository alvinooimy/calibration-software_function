import serial, time

ser = serial.Serial()
ser.port = "COM4"
ser.baudrate = 115200 
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 0.5          #non-block read 0.5s

try:
    ser.open()
except Exception as ex:
    print ("open serial port error " + str(ex))
    exit()
   
''' 
ser.write(b"<<SENDFILE>>\n") #tell server we are ready to recieve
readline = lambda : iter(lambda:ser.read(1),"\n")
with open("somefile.txt","wb") as outfile:
    while True:
        line = "".join(readline())
        if line == "<<EOF>>":
            break #done so stop accumulating lines

'''
path = 'outputfile.txt'
f = open(path,'w')

while True:  
    response = "".join(ser.readline().decode('utf-8'))
    if response != '':
        if response == "<<EOF>>":
            print(response)
            break
        f.write(response)
        
f.close()
ser.close()