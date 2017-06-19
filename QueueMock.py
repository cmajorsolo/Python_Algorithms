class queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    test=queue()
    print(test.isEmpty())
    test.enqueue(1)
    test.enqueue('test')
    print(test.dequeue())
    print(test.size())
