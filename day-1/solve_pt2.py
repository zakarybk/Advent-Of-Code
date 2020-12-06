INPUT_FILE = "input.txt"
TARGET_NUMBER = 2020

with open(INPUT_FILE, 'r') as f:
	expenses = f.readlines()
	expenses = [int(x) for x in expenses]

expenses.sort()

def find_matching_cost(expenses, cost, target_cost):
	required_cost = target_cost - cost
	if required_cost in expenses:
		return required_cost

for cost in expenses:
	# two numbers added need to equal this
	target_cost = TARGET_NUMBER - cost

	for cost_2 in expenses:
		match = find_matching_cost(expenses, cost_2, target_cost)
		if match:
			print("Found three: " + str(cost) + ", " + str(cost_2) + ", " + str(match))
			print("Answer: " + str(cost*cost_2*match))
			break