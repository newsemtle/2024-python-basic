class Travel:
    def __init__(self, destination, nights, days):
        self.destination = destination
        self.nights = nights
        self.days = days

    def info(self):
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration}")
