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

while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        time_tuple = localtime()
        fn = "/fc/data-logger.txt"
        
        # Open the file for appending and write a line of text to it
        with open(fn, "a") as f:
            f.write("\nLocal time: {}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
                time_tuple[0], time_tuple[1], time_tuple[2],
                time_tuple[3], time_tuple[4], time_tuple[5]))
            f.write("\ntemp=" + str(t))
            f.write("\nhumidity=" + str(h))
            f.write("")  # Add an empty line to separate entries

        sleep(2)

    except OSError as e:
        print("Error Data")

