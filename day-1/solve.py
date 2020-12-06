INPUT_FILE = "input.txt"
TARGET_NUMBER = 2020

with open(INPUT_FILE, 'r') as f:
	expenses = f.readlines()
	expenses = [int(x) for x in expenses]

for cost in expenses:
	required_cost = TARGET_NUMBER - cost

	if required_cost in expenses:
		print("Found pair: " + str(cost) + ", " + str(required_cost))
		print("Answer: " + str(cost*required_cost))
		break