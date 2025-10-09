ngay=int(input("Nhập ngày: "))
while(ngay>31):
    ngay=int(input("Nhập lại ngày: "))
thang=int(input("Nhập tháng: "))
while(thang>12):
    thang=int(input("Nhập lại tháng: "))
nam=int(input("Nhập năm: "))
ngayketiep=ngay+1
namke=nam
if thang in (1,3,5,7,8,10,12):
    if(ngayketiep<31): thangke=thang
    elif(ngayketiep>31):
        ngayketiep=1
        thangke=thang+1
elif thang in (4,6,9,11):
    if(ngayketiep<30): thangke=thang
    elif(ngayketiep>30):
        ngayketiep=1
        thangke=thang+1
elif thang==2:
    if((nam % 4 ==0 and nam % 100 != 0) or nam % 400==0):
        if(ngayketiep<29): thangke=thang
        elif(ngayketiep>29):
            ngayketiep=1
            thangke=thang+1
    else:
        if(ngayketiep<28): thangke=thang
        elif(ngayketiep>28):
            ngayketiep=1
            thangke=thang+1
if(thangke>12):
    thangke=1
    namke=nam+1
print("Ngày kế tiếp của ngày ",ngay,"/",thang,"/",nam,"là ngày ",ngayketiep,"/",thangke,"/",namke)



         