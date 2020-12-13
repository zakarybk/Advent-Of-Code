with open('input.txt', 'r') as f:
    instructions = [b for b in f.read().split('\n')]

next_instruction = 0
executed = []
acc = 0

while next_instruction not in executed:
    executed.append(next_instruction)

    instruction = instructions[next_instruction].split(" ")[0].strip()
    value = instructions[next_instruction].split(" ")[1].strip()
    if '-' in value:
        value = int(value.replace('-', '')) * -1
    else:
        value = int(value)

    if instruction == "acc":
        acc += value
        next_instruction += 1
    elif instruction == "jmp":
        next_instruction += value
    elif instruction == "nop":
        next_instruction += 1

print(f"Infinite loop found! Acc = {acc}")