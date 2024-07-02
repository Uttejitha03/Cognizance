 #Making the 1st array
k=[]
u=int(input("n.o of elements in an array:\n"))
print("Enter the elements 1st First array")
for i in range(0,u):
   l=int(input())
   k.append(l)
# Making the 2nd array
g=[]
#n=int(input("n.o of elements in an array:\n"))
print(("Enter the elements of 2nd array\n"))
for i in range(0,u):
    l=int(input())
    g.append(l)
 
print("The Array's are\n")
print(k)
print(g)

if k==g:
 print("\nTrue\n")
else:
 print("\nFalse\n")
