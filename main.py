class Car:
    def __init__(self, color: str, count_passengers_seat: bool, is_busy: bool):
        self.color = color
        self.count_passengers_seat = count_passengers_seat
        self.is_busy = is_busy
    def __str__(self):
        return f'Car: {self.color=} {self.count_passengers_seat=} {self.is_busy=}'

