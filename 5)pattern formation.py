print("Print equilateral triangle Pyramid using * symbol ")
# printing full Triangle pyramid using *
size = 5
u = (2 * size) - 2
for i in range(0, size):
    for k in range(0, u):
        print(end=" ")
    # decrementing u after each loop
    u = u - 1
    for k in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
