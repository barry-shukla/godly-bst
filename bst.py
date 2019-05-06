#This is the Node class that will store all the properties of an individual node including it's key, children, parents, and abilities to change these.
#They key is the unique ID of a node and cannot be changed
class Node:
	#constructor sets right left and parent to NoneTypes
    def __init__(self, key, right = None, left = None, parent = None):
        self.key = key
    	self.left = left
    	self.right = right
    	self.parent = parent

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def getKey(self):
		return int(self.key)

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setParent(self, parent):
        self.parent = parent
	
#root of the Tree
root = None

#PUBLIC METHODS!!! These functions are O(1) efficient :)

#First three functions are self explainatory
def put(key):
    newNode = Node(key)
    return insert(root, newNode).getKey()

def remove(key):
    return obliterate(key).getKey()

def search(key):
    return forage(key, root)

def resetTree(root):
	annhiliate()

#Traverse
def inOrder():
	return recursiveInOrder(root)

def preOrder():
	return recursivePreOrder(root)

def postOrder():
	return recursivePostOrder(root)

#PRIVATE METHODS!!!

#These are the recursive traversal methods
def recursiveInOrder(node):
	if(node != None):
		recursiveInOrder(node.getLeft())
		print(node.getKey())
		recursiveInOrder(node.getRight())

def recursivePreOrder(node):
	if(node != None):
		print(node.getKey())
		recursiveInOrder(node.getLeft())
		recursiveInOrder(node.getRight())

def recursivePostOrder(node):
	if(node != None):
		recursiveInOrder(node.getLeft())
		recursiveInOrder(node.getRight())
		print(node.getKey())

def forage(key, z):
	#if node doesn't exist in tree, return NoneType
	if(z == None):
		return None

	#if node exists, returns it
	elif(z.getKey() == key):
		return z

	#uses ternary to return node to left or right depending on if key is greater/less than current node's key
	else:
		return forage(key, z.getLeft()) if z.getKey() > key else forage(key, z.getRight())

def insert(z, newNode):
	current = None

	#If tree is empty, creates new root and returns it
	global root
	if(root == None):
		root = newNode
		return root
	
	#traverses tree by iterating the whole list, until it reaches the leaves
	while(z != None):
		current = z
		if(newNode.getKey() < z.getKey()):
			z = z.getLeft()
		else:
			 z = z.getRight()
	
	#if node's key is greater than current node's key or less than, inserts it there
	if(newNode.getKey() < current.getKey()):
		current.setLeft(newNode)
		newNode.setParent(current)
	else:
		current.setRight(newNode)
		newNode.setParent(current)

	return newNode

#destroys a node
def obliterate(key): 
	node = forage(key, root)
	if(node == None):
		return None

	PP = node.getParent()
	#--Case 1: node has no children--
	if(node.getLeft() == None and node.getRight() == None):
		if(PP.getLeft() == node):
			PP.setLeft(None)
		else:
			PP.setRight(None)

	#--Case 2: Node has one child--
	#Node has a left child
	elif(node.getLeft() != None and node.getRight() == None):
		if(PP.getLeft() == node):
			PP.setLeft(node.getLeft())
		else:
			#if node's left is not e
			PP.setRight(node.getLeft())

	#Node has a right child
	elif(node.getRight() != None and node.getLeft() == None):
		if(PP.getLeft() == node):
			PP.setLeft(node.getRight())
		else:
			PP.setRight(node.getRight())

	#--Case 3: Node has two children--
	else:
		current = node
		while(current != None):
			current = current.getLeft()
		#current is left most key
		node = current
		current = current.getRight()
	return node

#destroys all nodes, wipes/resets BST
def annhiliate():
	global root
	while(root != None):
		remove(root.getKey())

#godly BST
