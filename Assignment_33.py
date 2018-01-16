list1=[20,10,30,55,50,60,70]
list1.append(80)
print "append object 80 in list",list1
list1.insert(3,100)
print "Insert ogject 100 at 4th position",list1
list1.sort()
print "list in the sorted order",list1
list1=sorted(list1, key=int, reverse=True)
print "list in the reverse order",list1
list1.pop()
list1.pop()
list1.pop()
print "Delete last 3 elements in list",list1
