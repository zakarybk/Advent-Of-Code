with open('input.txt') as f:
    all_answers = [answers.replace('\n', '') for answers in f.read().split('\n\n')]

answer_count = 0

for answers in all_answers:
    unique = set(answers)
    answer_count += len(unique)

print("Total answers: " + str(answer_count))