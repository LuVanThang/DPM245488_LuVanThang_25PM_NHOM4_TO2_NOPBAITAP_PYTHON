from math import sqrt
print("Chương trình tính đọ dài đoạn AB")
x1=float(input("Nhập hoành độ điểm A: "))
y1=float(input("Nhập tung độ điểm A: "))
x2=float(input("Nhập hoành độ điểm B: "))
y2=float(input("Nhập tung độ điểm B: "))
d=sqrt((x2-x1)**2+(y2-y1)**2)
print("Độ dài đoạn AB là: ",d)