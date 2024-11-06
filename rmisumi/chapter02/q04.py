#1
a=[4, 8, 3, 4, 1]
a=[x % 2 for x in a]
print(a)
#2
a=[4, 8, 3, 4, 1]
a=sum([x % 2 for x in a])
print(a)
#3
a=[4, 8, 3, 4, 1]
a=[x for x in a if x % 2 !=0]
print(a)
