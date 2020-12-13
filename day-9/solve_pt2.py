import math
import solve

numbers = solve.numbers
invalid_number = solve.first_odd_number()

# find continuous set of numbers to add to invalid_number
first_index = 26
last_index = 26
cumulative = numbers[first_index]
found_set = False

while cumulative != invalid_number:

    # move the last index forwards
    if cumulative < invalid_number:
        last_index += 1
        cumulative += numbers[last_index]

    # move the first index forwards
    elif cumulative > invalid_number:
        cumulative -= numbers[first_index]
        first_index += 1

contiguous_range =  numbers[first_index:last_index]
contiguous_range.sort()
smallest = contiguous_range[0]
largest = contiguous_range[-1]

print(f"Anser: {smallest+largest}")





