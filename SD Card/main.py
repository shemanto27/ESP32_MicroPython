# Import necessary modules
import machine  # MicroPython's machine module for hardware control
import sdcard   # MicroPython's sdcard module for SD card support
import os       # MicroPython's os module for filesystem operations

# Initialize SPI for SD Card
# SPI is a communication protocol used to communicate with devices like the SD card
sd = sdcard.SDCard(machine.SPI(2), machine.Pin(5))

# Mount SD Card as a filesystem
# Mounting is like connecting the SD card to the MicroPython system, so we can read and write to it
vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")  # "/fc" is a folder name we give to our mounted SD card
print("Filesystem check")
print(os.listdir("/fc"))  # List the contents of the SD card

# File path for a one-line log file
fn = "/fc/one-line-log.txt"
print("\nSingle block write")
# Open the file for writing and write a line of text to it
with open(fn, "w") as f:
    n = f.write("1234567890\n")  # one block
    print(n, "bytes written")

fn = "/fc/one-line-log.txt"
print("\nSingle block read")
# Open the file for reading and read its content
with open(fn, "r") as f:
    result = f.read()
    print(len(result), "bytes read")
    print()
    print(result)

# Create a long line of text for a multi-line log file
line = "abcdefghijklmnopqrstuvwxyz\n"
lines = line * 200  # Repeat the line 200 times to make a longer text
fn = "/fc/multi-line-log.txt"
print("\nMultiple block write")
# Open the file for writing and write the long text to it
with open(fn, "w") as f:
    n = f.write(lines)
    print(n, "bytes written")

fn = "/fc/multi-line-log.txt"
print("\nMultiple block read")
# Open the file for reading and read its content
with open(fn, "r") as f:
    result2 = f.read()
    print(len(result2), "bytes read")
    print()
    print(result2)
