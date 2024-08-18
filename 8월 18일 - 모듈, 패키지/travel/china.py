from .travel import Travel


class China(Travel):
    def __init__(self):
        super().__init__("China", 4, 5)

    def locations(self):
        print("Beijing, Shanghai, Guangzhou")
