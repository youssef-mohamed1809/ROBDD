import boolean
from binarytree import Node
from sympy import * 
from sympy.logic.boolalg import truth_table
from sympy.abc import x,y,z
algebra = boolean.BooleanAlgebra()

function1 = algebra.parse(input("Input a boolean expression of 3 variables: "))

table = truth_table(function1, [x,y,z])
myList = [0]*8
i = 0

for t in table:
    myList[i] = ('{0} -> {1}'.format(*t))[13]
    i += 1

for i in range(8):
    if myList[i] == "F":
        myList[i] = 0
    else:
        myList[i] = 1

print(myList)
indexX =0
indexY = 0
indexZ = 0

for i in range(3):
    if str(function1.get_symbols()[i]) == "x":
        indexX = i
    elif str(function1.get_symbols()[i]) == "y":
        indexY = i
    elif str(function1.get_symbols()[i]) == "z":
        indexZ = i

root = Node(str(function1.get_symbols()[indexX]))
root.left = Node(str(function1.get_symbols()[indexY]))
root.right = Node(str(function1.get_symbols()[indexY]))
root.left.right = Node(str(function1.get_symbols()[indexZ]))
root.left.left = Node(str(function1.get_symbols()[indexZ]))
root.right.right = Node(str(function1.get_symbols()[indexZ]))
root.right.left = Node(str(function1.get_symbols()[indexZ]))

root.left.left.left = Node(myList[0])
root.left.left.right = Node(myList[1])
root.left.right.left = Node(myList[2])
root.left.right.right = Node(myList[3])
root.right.left.left = Node(myList[4])
root.right.left.right = Node(myList[5])
root.right.right.left = Node(myList[6])
root.right.right.right = Node(myList[7])

print(root)

##FIRST REDUCTION
if myList[0] == myList[1]:
    root.left.left = Node(myList[0])

if myList[2] == myList[3]:
    root.left.right = Node(myList[2])

if myList[4] == myList[5]:
    root.right.left = Node(myList[4])

if myList[6] == myList[7]:
    root.right.right = Node(myList[7])

print(root)
##SECOND REDUCTION

rightRemove = False
leftRemove = False

if str(root.left.right) == str(root.left.left):
    root.left.right = Node("")
    leftRemove = True

if str(root.right.left) == str(root.right.right):
    root.right.left = Node("")
    rightRemove = True
print(root)
###THIRD REDUCTION

if rightRemove:
    root.right = root.right.right

if leftRemove:
    root.left = root.left.left

if str(root.left) == str(root.right):
    root.left = Node("")

print(root)


###############################################################################################################

###SECOND BOOLEAN EXPRESSION

function2 = algebra.parse(input("Input a second boolean expression of 3 variables: "))



table = truth_table(function2, [x,y,z])
myList = [0]*8
i = 0

for t in table:
    myList[i] = ('{0} -> {1}'.format(*t))[13]
    i += 1

for i in range(8):
    if myList[i] == "F":
        myList[i] = 0
    else:
        myList[i] = 1

print(myList)

for i in range(3):
    if str(function2.get_symbols()[i]) == "x":
        indexX = i
    elif str(function2.get_symbols()[i]) == "y":
        indexY = i
    elif str(function2.get_symbols()[i]) == "z":
        indexZ = i


root2 = Node(str(function2.get_symbols()[indexX]))
root2.left = Node(str(function2.get_symbols()[indexY]))
root2.right = Node(str(function2.get_symbols()[indexY]))
root2.left.right = Node(str(function2.get_symbols()[indexZ]))
root2.left.left = Node(str(function2.get_symbols()[indexZ]))
root2.right.right = Node(str(function2.get_symbols()[indexZ]))
root2.right.left = Node(str(function2.get_symbols()[indexZ]))

root2.left.left.left = Node(myList[0])
root2.left.left.right = Node(myList[1])
root2.left.right.left = Node(myList[2])
root2.left.right.right = Node(myList[3])
root2.right.left.left = Node(myList[4])
root2.right.left.right = Node(myList[5])
root2.right.right.left = Node(myList[6])
root2.right.right.right = Node(myList[7])

print(root2)

##FIRST REDUCTION
if myList[0] == myList[1]:
    root2.left.left = Node(myList[0])

if myList[2] == myList[3]:
    root2.left.right = Node(myList[2])

if myList[4] == myList[5]:
    root2.right.left = Node(myList[4])

if myList[6] == myList[7]:
    root2.right.right = Node(myList[7])
print(root2)
##SECOND REDUCTION

rightRemove = False
leftRemove = False

if str(root2.left.right) == str(root2.left.left):
    root2.left.right = Node("")
    leftRemove = True

if str(root2.right.left) == str(root2.right.right):
    root2.right.left = Node("")
    rightRemove = True
print(root2)
###THIRD REDUCTION

if rightRemove:
    root2.right = root2.right.right

if leftRemove:
    root2.left = root2.left.left

if str(root2.left) == str(root2.right):
    root2.left = Node("")

print(root2)

##COMPARE EQUIVALENCE

if str(root) == str(root2):
    print("Both functions are equivalent")
else:
    print("Functions are not equivalent")