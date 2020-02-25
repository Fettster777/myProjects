#Chris Salehi

# Simple example of reading the MCP3008 analog input channels and printing
# them all out for solar test

import time
import datetime
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 18
#Master Input Slave Output
MISO = 23
#Master Output Slave Input
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
runTime = input("How many hours should the program run?: ")
runTimeHours = runTime * 60 * 60
t_end = time.time() + runTimeHours

print('Reading MCP3008 values, press Ctrl+C to quit...')
#open solartest2 file
file = open('solartest2.xls','a')
#create start time
st = time.time()
print 'Start Time'
#write start time to excel
file.write('Start Time' + '\n')
print (datetime.datetime.fromtimestamp(st).strftime('%Y-%m-%d %H:%M:%S'))
file.write(datetime.datetime.fromtimestamp(st).strftime('%Y-%m-%d %H:%M:%S') + "\n")
#print headers
print('| {0:>4} |'.format(*range(8)) + '|  Voltage |' + '|milliAmps|' + '| milliWatts|' + '|      dateTime       |')
file.write('| {0:>4} |'.format(*range(8)) + '\t' +  'Voltage' + '\t' + 'milliAmps' + '\t' + 'milliWatts' + '\t' + 'dateTime' + '\n')
#file.write('{0:>4}'.format(*range(8)) + "\t")
print('-' * 67)
# Main program loop.
#while True:
allValues = []
while time.time() < t_end:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(1):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    #allValues.append(values)
    # Print the ADC values.
    vol = float(values[i]) * (5.0/1023)
    ma = (( vol /1000.0) * 1000.00)
    mw = ((vol * (ma / 1000.0)) * 1000.0)
    t = time.time()
    print('| {0:>4} |'.format(*values) + "| {0:.6f} |".format(vol) + "| {0:.6f}|".format(ma) + '| {0:.7f} |'.format(mw) + datetime.datetime.fromtimestamp(t).strftime('| %Y-%m-%d %H:%M:%S |'))
    file.write('{0:>4}'.format(*values) + '\t' + "{0:.6f}".format(vol) + '\t' + '{0:.6f}'.format(ma) + '\t' + '{0:.7f}'.format(mw) + '\t' + datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') + '\n')
    # Pause for a minute
    time.sleep(60)
    allValues.append(values)
#end = datetime.datetime.fromtimestamp().strftime('%Y-%m-%d %H:%M:%S')
#sum total of analog values printed
sum = (sum(sum(v) for v in allValues))
print 'Total Analog'
file.write('Total Analog' + '\n')
print (sum) 
file.write(str(sum) + '\n')
#print milliwatt hours
mWH = 25 * runTime
print ('Milliwatt hours')
file.write('MilliWatt Hours' + '\n')
print (mWH)
file.write(str(mWH) + '\n')
#calculate and print end time
ed = time.time()
print 'End Time'
file.write('End Time' + '\n')
print (datetime.datetime.fromtimestamp(ed).strftime('%Y-%m-%d %H:%M:%S'))
file.write(datetime.datetime.fromtimestamp(ed).strftime('%Y-%m-%d %H:%M:%S') + '\n')
file.close()
