from threading import Thread
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings( 0 )
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)






print( "hc595 walk" )

shift = 5
latch = 6
data = 13

GPIO.setup( shift, GPIO.OUT )
GPIO.setup( latch, GPIO.OUT )
GPIO.setup( data, GPIO.OUT )

#shift, latch_clock_pin, data_pin, value, delay
def hc595(aantal_aan):
   # implementeer deze functie
   #Eerst alle ledjes uit voor in het geval dat er nog leds aan staan
   for i in range(8):
       GPIO.output(data,GPIO.LOW)
       GPIO.output(shift,GPIO.HIGH)
       GPIO.output(shift,GPIO.LOW)
   GPIO.output(latch,GPIO.HIGH)
   GPIO.output(latch,GPIO.LOW)
   #Zet het aantal leds aan volgens de imput parameter 'aantal_aan'
   for i in range(aantal_aan):
       GPIO.output(data,GPIO.HIGH)
       GPIO.output(shift,GPIO.HIGH)
       GPIO.output(shift,GPIO.LOW)
   GPIO.output(latch,GPIO.HIGH)
   GPIO.output(latch,GPIO.LOW)

# while True:
#     aantal = int(input('hoeveel ledjes wil je laten branden?'))
#     hc595(rating())






