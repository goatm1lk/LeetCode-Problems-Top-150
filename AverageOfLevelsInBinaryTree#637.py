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
    #Create a queue in order to loop through the values from each level.
    queue = deque([root])
    #Create a dict to hold the resulting values from each level on the binary tree.
    output = {}
    #Counter to keep track of the levels.
    counter = 0
    #Loop through the queue in order to sort out the which values are on which level.
    while queue:
        print("Level", counter, ":", [node.val for node in queue])
        #Get the length of the current queue.
        level_size = len(queue)
        #Create an array to append to the output.
        level_nums = []
        #Loop through the level size
        for _ in range(level_size):
            #Pop the one node from the left of the queue.
            node = queue.popleft()
            #Append that node value to the array that is holding the numbers for this level.
            level_nums.append(node.val)
           #Now we want to add on the node to the left from this one.
            if node.left:
                queue.append(node.left)
            #and to the right aswell.
            if node.right:
                queue.append(node.right)
        #After looping through the queue size, and making a new queue if possible, add the level_nums array to our hash map.
        output[counter] = level_nums
        #Move the counter up one as we moving down a level.
        counter += 1
    results = {}
    #loop through the output to get all the averages of each level_nums array, in order to append to result array.
    for i in range(len(output)):
        Sum = sum(output[i])
        result = Sum / len(output[i])
        results[i + 1] = result
        
    return output, results
root = TreeNode(random.randint(0,10))
createRandomTree(3,root)

results = getAverageOfLevelsInBinaryTree(root)
print("Here is the Average of each level:", results[1])