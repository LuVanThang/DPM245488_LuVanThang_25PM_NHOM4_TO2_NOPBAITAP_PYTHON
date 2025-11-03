import math 

print("--- Chương trình tính Logarit cơ số a của x (log_a(x)) ---")


a = float(input("Nhập cơ số a: "))
x = float(input("Nhập giá trị x: "))
while a<=0 or a==1 or x<=0:
    print("Cơ số a phải lớn hơn 0 và khác 1, x phải lớn hơn 0. Vui lòng nhập lại!")
    a = float(input("Nhập cơ số a: "))
    x = float(input("Nhập giá trị x: "))

if a > 0 and a != 1 and x > 0:
    ket_qua = math.log(x) / math.log(a)
    
    print(f"Log cơ số {a} của {x} là: {ket_qua}")
