print("Chuong trinh tinh a va b")
a=float(input("Nhap vao a: "))
b=float(input("Nhap vao b: "))
pheptoan=str(input("Nhap vao phep toan (+,-,*,/): "))
if(pheptoan=="+"):
    kq=a+b
elif(pheptoan=="-"):
    kq=a-b
elif(pheptoan=="*"):
    kq=a*b
elif(pheptoan=="/"):
    kq=a/b
else:
    print("Khong co phep toan tren trong chuong trinh!!")
if(kq!=0):
    print("Ket qua phep toan: ",kq)
