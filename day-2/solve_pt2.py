INPUT_FILE = "input.txt"

with open(INPUT_FILE, 'r') as f:
	policy_password = f.readlines()

valid_count = 0

for grouped in policy_password:
	policy_first_index = int(grouped[0:grouped.find("-")])
	policy_last_index = int(grouped[grouped.find("-")+1:grouped.find(" ")])
	policy_letter = grouped[grouped.find(":")-1]
	password = grouped[grouped.find(":")+1:].strip()

	print(policy_first_index)
	print(policy_last_index)
	print(policy_letter)
	print(password)

	first_index_letter = password[policy_first_index-1]
	last_index_letter = password[policy_last_index-1]

	is_valid = (first_index_letter == policy_letter or last_index_letter == policy_letter) and\
		not (first_index_letter == policy_letter and last_index_letter == policy_letter)

	if is_valid:
		valid_count += 1

print("Vailid passwords matching policy: " + str(valid_count))