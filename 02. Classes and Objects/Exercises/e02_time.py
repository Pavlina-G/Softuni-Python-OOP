class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):

        if seconds > self.max_seconds:
            seconds = 0
            minutes += 1
        if minutes > self.max_minutes:
            self.minutes = 0
            hours += 1
        if hours > self.max_hours:
            self.hours = self.max_hours

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"%02d:%02d:%02d" % (self.hours % 24, self.minutes % 60, self.seconds % 60)
        # return f"{self.hours % 24:02d}:{self.minutes % 60:02d}:{self.seconds % 60:02d}"
 
    def next_second(self):
        self.set_time(self.hours, self.minutes, self.seconds + 1)
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
time = Time(00, 58, 59)
print(time.next_second())
