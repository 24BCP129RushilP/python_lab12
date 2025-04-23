class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours % 24, total_minutes % 60)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

# Example usage
t1 = Time(10, 45)
t2 = Time(3, 30)
print("Added Time:", t1.add_time(t2))