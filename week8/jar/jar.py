class Jar:
    def __init__(self, capacity=12):
        if not capacity:
            self.capacity = 12
        if capacity < 0:
            raise ValueError
        else:
            self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        else:
            self.size -= n
    
    def get_capacity(self):
        return self.capacity

    def get_size(self):
        return self.size

    def set_capacity(self, n):
        if n < 0:
            raise ValueError
        else:
            self.capacity = n