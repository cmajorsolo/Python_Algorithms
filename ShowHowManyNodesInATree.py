class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def BST_Insertion(root, node):
    if root.value is None:
        root = node
    else:
        if root.value > node.value:
            if root.left is None:
                root.left = None
            else:
                BST_Insertion(root.left, node)

        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                BST_Insertion(root.right, node)

def printTree(rootNode):
    if rootNode is None:
        return ''
    elif rootNode.right is not None or rootNode.left is not None:
        return printTree(rootNode.right) + '  '+ str(rootNode.value) + '  '+printTree(rootNode.left)

r = Node(4)
#left
a = Node(2)
b = Node(1)
c = Node(3)
#right
d = Node(8)
e = Node(6)
f = Node(10)

BST_Insertion(r, a)
BST_Insertion(r, b)
BST_Insertion(r, c)
BST_Insertion(r, d)
BST_Insertion(r, e)
BST_Insertion(r, f)

printTree(r)