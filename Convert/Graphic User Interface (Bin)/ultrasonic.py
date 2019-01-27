import RPi.GPIO as GPIO
import time
 


def presence_of_object():
    '''check for the presence of user using the ultrasonic sensor'''
    if distance()<100:
        return True
    else:
        return False
 
def distance():
    '''calculate the distance between a particular object and the sensor'''
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)


 
    #set GPIO Pins

    GPIO_TRIGGER = 20
    GPIO_ECHO = 21
     
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    diff= StopTime-StartTime
    dist = (diff*34300)/2
    return dist

