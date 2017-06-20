class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def BST_Insertion(root, node):
    if root.value is None:
        root = node
    else:
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                BST_Insertion(root.left, node)
        elif node.value > root.value:
            if root.right is None:
                root.right = node
            else:
                BST_Insertion(root.right, node)

# traverse the tree
def printTree(rootNode):
    if rootNode is None:
        return
    else:
        print(rootNode.value)
        printTree(rootNode.left)
        printTree(rootNode.right)

#breath first search
def breathPrint(node):
    if node is None:
        return
    queue = []
    queue.insert(0, node)
    while(len(queue) > 0):
        n = queue.pop()
        print(n.value)
        if n.left is not None:
            queue.insert(0, n.left)
        if n.right is not None:
            queue.insert(0, n.right)

def depthPrint(node):
    if node is None:
        return
    stack = []
    stack.append(node)
    while(len(stack) > 0):
        n = stack.pop()
        print(n.value)
        if n.right is not None:
            stack.append(n.right)
        if n.left is not None:
            stack.append(n.left)

def getNumberOfNodesAtKLevel(node, k):
    if node is None or k<1:
        return 0
    if k==1:
        return 1
    numberLeft = getNumberOfNodesAtKLevel(node.left, k-1)
    numberRight = getNumberOfNodesAtKLevel(node.right, k-1)
    return int(numberLeft + numberRight)

def getLeafNodeNumber(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    numberLeft = getLeafNodeNumber(node.left)
    numberRight = getLeafNodeNumber(node.right)
    return int(numberLeft + numberRight)



r = Node(4)
#left
a = Node(2)
b = Node(1)
c = Node(3)
#right
d = Node(8)
e = Node(6)
f = Node(10)
g = Node(11)

BST_Insertion(r, a)
BST_Insertion(r, b)
BST_Insertion(r, c)
BST_Insertion(r, d)
BST_Insertion(r, e)
BST_Insertion(r, f)
BST_Insertion(r, g)

#printTree(r)
#breathPrint(r)
depthPrint(r)
#print(getLeafNodeNumber(r))