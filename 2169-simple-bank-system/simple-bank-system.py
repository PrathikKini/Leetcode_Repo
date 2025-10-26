class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance

    def ok(self, a):
        return 1 <= a <= len(self.b)

    def transfer(self, a, c, m):
        if not (self.ok(a) and self.ok(c) and self.b[a-1] >= m):
            return False
        self.b[a-1] -= m
        self.b[c-1] += m
        return True

    def deposit(self, a, m):
        if not self.ok(a):
            return False
        self.b[a-1] += m
        return True
    
    def withdraw(self, a, m):
        if not (self.ok(a) and self.b[a-1] >= m):
            return False
        self.b[a-1] -= m
        return True