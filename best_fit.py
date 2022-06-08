import sys
import random

def bestFit(weight, c):
    
    num_of_elems = len(weight)
    result = 0

    # Store the remaining capacities for each bin
    remaining_capacity = [c]*num_of_elems

    # Try to insert all elements
    for i in range(0, num_of_elems):
        min_space_left = c+1
        best_bin_index = 0

        # Check each bin for that item
        for j in range(0, result):
            capacity_cond = remaining_capacity[j] >= weight[i]
            min_space_cond = remaining_capacity[j] - weight[i] < min_space_left
            # Insert to the bin if the conditions are satisfied
            if capacity_cond and min_space_cond:
                best_bin_index = j
                min_space_left = remaining_capacity[j] - weight[i]

        # Create a new bin if there is not enough space
        if min_space_left == c+1:
            remaining_capacity[result] = c - weight[i]
            result += 1
        # Update the remaining capacity of the inserted bin
        else:
            remaining_capacity[best_bin_index] -= weight[i]

    return result

def gen_random_instance(num_items, c):
	result = []
	for i in range(0, num_items):
		result.append(random.randint(1, c-1))
	return result

c = 10
num_items = 30
weights = gen_random_instance(num_items, c)
print(weights)
print(bestFit(weights, c))
