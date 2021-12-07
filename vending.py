from dc_motor import DCMotor
from servo import Servo
from arduino_comm import ArduinoComms
from time import sleep

class VendingMachine:

	def __init__(self):
		self.actuator = DCMotor(P1 = 16, P2 = 18, ENA = 22, duty=25, pwm_freq=500)
		self.servo    = Servo(0)
		self.comm     = ArduinoComms()

	def get_item(self, item, x, y):
		read_x, read_y = self.comm.send_data(x,y)

		# START 
		self.servo.setPulse(2100)
		sleep(2)
		self.actuator.extend()
		sleep(15)
		self.servo.setPulse(2600)
		sleep(5)
		self.actuator.retract()
		sleep(15)

		#UNLOAD 
		self.servo.setPulse(1000)
		sleep(2)
		self.actuator.extend_by_ticks(4000000)
		sleep(18)
		self.servo.setPulse(800)
		sleep(2)
		self.actuator.retract_half()
		sleep(10)

		# RESET
		self.reset_partial(-1 * x)


		# self.servo.setPulse(2150)
		# self.actuator.extend()
		# sleep(5)
		# self.servo.setPulse(2500)
		# sleep(5)
		# self.actuator.retract_half()
		# sleep(5)
		# self.servo.setPulse(800)
		# sleep(5)
		# self.actuator.retract_half()
		# self.servo.setPulse(1500)
		# self.actuator.retract()
		return {'msg': f"DROPPED {item}!"}

	def reset(self, x_data):
		self.move_arm(x_data, 0)
		self.actuator.retract()
		sleep(10)
		self.servo.setPulse(1300)
		sleep(4)

	def reset_partial(self, x_data):
		self.move_arm(x_data, 0)
		self.servo.setPulse(1300)

	def move_arm(self, x, y):
		read_x, read_y = self.comm.send_data(x,y)
		return {'msg': f"SEND: {x} {y}, RCV: {read_x} {read_y}"}


if __name__ == '__main__':
	v = VendingMachine()
	v.reset(0)
	# v.move_arm(-200, 0)
	# try:
	# 	v.get_item("BANANA", 6200, 0)
	# except KeyboardInterrupt:
	# 	v.reset(-6200)