n = 4
print("\n--- Hình vuông rỗng ---")
for i in range(n): 
    for j in range(n): 
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ") 
    print() 
print("\n--- Tam giác vuông ---")
for i in range(n):  
    for j in range(n - 1 - i):
            print(" ", end=" ")  
    for k in range(i + 1):
            print("*", end=" ")       
    print()
print("\n--- Hinh chéo nhau ---")
for i in range(n*2):
    for j in range (n*2):
        if i==n-1 or (i==1 and j==1) or (i==0 and j==0) or(i==2 and j==2 and j==0):
             print("*", end=" ")  
        else:
                print(" ", end=" ") 
    print()