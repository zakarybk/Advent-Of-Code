import pprint

INPUT_FILE = "input.txt"
TREE = '#'

with open(INPUT_FILE, 'r') as f:
	# Split by blank line, ignore single new lines
	passports = [x.replace('\n', ' ') for x in f.read().split('\n\n')]

REQUIRED_FIELDS = {
	"byr": True,
	"iyr": True,
	"eyr": True,
	"hgt": True,
	"hcl": True,
	"ecl": True,
	"pid": True,
	"cid": False
}

def required_fields_count(required_fields):
	count = 0
	for field, required in required_fields.items():
		if required:
			count += 1
	return count

def found_required_fields(fields):
	count = 0
	for field, required in REQUIRED_FIELDS.items():
		if required and field in fields:
			count += 1
	return count

valid_passports = 0

for passport in passports:
	passport_fields = passport.split(' ')
	passport_fields = [field[:field.find(':')] for field in passport_fields]

	required = required_fields_count(REQUIRED_FIELDS)
	required_found = found_required_fields(passport_fields)
	if required == required_found:
		valid_passports += 1
	

print("Found " + str(valid_passports) + " valid passports!")