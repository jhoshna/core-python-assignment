def get_available_seats(total, booked):
    return [seat for seat in range(1, total + 1) if seat not in booked]


def book_seat(booked, seat, total):
    if seat in booked:
        print(f"Seat {seat} is already booked.")
    elif seat < 1 or seat > total:
        print(f"Seat {seat} is not valid.")
    else:
        booked.append(seat)
    return booked


def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    else:
        print(f"Seat {seat} is not booked.")
    return booked


total = 10
booked = [2, 5, 7]

new_seat = 3
cancel_seat_num = 5

booked = book_seat(booked, new_seat, total)
booked = cancel_seat(booked, cancel_seat_num)
available = get_available_seats(total, booked)

print("Available seats:",available)