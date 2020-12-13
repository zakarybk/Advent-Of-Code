# unsovled

with open('input.txt', 'r') as f:
    instructions = [b for b in f.read().split('\n')]

next_instruction = 0
executed = []
acc = 0
changed_value = False

length = len(instructions) - 1
print(length)

while next_instruction != length:
    instruction = instructions[next_instruction].split(" ")[0].strip()
    value = instructions[next_instruction].split(" ")[1].strip()

    if '-' in value:
        value = int(value.replace('-', '')) * -1
    else:
        value = int(value)

    print(instruction)

    if instruction == "acc":
        executed.append(next_instruction)
        acc += value
        next_instruction += 1

    elif instruction == "jmp":
        if not changed_value and (next_instruction + value) in executed:
            instructions[next_instruction] = f"nop {value}"
            changed_value = True
            print(f"Changed jmp to nop {value}")
        else:
            executed.append(next_instruction)
            next_instruction += value

    elif instruction == "nop":
        if not changed_value and (next_instruction + 1) in executed:
            instructions[next_instruction] = f"jmp {value}"
            changed_value = True
            print(f"Changed nop to jmp {value}")
        else:
            executed.append(next_instruction)
            next_instruction += 1

print(f"Infinite loop found! Acc = {acc}")