# Python program to print level order traversal using Queue

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
#=========================================================================================================
# Iterative Method to print the height of binary tree
def InOrderTraversal(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []



    while(len(queue) > 0):




#====================================================================================
#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Inorder traversal of binary tree is -"
InOrderTraversal(root)
#This code is contributed by Nikhil Kumar Singh(nickzuck_007)