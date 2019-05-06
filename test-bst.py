#Test the class

#these are the "public" methods that can be tested
from bst import inOrder, put, remove, search, resetTree, preOrder, postOrder

put(20)
put(10)
put(05)
put(15)
put(30)
put(25)
put(35)
print('remove(5) removes and returns ' + str(remove(05)))

print(inOrder()) #this should print [5,10,15,20,25,30,35]


