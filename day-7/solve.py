import re

with open('input.txt', 'r') as f:
    bag_data = [b for b in f.read().split('\n')]

bag_and_contents = {}

bags_pattern = re.compile("\d (\w+ \w+)")

# sort bag data into dict : list
for data in bag_data:
    bag, _, bags = data.partition(" bags ")
    bag_and_contents[bag] = re.findall(bags_pattern, bags)

def bags_containing_bag(bags, bag):
    count = 0

    for contained_bags in bags:
        if bag in bag_and_contents[contained_bags]:
            print(contained_bags)
            count += 1

def bag_contains_any_of_these(bag, bags):
    contains = False
    look_through = bag_and_contents[bag]
    for l in look_through:
        if bag_and_contents[bag].contains(l):
            contains = True
            break
    return contains

def bags_containing_shiny_gold(bags):
    shiny_gold = "shiny gold"
    containing_gold = bags

    for bag in bags:
        if bag_contains_any_of_these(bag, containing_gold):
            containing_gold

# bag_of_choice
# all_bags bag = [contained]
# bags_containing bag
# bag of choice changes based on whether a golden bag was contained in it


bag_of_choice = "shiny gold"
first_level_golden_bags = [b for b in bag_and_contents if bag_of_choice in bag_and_contents[b]]
print(first_level_golden_bags)
all_possible = bags_containing_bag(first_level_golden_bags, bag_of_choice)
print(all_possible)

# print(bag_and_contents)