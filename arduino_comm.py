from collections import namedtuple
import serial
import struct
from time import sleep

class ArduinoComms:

	def __init__(self):
		self.Data = namedtuple('Data', 'x y')
		self.ser  = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=3, dsrdtr=True)
		# print(self.ser.dtr)
		sleep(5)
		# self.ser.write(4)
		# sleep(1)
		# self.ser.read(4)
		# sleep(4)
		# self.ser.dtr = False
		# sleep(1)
		# self.ser.reset_input_buffer()
		# self.ser.dtr = True
		# sleep(4)
		if self.ser.in_waiting > 0:
			res = self.ser.read(self.ser.in_waiting)
			print(f"READ TRASH: {res}")
		if self.ser.out_waiting > 0: 
			print(f"WRITE BUFFER HAS {self.ser.out_waiting} bytes! RESETTING OUTPUT BUFFER...")
			self.ser.reset_output_buffer()
			print(f"OUTPUT BUFFER RESET! OUTPUT BUFFER SIZE: {self.ser.out_waiting}")

	def read_data(self):
		if self.ser.in_waiting > 0:
			read_in = self.ser.read(8)
			vals = self.Data._make(struct.unpack('ii', read_in))
			return vals
		else:
			return None

	def send_data(self, x, y):
		if self.ser.out_waiting == 0: 
			data = struct.pack('ii', x, y)
			n = self.ser.write(data)
			# self.ser.flush()
			print("SENT DATA!")

			while self.ser.in_waiting != 8:
				sleep(.1)
				# if (self.ser.in_waiting == 4):
				# 	print("INCORRECT READ")
				# 	print(struct.unpack('I', self.ser.read(4)))
				# # 	self.ser.write(data)
				# 	return None

			read_x, read_y = self.read_data()
			if read_x != x or read_y != y: 
				print(f"WARNING:\n\tSENT {x} {y}\n\tRECV {read_x} {read_y}")
			else:
				return read_x, read_y
		else:
			print(f"OUTPUT BUFFER FULL: {self.ser.out_waiting}")

	def cleanup(self):
		self.ser.close()

if __name__ == '__main__':
	try:
		ac = ArduinoComms()
		data = ac.send_data(200,800)
		# data2 = ac.send_data(20,20)
		print(data)
		# print(data2)
		ac.cleanup()
	except KeyboardInterrupt:
		ac.cleanup()