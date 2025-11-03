from math import sqrt
print("Chương trình tính diện tích Tam Giác")
a=float(input("Nhập cạnh a>0: "))
b=float(input("Nhập cạnh b>0: "))
c=float(input("Nhập cạnh c>0: "))
while(a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or (b+c)<=a:
    print("Tam giác không hợp lệ vui long nhập lại!!!")
    a=float(input("Nhập cạnh a>0: "))
    b=float(input("Nhập cạnh b>0: "))
    c=float(input("Nhập cạnh c>0: "))
else:
    cv=a+b+c
    p=cv/2
    dt=sqrt(p*(p-a)*(p-b)*(p-c))
    print("Chu vi tam giác là: ",cv)
    print("Diện tích tam giác là: ",dt)