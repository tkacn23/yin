#-*- coding: utf-8 -*-   
  
import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode( GPIO.BOARD )  
  
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
  
while True:  
    input_state = GPIO.input(11)  
  
    if input_state == False:  
        print( 'Button pressed' )  
        time.sleep(0.5)  