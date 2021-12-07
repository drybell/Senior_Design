try:
	import RPi.GPIO as GPIO
except ImportError:
	pass
from time import sleep
import argparse

class MotorInterrupt(Exception):
	pass

class DCMotor: 

	def __init__(self, P1 = None, P2 = None, ENA = None, ENB = None, P3 = None, P4 = None, rpm = 120, duty = 70, pwm_freq = 10):
		self.ENA = ENA
		self.ENB = ENB 
		self.P1 = P1
		self.P2 = P2
		self.P3 = P3
		self.P4 = P4
		self.rpm = rpm
		self.ticks = 60 / rpm 
		self.cw_commands = [1, 0]
		self.ccw_commands = [0, 1]
		self.en_command = 0xff

		if P3 is None and P4 is None and ENB is None: 
			self.one_motor = "1"
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(P1,GPIO.OUT)
			GPIO.setup(P2,GPIO.OUT)
			GPIO.setup(ENA,GPIO.OUT)
			self.stop()
			self.driver = GPIO.PWM(ENA, pwm_freq)
			self.driver.start(duty)
		elif P1 is None and P2 is None and ENA is None: 
			self.one_motor = "2"
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(P3,GPIO.OUT)
			GPIO.setup(P4,GPIO.OUT)
			GPIO.setup(ENB,GPIO.OUT)
			self.stop()
			self.driver = GPIO.PWM(ENB, pwm_freq)
			self.driver.start(duty)
		else: 
			self.one_motor = False
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(P1,GPIO.OUT)
			GPIO.setup(P2,GPIO.OUT)
			GPIO.setup(P3,GPIO.OUT)
			GPIO.setup(P4,GPIO.OUT)
			GPIO.setup(ENA,GPIO.OUT)
			GPIO.setup(ENB,GPIO.OUT)
			self.stop()
			self.driver = GPIO.PWM(ENA, pwm_freq)
			self.driver2 = GPIO.PWM(ENB, pwm_freq)
			self.driver.start(duty)
			self.driver2.start(duty)

	def runCW(self):
		if self.one_motor == "1":
			# while True:
			GPIO.output(self.P1, GPIO.HIGH)
			GPIO.output(self.P2, GPIO.LOW)
		elif self.one_motor == "2":
			while True:
				GPIO.output(self.P3, GPIO.HIGH)
				GPIO.output(self.P4, GPIO.LOW)
		else:
			while True:
				GPIO.output(self.P1, GPIO.HIGH)
				GPIO.output(self.P2, GPIO.LOW)
				GPIO.output(self.P3, GPIO.HIGH)
				GPIO.output(self.P4, GPIO.LOW)

	def runCCW(self):
		if self.one_motor == "1":
			# while True:
			GPIO.output(self.P1, GPIO.LOW)
			GPIO.output(self.P2, GPIO.HIGH)
		elif self.one_motor == "2":
			while True:
				GPIO.output(self.P3, GPIO.LOW)
				GPIO.output(self.P4, GPIO.HIGH)
		else:
			try:
				while True:
					GPIO.output(self.P1, GPIO.LOW)
					GPIO.output(self.P2, GPIO.HIGH)
					GPIO.output(self.P3, GPIO.LOW)
					GPIO.output(self.P4, GPIO.HIGH)
			except MotorInterrupt:
				return 

	def retract(self):
		for i in range(21000000):
			self.runCW()

	def extend(self):
		for i in range(21000000):
			self.runCCW()

	def retract_half(self):
		for i in range(10000000):
			self.runCW()

	def extend_half(self):
		for i in range(10000000):
			self.runCCW()

	def extend_by_ticks(self, ticks):
		for i in range(ticks):
			self.runCCW()

	def retract_by_ticks(self, ticks):
		for i in range(ticks):
			self.runCW()

	def modifyRPM(self, new_rpm):
		self.rpm = new_rpm
		self.ticks = 60 / new_rpm

	def stop(self):
		# raise MotorInterrupt
		if self.one_motor == "1":
			GPIO.output(self.P1, GPIO.LOW)
			GPIO.output(self.P2, GPIO.LOW)
		elif self.one_motor == "2":
			GPIO.output(self.P3, GPIO.LOW)
			GPIO.output(self.P4, GPIO.LOW)
		else:
			GPIO.output(self.P1, GPIO.LOW)
			GPIO.output(self.P2, GPIO.LOW)
			GPIO.output(self.P3, GPIO.LOW)
			GPIO.output(self.P4, GPIO.LOW)

	def close(self):
		GPIO.cleanup()

if __name__ == '__main__':
	dc = DCMotor(P1 = 16, P2 = 18, ENA = 22, duty=25, pwm_freq=500)
	dc.retract_half()
# P1 = 16, P2 = 18, ENA = 22,
# P3 = 24, P4 = 26, ENB = 32
# dc = DCMotor(P1 = 16, P2 = 18, ENA = 22, duty=25, pwm_freq=500)
# dc = DCMotor( P1 = 16, P2 = 18, ENA = 22, P3 = 24, P4 = 26, ENB = 32, duty = 100, pwm_freq = 1000)
# try:
# 	dc.runCW()	
# except KeyboardInterrupt:
# 	dc.close()
# dc.retract()
