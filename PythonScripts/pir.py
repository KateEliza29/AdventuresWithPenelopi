import RPi.GPIO as GPIO
import time

# This is mandatory. Choose between BCM or BOARD. BCM varies between pi models, BOARD does not.
GPIO.setmode(GPIO.BOARD)

# Tells the pi to expect input through pin 8
pin = 8
GPIO.setup(pin, GPIO.IN)

# The sensor takes up to 60 seconds to power up and stabilise. Pause the script until the sensor is ready.
print('Sensor is eating weetabix')
time.sleep(60)
print('Sensor is now ready for anything')

# This is the method that will be called when the GPIO.RISING event is detected. The pin param is passed automatically when the
#method is triggered as a callback.
def risingHandler(input_pin):
        print('You moved! Input value: ' + str(GPIO.input(8)))

# When the pi detects a change in input from 0 to 1 (the rising edge), trigger the callback.
GPIO.add_event_detect(pin, GPIO.RISING, callback=risingHandler)

# Set the loop that keeps the script alive.
try:
        while True:
                time.sleep(0.001)
except KeyboardInterrupt:
                print('\nScript ended')
finally:
        GPIO.cleanup()