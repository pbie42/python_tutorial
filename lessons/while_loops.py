age = 25
num = 0

while num < age:
	if num == 0:
		continue
	if num % 2 == 0:
		print(f"{num}")
		if num > 10:
			break
	num += 1
