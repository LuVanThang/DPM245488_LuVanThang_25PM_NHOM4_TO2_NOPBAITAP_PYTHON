n=int(input("Nhap vao gia tri n: "))
arr=[]
temp=set()
while len(arr)<n:
    try:
        x=int(input(f"Nhập vào giá trị thứ {len(arr)+1}: "))
    except ValueError:
        print("Phải nhập vào số nguyên vui lòng nhập lại")
        continue
    if x in temp:
        print("Giá trị trùng lập vui lòng nhập lại")
    else:
        arr.append(x)
        temp.add(x)
print("Mảng số: ",arr)