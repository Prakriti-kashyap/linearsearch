# This function uses global variable s
def f():
	print("Inside Function", s)

# Global scope
s = "I love PYTHON"
f()
print("Outside Function", s)
