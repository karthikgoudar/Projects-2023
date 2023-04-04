'''
Binary Tree Traversal

Author : Karthik Goudar
Date   : 1 Mar, 2023

''' 

# Structure of binary tree: 
# 1. To represent nodes which contains data:
# 2. 2 links which points to left and right children along the data fields

# Binary tree class and its methods 
class BinaryTreeNode: 
    def __init__(self,data):
        self.data = data   #root node
        self.left = None   # left child
        self.right = None  # right child

    # set data
    def setData(self, data):
        self.data = data

    #get data
    def getData(self):
        return self.data

    # get left child of node
    def getLeft(self):
        return self.left
    
    #get right child of node
    def getRight(self):
        return self.right
    
# ---------------------------------------------------------------#

# BINARY TREE TREVERSAL OPERATIONS
    
'''
               1
          2        3
        4   5    6   7
    pre-order   = [1 2 4 5 3 6 7]
    in-order    = [4 2 5 1 6 3 7]
    post-order  = [4 5 2 6 7 3 1]
    level-order = [1 2 3 4 5 6 7]
'''
# ---------------------------------------------------------------#

# Pre order treversal (some info must be maintained while moving down the tree)
# first middle then left then right
# to go to right from left we must know the root of these two
# we can do that by implementing stacks

class BinaryTree:
    def __init__(self, root=None): 
        self.root = root

    def preOrder(self, root):
        if root == None:
            return 
        print(root.data, sep='-->', end='-->')
        self.preOrder(root.left)
        self.preOrder(root.right)
        
# Non-recursive preorder traversal

def preOrderIterative(self, root, result):
    if not root:
        return
    stack = []
    stack.append(root)

    while stack: 
        node  = stack.pop()
        result.append(node.data) 
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.data)
 
# ---------------------------------------------------------------#

# In order traversal
# Root is visited between the subtrees
# Traverse the right subtree in Inorder
# Visit the root
# Traverse the right subtree in Inorder

class BinaryTree:
    def __init__(self, root = None):
        self.root = root
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print(root.data, sep='-->', end='-->')
        self.inOrder(root.right)

# Non recursive inorder treversal

    def inOrderIterative(self, root, result):
        if not root:
            return
        
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right

# ---------------------------------------------------------------#

# Post oeder treversal
# Root is visited after both subtrees
# Traverse the left subtree
# Visit the root 

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def postOrder(self, root):
        if not root:
            return 
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, sep='-->', end='-->')

# Non recursive Postorder Traversal

# Each node is visited twice
# The node's values are appended to thr result in traversal order

    def postOrderIterative(root, result):
        if not root:
            return 
        visited = set()
        stack = []
        node = root 

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.left and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.data)
                    node = None


# ---------------------------------------------------------------#

# Level order treversal

# Visit the root
# While traversing level l, keep all the elements at level l+1 in queue
# Go to the next level and visit all the nodes in that level
# Repeat this until all the levels are compleated

# Implementation with Python module Queue

import queue

def levelOrder(root, result):
    if root is None:
        return 
    q = queue.Queue()
    q.put(root)       
    node = None

    while not q.empty():
        node = q.get()
        result.append(node.data)
 
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

# ---------------------------------------------------------------#
