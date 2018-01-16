def Bubblesort(list):
    a = True
    num = len(list)-1
    while num > 0 and a:
       a = False
       for i in range(num):
           if list[i]>list[i+1]:
               a = True
               temp = list[i]
               list[i] = list[i+1]
               list[i+1] = temp
       num = num-1

list=[20,30,40,90,50,60,70,80,100,110]
Bubblesort(list)
print(list)
