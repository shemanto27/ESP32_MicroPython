import machine
import sdcard
import os
from utime import sleep, localtime
import dht

sensor = dht.DHT22(machine.Pin(13))

# Initialize SPI for SD Card
sd = sdcard.SDCard(machine.SPI(2), machine.Pin(5))

# Mount SD Card as a filesystem
vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")
print("Filesystem check")
print(os.listdir("/fc"))

fn = "/fc/data-logger.csv"
with open(fn, "a") as f:
            f.write("Time,")
            f.write("Temp,")
            f.write("Humidity\n")
            f.close()

while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        time_tuple = localtime()
        
        
        # Open the file for appending and write a line of text to it
        with open(fn, "a") as f:
            f.write("{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d},".format(       
                time_tuple[0], time_tuple[1], time_tuple[2],
                time_tuple[3], time_tuple[4], time_tuple[5])) # {}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}: This is formatting for the date and time
            f.write("{:.2f},".format(t))  # .2f: This means format as a floating-point number (f) with 2 digits after the decimal point (.2)
            f.write("{:.2f}\n".format(h))

        sleep(2)

    except OSError as e:
        print("Error Data")

