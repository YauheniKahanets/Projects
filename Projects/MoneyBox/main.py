class MoneyBox:
    def __init__(self, capacity):

        self.capacity = capacity
        self.box = 0

    def can_add(self, v):
        v += self.box
        return v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.capacity = self.capacity - v
            return self.capacity
        else:
            return False
