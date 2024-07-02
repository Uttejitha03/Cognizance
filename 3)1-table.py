lst = []
u = int(input("Enter num of rows : "))
print("Enter the roll num , name and marks respectively to output a data table")
for i in range(0, u):
    ele = [input(), input(),input()]
    lst.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for a in lst:
    for b in a:
        print(b,end=" "*10)
    print()
