
class Counter:

    def __init__(self, limit: int):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.limit:
            self.current = 0
            raise StopIteration
        
        self.current += 1
        return self.current


counter = Counter(5)

# it = iter(counter)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i in counter:
    print(i)

for i in counter:
    print(i)
