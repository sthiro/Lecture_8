class Jar():
    def __init__(self, capacity=12):
        self.int_checker(capacity, "capacity")

        self._capacity = capacity # jar size
        self._size = 0 # number of cookiess

    def __str__(self):
        num_cookies = self._size
        return "🍪" * num_cookies


    def deposit(self, n):
        self.int_checker(n, "deposit")
        
        if not self._capacity >= n + self._size:
            raise ValueError("Jar is full, Invalid deposit")
        
        self._size += n


    def withdraw(self, n):
        self.int_checker(n, "withdraw")

        if n > self._size:
            raise ValueError("Insufficient cookies")
        
        self._size -= n

    def int_checker(self, n, type):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f"Invalid {type} numer")


    @property
    def capacity(self):
        return self._capacity
    

    @property
    def size(self):
        return self._size

