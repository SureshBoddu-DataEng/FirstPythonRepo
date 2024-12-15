def sum(a, b):
	return a + b

def subtract(a, b):
	if a > b:
		return (a+b) - b
	return "A should be greater than B"
	
def multiply(a, b):
    return a * b
    
def division(a, b):
    if b != 0:
        return a/b
    else:
        return "Denominator should not be zero"
    
print(division(10,0))
