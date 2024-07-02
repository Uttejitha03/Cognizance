m=int(input("start with the n.o\n"))
n=int(input("stop with the n.o\n"))
o=""
p=".  0.  0.  0.  0.  0. "
for i in range(m,n):
 o=o+str(i)+p
print(o + str(n))
