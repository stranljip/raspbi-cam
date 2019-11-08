from picamera import PiCamera
from time import sleep
from datetime import datetime

import RPi.GPIO as GPIO

motionsensor_channel = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionsensor_channel,GPIO.IN)

camera = PiCamera()

recording = False
while 1==1:
    now = datetime.now()
    now_formatted = now.strftime("%Y%m%d-%H%M%S")
    
    if GPIO.input(motionsensor_channel):
        if not recording:
            camera.start_recording('/home/pi/hamstercam/' + now_formatted + '-hamster.h264')
            recording = True
            print(str(now) + " Starte Aufname")
        camera.wait_recording(20)
        print(str(now) + " Bewegung detektiert")
    else:
        if recording:
            camera.stop_recording()
            recording = False
            print(str(now) + " Keine Bewegung detektiert - Aufnahme gestoppt")

#camera = PiCamera()
#sleep(5)
#camera.capture('/home/pi/Desktop/camera.jpg')
    
GPIO.cleanup()
