list1=[1,2,3,4,5,6,7]
list2=[10,30,15,22,33,55,98]
list3=[101,440,222,333,121,435,296]
list4=[]
list5=[]
list1.sort()
list2.sort()
list3.sort()
a=list1[len(list1)-2]
b=max(list1)
list4.append(a)
list4.append(b)
a=list2[len(list2)-2]
b=max(list2)
list4.append(a)
list4.append(b)
a=list3[len(list3)-2]
b=max(list3)
list4.append(a)
list4.append(b)
print "new max list is",list4
print "Avg of max list is ",sum(list4) / len(list4)
a=list1[1]
b=min(list1)
list5.append(a)
list5.append(b)
a=list2[1]
b=min(list2)
list5.append(a)
list5.append(b)
a=list3[1]
b=min(list3)
list5.append(a)
list5.append(b)
print "new min list is",list5
print "Avg of max list is ",sum(list5) / len(list5)