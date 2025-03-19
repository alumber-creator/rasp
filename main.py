import serial
import time

# Configure the serial port
# '/dev/ttyS0' is the default serial port on Raspberry Pi 3
# If you're using a USB connection, it might be '/dev/ttyUSB0' or '/dev/ttyACM0'
ser = serial.Serial(
    port='/dev/ttyS0',  # Change this if needed
    baudrate=9600,      # Make sure this matches the Arduino's baud rate
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print("Raspberry Pi is ready to receive data from Arduino")

try:
    while True:
        # Check if data is available to read
        if ser.in_waiting > 0:
            # Read a line from serial (until newline character)
            raw_line = ser.readline()
            try:
                # Try to decode with UTF-8, replacing invalid characters
                line = raw_line.decode('utf-8', errors='replace').rstrip()
                print(f"Received data: {line}")
            except Exception as e:
                # If that still fails, print the raw bytes
                print(f"Received raw bytes: {raw_line}")
            
        time.sleep(0.1)  # Small delay to prevent CPU hogging
        
except KeyboardInterrupt:
    print("Program terminated by user")
    
finally:
    ser.close()
    print("Serial connection closed")

