def belt_count(dictionary):
	belts = list(dictionary.values())
	for belt in set(belts):
		num = belts.count(belt)
		print(f"There are {num} {belt} belts")

ninja_belts = {}
def ninjaIntro(dict):
	for key, val in dict.items():
		print(f"I am {key}, and I am a {val} belt")

while True:
	ninja_name = input("Enter a ninja name: ")
	ninja_belt = input("Enter a belt color: ")
	ninja_belts[ninja_name] = ninja_belt

	another = input("Add another? (Y/N): ")
	if another == 'y' or another == 'Y':
		continue
	else:
		break

# ninjaIntro(ninja_belts)
belt_count(ninja_belts)