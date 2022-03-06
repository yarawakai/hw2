def doubler(func):
	def wrapper():
		string = func(func())
		print(string)
	return wrapper

@doubler
def hello(name):
	return "hello {name}"


doubler(hello("max"))
