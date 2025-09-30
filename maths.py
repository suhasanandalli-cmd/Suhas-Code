def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mux(a, b):
	return a * b

# Division function
def div(a, b):
	if b == 0:
		raise ValueError("Cannot divide by zero.")
	return a / b

# Example usage
if __name__ == "__main__":
	print("Add:", add(2, 1))
	print("Sub:", sub(2, 1))
	print("Mux:", mux(2, 1))
	print("Div:", div(2, 1))