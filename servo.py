
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,50)
p.start(7.5)
try:
	while True:
		p.ChangeDutyCycle(10.5)
		print "Changing to 150"
		time.sleep(2)
		p.ChangeDutyCycle(7.5)
		print "changing to 90"
		time.sleep(2)
		p.ChangeDutyCycle(3)
		print "changing to 0"

		time.sleep(2)

except KeyboardInterrupt:
	p.stop()

	GPIO.cleanup()
