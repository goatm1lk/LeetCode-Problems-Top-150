#1. We must deque the binary tree in order to bfs over it. An output array is also needed
#2. Loop through the queue. For every iteration you would want to find the level size, and create an array of the numbers on that level of the binary tree.
#3. In this loop we would want to create a for loop for the level size(which is the size of the queue) and for each iteration we must assign a node variable to the value on the leftside of the queue.
#4. Following that we want to check for left and right nodes to append to the queue, so we can visit them eventually.
from collections import deque
import random
class TreeNode:
    def __init__(self,val = 0,left= None, right = None):
        self.val = val 
        self.left = left
        self.right = right
    
def createRandomTree(length,root):
    if length == 0:
        return
    root.left = TreeNode(random.randint(0,10))
    createRandomTree(length - 1, root.left)

    root.right = TreeNode(random.randint(0,10))
    createRandomTree(length - 1,root.right)

def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val)
    printInOrder(root.right)
    
def getAverageOfLevelsInBinaryTree(root):
    queue = deque([root])
    output = {}
    counter = 0
    #BFS thru the queue
    while queue:
        level_size = len(queue)
        level_nums = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nums.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output[counter] = level_nums
        counter += 1
    
    results = {}
    
    for i in range(len(output)):
        Sum = sum(output[i])
        result = Sum / len(output[i])
        results[i + 1] = result
    return output, results
root = TreeNode(random.randint(0,10))
createRandomTree(3,root)

results = getAverageOfLevelsInBinaryTree(root)
print("Here is each level of the Binary Tree: ",results[0], "Here is the Average of each level:", results[1])