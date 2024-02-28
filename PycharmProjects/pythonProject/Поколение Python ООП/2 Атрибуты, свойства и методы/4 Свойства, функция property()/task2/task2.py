class HourClock:
    def __init__(self, hour):
        self.set_hours(hour)

    def get_hours(self):
        return self.hour

    def set_hours(self, hour):
        if isinstance(hour, int) and hour in range(1, 13):
            self.hour = hour
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)


time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)