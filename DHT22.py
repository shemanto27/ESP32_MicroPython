#step-1: impoting necessary modules
from machine import Pin
from utime import sleep
import dht

#step-2: telling ESP32 where our sensor's data pin is connected
sensor = dht.DHT22(Pin(13))

#step-3: reading data continuously inside loop
while True:
  try:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()

    print("temp=" + str(t))
    print("humidity=" + str(h))
    sleep(2)
    print("")
    
  except OSError as e: # Error Handling  
    print("Error Data")