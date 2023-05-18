x,n = 3, 3

def fib(x):
	"""Assume x an int >=0
    Returns Fibonacci of x"""
    
	global numFibCalls
	numFibCalls = 0
	numFibCalls += 1

	if x == 0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)
	
def testFib(n):
	for i in range(n+1):
		global numFibCalls
		numFibCalls = 0
		print(f"fib of {i} = {fib(i)}")
		print(f"fib called {numFibCalls} times")

print(fib(6))
testFib(6)