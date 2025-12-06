#A
#A B C
#A B C D E
#A B C D E F G
#A B C D E F G H I

n=5
for i in range(1,n+1):
    for j in range(i*2-1):
        print(chr(65+j),end=" ")
    print()
    