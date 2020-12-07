import re
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

height_pattern = re.compile("^(\d*)(cm|in)$")

def is_valid_height(hgt):
	match = height_pattern.search(hgt)
	return match is not None\
		and ((match.group(2) == "cm" and 150 <= int(match.group(1)) <= 193)\
		or (match.group(2) == "in" and 59 <= int(match.group(1)) <= 76))

hair_pattern = re.compile("^#[a-f|0-9]{6}$")
pass_id_pattern = re.compile("^\d{9}$")

FIELD_VALIDATIONS = {
	"byr": lambda num: 1920 <= int(num) <= 2002,
	"iyr": lambda num: 2010 <= int(num) <= 2020,
	"eyr": lambda num: 2020 <= int(num) <= 2030,
	"hgt": lambda hgt: is_valid_height(hgt),
	"hcl": lambda hcl: hair_pattern.search(hcl) is not None,
	"ecl": lambda ecl: ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
	"pid": lambda pid: pass_id_pattern.search(pid) is not None,
}

def required_fields_count(required_fields):
	count = 0
	for field, required in required_fields.items():
		if required:
			count += 1
	return count

def valid_fields_count(fields_values):
	count = 0
	for field, required in REQUIRED_FIELDS.items():
		if required and field in fields_values\
			and (field not in FIELD_VALIDATIONS or FIELD_VALIDATIONS[field](fields_values[field].strip())):
			count += 1
	return count

valid_passports = 0

for passport in passports:
	passport_fields = passport.split(' ')
	field_values = {field[:field.find(':')]: field[field.find(':')+1:] for field in passport_fields}

	required_count = required_fields_count(REQUIRED_FIELDS)
	valid_count = valid_fields_count(field_values)

	if required_count == valid_count:
		valid_passports += 1
	
print("Found " + str(valid_passports) + " valid passports!")