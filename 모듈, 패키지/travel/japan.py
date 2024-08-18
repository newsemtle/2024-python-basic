from .travel import Travel


class Japan(Travel):
    def __init__(self):
        super().__init__("Japan", 4, 5)

    def locations(self):
        print("Tokyo, Osaka, Kyoto")
