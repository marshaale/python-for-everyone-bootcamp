class Counter:
    def __init__(self):
        self.count = 0
    
    def bump(self):
        self.count += 1

counter = Counter()
counter.bump()
counter.bump()
counter.bump()
print("Count:",counter.count)