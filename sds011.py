#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial, struct, time, csv, datetime, os

output_file = os.getenv("OUTPUT_FN", "/output/pm_log.csv")

ser = serial.Serial()
ser.port = os.getenv("TTY_DEV", "/dev/ttyUSB0")
ser.baudrate = int(os.getenv("TTY_SPEED", "9600"))

ser.open()
ser.flushInput()

byte, lastbyte = "\x00", "\x00"
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

k = 0 # current bucket
bs = int(os.getenv("BUCKET_SIZE", "60")) # bucket size for averages
pp = 10 # print module every
pm_25_avg = [] # bucket acc
pm_10_avg = [] # bucket acc

for i in range(0, bs):
    pm_25_avg.append(0)
    pm_10_avg.append(0)

while True:
    lastbyte = byte
    byte = ser.read(size=1)
    
    # We got a valid packet header
    if lastbyte == "\xAA" and byte == "\xC0":
        sentence = ser.read(size=8) # Read 8 more bytes
        readings = struct.unpack('<hhxxcc',sentence) # Decode the packet - big endian, 2 shorts for pm2.5 and pm10, 2 reserved bytes, checksum, message tail
        
        pm_25 = readings[0]/10.0
        pm_10 = readings[1]/10.0

        pm_25_avg[k] = pm_25
        pm_10_avg[k] = pm_10
        
        dt = datetime.datetime.now().replace(microsecond=0).isoformat().replace('T', ' ')
        
        if k % pp == 0:
            avg_25 = sum(pm_25_avg) / bs
            avg_10 = sum(pm_10_avg) / bs
            
            if avg_25 <= 10:
                rating = colored(0, 255, 0, 'GOOD')
            elif avg_25 <= 20:
                rating = colored(54, 193, 155, 'FAIR')
            elif avg_25 <= 25:
                rating = colored(216, 255, 0, 'MODERATE')
            elif avg_25 <= 50:
                rating = colored(255, 43, 12, 'POOR')
            elif avg_25 <= 75:
                rating = colored(255, 0, 0, 'VERY POOR')
            else:
                rating = colored(225, 12, 199, 'EXTREMELY POOR')
            
            print dt,"PM2.5:",round(avg_25, 2),"μg/m³ PM10:",round(avg_10, 2),"μg/m³",rating
        
        with open(output_file, 'ab') as csvfile:
            file = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file.writerow([dt, pm_25, pm_10])
            csvfile.close()
        
        k = k + 1
        if k >= bs:
            k = 0
