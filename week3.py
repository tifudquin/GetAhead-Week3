class Tree:
    def __init__(self, value):
        self.children = []
        self.value = value

    def addNode(self, val):
    	self.children.append(Tree(val))

def traverseTree(firstParent, root, length, results, maxParent):

    for child in root.children:

    	# If the current node is the root node of the original tree
        if root.value == firstParent:
            maxParent[0] = firstParent # Reset the max parent of the subtree to root node
            results[0] = 0 # Reset the longest consecutive path of subtree

        if child.value == None: 
            return 0 # End recursion

        # Increase length
        elif child.value == root.value + 1:

            if maxParent[0] + 1 == root.value:
                length = results[0]
            length += 1

        else:
            length = 1


        if results[0] <= length:
            maxParent[0] = root.value # Update the max parent of the subtree

        # Update the longest consecutive path of the subtree
        results[0] = max(results[0], length)

        # Update the longest consecutive path of the whole tree
        results[1] = max(results[1], results[0])

        # Go through the subtree recursively
        traverseTree(firstParent, child, length, results, maxParent)


# Method that counts the longest consecutive path in a tree
def longestConsecutivePath(root): 
    if root == None:  
        return 0

    # [longest path of subtree, longest path of whole tree]
    results = [0, 0]

    # Max parent of the subtree
    maxParent = [0]

    # Current length of consecutive path
    length = 0

    # Root node of the whole tree
    firstParent = root.value

    traverseTree(firstParent, root, length, results, maxParent)  

    return results[1]


# Driver code
if __name__ == '__main__': 
    root = Tree(1)

    root.addNode(100)
    root.addNode(20)
    root.addNode(2)

    root.children[1].addNode(21)

    root.children[1].children[0].addNode(22)

    root.children[2].addNode(60)
    root.children[2].addNode(61)
    root.children[2].addNode(3)

    root.children[2].children[2].addNode(4)

    print(longestConsecutivePath(root))