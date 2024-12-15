def sum(a, b):
	return a + b

def subtract(a, b):
	if a > b:
		return (a+b) - b
	return "A should be greater than B"
	
def multiply(a, b):
    return a * b
    
def division(a, b):
    return a/b
    
print(division(10,0))
