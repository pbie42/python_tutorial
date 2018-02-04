from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet("Naboo", 300000, 8, "Naboo System")
# print(f"Name is {naboo.name}")
# print(f"Radius is {naboo.radius}")
# print(f"Gravity is {naboo.gravity}")
# print(f"{naboo.orbit()}")
# print(f"{naboo.commons()}")

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f"The mass of {naboo.name} is {naboo_mass} and it's volume is {naboo_vol}")