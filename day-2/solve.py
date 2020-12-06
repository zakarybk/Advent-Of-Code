INPUT_FILE = "input.txt"

with open(INPUT_FILE, 'r') as f:
	policy_password = f.readlines()

valid_count = 0

for grouped in policy_password:
	policy_lower_limit = int(grouped[0:grouped.find("-")])
	policy_upper_limit = int(grouped[grouped.find("-")+1:grouped.find(" ")])
	policy_letter = grouped[grouped.find(":")-1]
	password = grouped[grouped.find(":")+1:].strip()

	print(policy_lower_limit)
	print(policy_upper_limit)
	print(policy_letter)
	print(password)

	occurrence_count = password.count(policy_letter)
	print("occurrence_count: " + str(occurrence_count))

	if occurrence_count >= policy_lower_limit and occurrence_count <= policy_upper_limit:
		valid_count += 1

print("Vailid passwords matching policy: " + str(valid_count))