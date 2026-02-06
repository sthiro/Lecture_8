class Jar:
    def __init__(self, capacity=12):
        if not capacity >= 0 or not capacity.is_integer():
            raise ValueError("Invalid jar capacity")

        self._capacity = capacity # jar size
        self._size = 0 # number of cookies

    def __str__(self):
        num_cookies = self._size
        for _ in range(num_cookies):
            print("🍪", end="") # print 🍪 horizontally


    def deposit(self, n):
        if not self._capacity >= n + self._size:
            raise ValueError("Jar is full, Invalid deposit")
        
        self._size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Insufficient cookies")
        self._size -= n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
