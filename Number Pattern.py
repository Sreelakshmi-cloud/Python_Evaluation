rows = int(input("enter the number of rows"))
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()