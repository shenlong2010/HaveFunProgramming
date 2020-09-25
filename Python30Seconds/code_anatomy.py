# Writing high performance Python code
def difference(a, b):

	# Not able to solve duplicate
	# return [item for item in a if item not in b]

	# Solve duplicate but slower than the previous
	# return [item for item in a if item not in set(b)]

	return [item for item in a if item not in make_set(b)]

def make_set(itr):
	print('Making set...')
	return set(itr)

print(difference([]))
