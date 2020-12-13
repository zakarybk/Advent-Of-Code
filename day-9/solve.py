import math

with open('input.txt', 'r') as f:
    numbers = [int(b.strip()) for b in f.read().split('\n')]

preamble_count = 25
previous_numbers = numbers[:preamble_count]

def has_match_for_sum(numbers, sum):
    for num in numbers:
        x = abs(num - sum)
        if x in numbers:
            return True
    
    return False

def first_odd_number():
    # for each number after initial preamble_count
    for num in numbers[preamble_count:]:

        # two numbers will sum together to equal num
        if not has_match_for_sum(previous_numbers, num):
            return num

        # Update previous numbers
        previous_numbers.pop()
        previous_numbers.insert(0,num)

if __name__ == '__main__':
    print(f"No two previous numbers add up to {first_odd_number()}!!!")
