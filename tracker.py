def func_counter(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		wrapper.counter += 1
	wrapper.counter = 0
	return wrapper

@func_counter
def foo(y):
	return y+2**3-34

