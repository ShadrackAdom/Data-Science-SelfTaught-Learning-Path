import time

print("FIRST")
def odd():

	listt = [7,81,21,2001]
	
	array_to_check = []

	for i in listt:
		if i % 2 == 0:
			array_to_check.append(i)

	
	if len(array_to_check) != 0:
		for i in array_to_check:
			print(array_to_check)
	elif len(array_to_check) == 0:
		print("There's no odds")

start_time = time.perf_counter()

# call your function here
odd()

# get the end time
end_time = time.perf_counter()

# calculate the run time in seconds
run_time = end_time - start_time

# print the run time
print(f"Function run time: {run_time:.6f} seconds")


print("SECOND")

def largest_odd_number(x, y, z, t):
    largest_odd = None

    if x % 2 != 0 and (largest_odd is None or x > largest_odd):
        largest_odd = x
    if y % 2 != 0 and (largest_odd is None or y > largest_odd):
        largest_odd = y
    if z % 2 != 0 and (largest_odd is None or z > largest_odd):
        largest_odd = z

    if largest_odd is not None:
        return largest_odd
    else:
        return "None of the numbers are odd."



largest_odd_number(7,81,21,2001)

start_time = time.perf_counter()

# call your function here
largest_odd_number(7,81,21,2001)

# get the end time
end_time = time.perf_counter()

# calculate the run time in seconds
run_time = end_time - start_time

# print the run time
print(f"Function run time seccc: {run_time:.6f} seconds")