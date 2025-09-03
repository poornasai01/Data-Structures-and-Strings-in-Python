list = [1,2,3,4,5,6,7,8,9,10]\

list1 = list[:5]
list2 = list1.copy()
list2.reverse()

print("Original list: ",list)
print("Extracted first five elements: ",list1)
print("Reversed extracted elements: ",list2)