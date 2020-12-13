with open('input.txt', 'r') as f:
    numbers = [int(b.strip()) for b in f.read().split('\n')]

numbers.sort()

# charging outlet near your seat
numbers.insert(0, 0)

# device's built-in joltage adapter
numbers.append(numbers[-1]+3)

difference_of_1 = 0
difference_of_3 = 0

for i in range(1, len(numbers)):
    previous = numbers[i-1]
    current = numbers[i]

    difference = current - previous

    if difference == 1:
        difference_of_1 += 1
    elif difference == 3:
        difference_of_3 += 1

print(f"Difference of 1: {difference_of_1}")
print(f"Difference of 3: {difference_of_3}")
print(f"Answer: {difference_of_1*difference_of_3}")
