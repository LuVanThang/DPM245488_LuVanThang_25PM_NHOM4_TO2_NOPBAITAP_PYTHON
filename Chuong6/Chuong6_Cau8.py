n=int(input("Nhập vào n: "))
arr=[]
for i in range(n):
    x=float(input(f"Nhập vào số thứ {i+1}: "))
    arr.append(x)
giam_dan=sorted(arr,reverse=True)
print("Danh sách sau khi sắp xếp: ",giam_dan)