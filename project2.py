#Project 2
#task 1
limit =int(input("Enter the range: "))
f1 =0
f2 =1
for f in range(0,limit):
    if f<=1:
        next=f
    else:
        next=f1+f2
        f1=f2
        f2=next
    print(next)
print()
#task 2
list1 =[12,-7,5,64,-14]
for num in list1:
    if num>=0:
        print(num,end=" ",)
print()
list2 =[12,14,-95,-6.7,3.3]
for n in list2:
    if n>=0:
        print(n,end=" ")