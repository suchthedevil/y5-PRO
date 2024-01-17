def histogram(t):
    n = max(t)
    for i in range(n):
        for k in range(len(t)):
            if i < n-t[k]:
                print(" ", end=" ")
            else: 
                print("*", end=" ")
        print()

    
histogram([5,4,3,2,1,1,2,3,4,5])