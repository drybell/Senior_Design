import pca9685 as p
from time import sleep 

class Servo:

	def __init__(self, index):
		self.pwm = p.PCA9685(0x40, debug=False)
		self.pwm.setPWMFreq(50)

		self.index = index

	def setPulse(self, value):
		self.pwm.setServoPulse(self.index, value)
		# sleep(.25)

if __name__ == '__main__':
	servo = Servo(0)

	# servo_flag.setPulse(1500)
	servo.setPulse(1500)
	# sleep(1)
	# servo.setPulse(2000)
	# sleep(1)
	# servo.setPulse(1000)