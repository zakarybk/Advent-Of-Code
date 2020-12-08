import math
import solve

if __name__ == '__main__':
    with open('input.txt') as f:
        seats_encoded = f.read()
        seats_encoded = [l for l in seats_encoded.split('\n') if l != '']

    highest_id = solve.calc_seat_id(solve.decode_seat(seats_encoded[0].strip()))
    seats = []

    for seat in seats_encoded:
        id = solve.calc_seat_id(solve.decode_seat(seat))
        seats.append(id)
        if id > highest_id:
            highest_id = id

    print("Highest seat ID: " + str(highest_id))

    seats.sort()

    for i in range(highest_id):
        if i not in seats:
            print("Empty seat!: " + str(i))


