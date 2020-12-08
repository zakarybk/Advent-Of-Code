import math

def decode_row(row_encoded, row_range):
    row = row_encoded[0].upper()
    new_range = row_range

    # lower limit
    if row == 'F' or row == 'L':
        new_range = (
            row_range[0], 
            row_range[0]+int(math.floor(float(row_range[1] - row_range[0]) / 2))
        )
    # upper limit
    elif row == 'B' or row == 'R':
        new_range = (
            row_range[0]+int(math.ceil(float(row_range[1] - row_range[0]) / 2)), 
            row_range[1]
        )

    if len(row_encoded) == 1:
        if row == 'F' or row == 'L':
            return new_range[0]
        elif row == 'B' or row == 'R':
            return new_range[-1]
    else:
        return decode_row(row_encoded[1:], new_range)

def decode_seat(seat_encoded):
    row = decode_row(seat_encoded[:7], (0, 127))
    column = decode_row(seat_encoded[7:], (0, 7))
    return (row, column)

def calc_seat_id(seat_pos):
    return seat_pos[0] * 8 + seat_pos[1]

if __name__ == '__main__':
    with open('input.txt') as f:
        seats_encoded = f.read()
        seats_encoded = [l for l in seats_encoded.split('\n') if l != '']

    highest_id = calc_seat_id(decode_seat(seats_encoded[0].strip()))

    for seat in seats_encoded:
        id = calc_seat_id(decode_seat(seat))
        if id > highest_id:
            highest_id = id

    print("Highest seat ID: " + str(highest_id))

