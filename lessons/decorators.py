def cough_dec(func):

	def func_wrapper():
		# code before this function
		print(f"*cough*")
		func()
		print(f"*cough*")
		# code after the function

	return func_wrapper

@cough_dec
def question():
	print(f"Can you give me a discount on that?")

@cough_dec
def answer():
	print(f"It's only $5 you cheapskate")

question()
answer()