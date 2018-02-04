# def greet(name="Ryu", time="Morning"):
# 	print(f"Good {time}, {name}, hope you are well")

# name = input("Enter your name: ")
# time = input("Enter time of day: ")

# greet()

def area(radius):
	return (3.142 * radius * radius)

def vol(area, length):
	print(area * length)

radius = int(input("Enter a radius: "))
length = int(input("Enter a length: "))

# areaCalc = area(radius)
vol(area(radius), length)