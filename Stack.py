class stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return 0
        else:
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    test = stack()
    print(test.isEmpty())
    print(test.push(1))
    print(test.push('test'))
    # test.pop()
    print(test.size())
    print(test.peek())


