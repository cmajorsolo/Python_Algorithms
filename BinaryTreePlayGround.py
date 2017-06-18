class Node:
    def __init__(self, val):
        self.leftChild = None
        self.rightChild = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def insertNode(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.value):
            if(node.leftChild is not None):
                self._add(val, node.leftChild)
            else:
                node.leftChild = Node(val)
        else:
            if(node.rightChild is not None):
                self._add(val, node.rightChild)
            else:
                node.rightChild = Node(val)
    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.leftChild)
            print (str(node.value) + ' ')
            self._printTree(node.rightChild)

def testTree():
    tree = Tree()
    tree.insertNode(0)
    tree.insertNode(1)
    tree.insertNode(2)
    tree.insertNode(3)
    tree.insertNode(4)
    tree.insertNode(5)
    tree.printTree()

testTree()