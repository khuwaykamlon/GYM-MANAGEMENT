import serial
import time

# Initialize the serial port for the RFID reader
rfid_reader = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust port if necessary

# Read data from the RFID reader
while True:
    if rfid_reader.in_waiting > 0:
        rfid_tag = rfid_reader.readline().decode('utf-8').strip()
        print(f"RFID Scanned: {rfid_tag}")
        
        # Process the scanned RFID tag (match with member database)
        # Call the function to handle the check-in (defined below)
        check_in_member(rfid_tag)
        
    time.sleep(1)  # Wait before checking for new RFID data
