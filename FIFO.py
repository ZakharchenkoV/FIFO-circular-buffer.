class Dogs:
    def __init__(self):
        self.breed = []

    def isEmpty(self):
        return self.breed == []

    def inQueue(self, item):
        self.breed.insert(0, item)

    def outQueue(self):
        return self.breed.pop()

    def size(self):
        return len(self.breed)

    def printQueue(self):
        for items in self.breed:
            print(items, ',', end=' ', sep ='')


q = Dogs()
print(q.isEmpty())

q.inQueue('English setter')

q.inQueue('Boxer')

q.inQueue('Bulldog')

print(q.isEmpty())

q.printQueue()

print('\nSize =', q.size())

q.outQueue()

q.printQueue()