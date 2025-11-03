print("Đọc số ra dạng chữ")
n=int(input("Vui lòng nhập vào số có tối đa 2 chữ số: "))
while(n>99):
    n=int(input("Vui lòng nhập lại số có tối đa 2 chữ số: "))
a=int(n/10)
if (a==1) : chuc="Mười"
elif (a==2) : 
    chuc="Hai mươi"
elif (a==3) : 
    chuc="Ba mươi"
elif (a==4) : 
    chuc="Bốn mươi"
elif (a==5) : 
    chuc="Năm mươi"
elif (a==6) : 
    chuc="Sáu mươi"
elif (a==7) :
    chuc="Bảy mươi"
elif (a==8) : 
    chuc="Tám mươi"
elif (a==9) : 
    chuc="Chín mươi"
b=int(n%10)
if(b==1): donvi=" mốt"
elif(b==2): donvi=" hai"
elif(b==3): donvi=" ba"
elif(b==4): donvi=" bốn"
elif(b==5): donvi=" năm"
elif(b==6): donvi=" sáu"
elif(b==7): donvi=" bảy"
elif(b==8): donvi=" tám"
elif(b==9): donvi=" chín"
if(a>0 and b>0):
    print("Số ",n," đọc ra dạng chữ là ",chuc,donvi)
if(a<=0 and b>0):
    print("Số ",n," đọc ra dạng chữ là ",donvi)
if(a>0 and b<=0):
    print("Số ",n," đọc ra dạng chữ là ",chuc)
