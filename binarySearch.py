def binarysearch_function(list , number):
	first = 0
	last = len(list) - 1
	found = False

	while not found:
		midpoint = (first + last) // 2
		if list[midpoint] == number:
			found = True
		else:
			if number < list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

array = [1 , 3 , 6 , 8 , 20 , 32 , 34 , 46 , 49 , 50 ]
print(binarysearch_function( array , 1))