import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ldr = 18

GPIO.setup(ldr, GPIO.IN)

def check_ldr():
    '''check for the presence of item by utilizing the change in intensity of light'''
    if GPIO.input(ldr) == GPIO.HIGH:
        output = "dark"
    elif GPIO.input(ldr) == GPIO.LOW:
        output = "bright"
    return output