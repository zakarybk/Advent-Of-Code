with open('input.txt') as f:
    all_answers = [answers.replace('\n', ' ') for answers in f.read().split('\n\n')]

answer_count = 0

for answers in all_answers:
    group_answers = set()
    person_answers = answers.split(' ')
    group_answers = set(person_answers[0])

    for i in range(1, len(person_answers)):
        answer = set(person_answers[i])
        group_answers = group_answers.intersection(answer)

    answer_count += len(group_answers)

print("Total answers: " + str(answer_count))