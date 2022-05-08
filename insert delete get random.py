import random


class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.s = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.s)
        self.s.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        ind = self.d[val]
        self.s[ind] = self.s[-1]
        self.d[self.s[-1]] = ind
        self.s.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.s)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
