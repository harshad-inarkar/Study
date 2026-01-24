import random

class RandomizedSet:

    def __init__(self):
        self.l = []
        self.il = {}
        

    def insert(self, val: int) -> bool:
        if val in self.il:
            return False
        
        self.il[val] = len(self.l)
        self.l.append(val)

        return True


    def remove(self, val: int) -> bool:
        if val not in self.il:
            return False
        
        last = self.l[-1]
        idx = self.il[val]

        self.l[idx] = last
        self.il[last] = idx

        self.l.pop()

        del self.il[val]

        return True

    def getRandom(self) -> int:
        return self.l[int(len(self.l) * random.random())]
    
# Example usage
if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))    # True
    print(obj.remove(2))    # False
    print(obj.insert(2))    # True
    print(obj.getRandom())  # Random element from [1,2]
    print(obj.remove(1))    # True
    print(obj.insert(2))    # False
    print(obj.getRandom())  # Random element from [2]
