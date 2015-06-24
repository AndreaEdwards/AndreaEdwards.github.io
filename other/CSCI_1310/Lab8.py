#!usr/local/bin/python3
import sys
distance = float(sys.argv[1])

class Car:
	def drive(self, distance):
		time = distance / self.velocity
		return("%.2f" % time)


class Ferrari(Car):
	def __init__(self):
		self.velocity = 350
		self.pentalty = 0.5
		self.name = "Ferrari"
		print("Ferrari velocity is", self.velocity, "mph")

	def __str__(self):
		return(self.name)

	def drive(self, distance):
		time = (distance / self.velocity) + self.pentalty
		return("%.2f" % time)


class Kia(Car):
	def __init__(self):
		self.velocity = 60
		self.name = "Kia"
		print("Ferrari velocity is", self.velocity, "mph")

	def __str__(self):
		return(self.name)

class Report:
	def calculate(self, car):
		result = car.drive(distance)
		print("Time taken by", car, "is", result, "hours")

	def compare(self, car1, car2):
		car1_result = car1.drive(distance)
		car2_result = car2.drive(distance)

		if car1_result < car2_result:
			print(car1, "is faster than", car2)
		else:
			print(car2, "is faster than", car1)

def main():
	ferrari = Ferrari()
	kia = Kia()
	report = Report()
	report.calculate(ferrari)
	report.calculate(kia)
	report.compare(ferrari, kia)

main()
