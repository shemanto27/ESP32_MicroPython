from machine import Pin
from utime import sleep, localtime
import dht

sensor = dht.DHT22(Pin(23))

while True:
  try:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    time_tuple = localtime()
    
    print("Local time:", "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
    time_tuple[0], time_tuple[1], time_tuple[2],
    time_tuple[3], time_tuple[4], time_tuple[5]))
    print("temp=" + str(t))
    print("humidity" + str(h))
    sleep(2)
    print("")
    
  except OSError as e:
    print("Error Data")

