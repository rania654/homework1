import numpy as np
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]
array = np.array(list2)

print(list1*2)
#Doubles the list itself; so the list's contents is added at the end of the list
print(array*2)
#Doubles the contents of a list; there's also no commas

list3 = [1,2,3]
list4 = [4,5,6]
array2 = np.array([1,2,3])
array3 = np.array([4,5,6])

print(list3+list4)
#Appended right operand to left
print(array2+array3)
#Added right operand and left operand values together; no commas

array4 = np.arange(24)
print(array4.reshape(1,24))
print(array4.reshape(2,12))
print(array4.reshape(3,8))
print(array4.reshape(4,6))
print(array4.reshape(6,4))
print(array4.reshape(8,3))
print(array4.reshape(12,2))
print(array4.reshape(24,1))
