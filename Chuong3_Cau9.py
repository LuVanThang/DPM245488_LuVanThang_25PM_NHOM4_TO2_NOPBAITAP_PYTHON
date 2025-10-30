print("Tim quy cua thang")
thang=int(input("Nhap vao thang can tim: "))
if(thang>=1 and thang<=3):
    print("Thang ",thang," thuoc quy 1")
elif(thang>=4 and thang<=6):
    print("Thang ",thang," thuoc quy 2")
elif(thang>=7 and thang<=9):
    print("Thang ",thang," thuoc quy 3")
elif(thang>=10 and thang<=12):
    print("Thang ",thang," thuoc quy 4")    
else:
    print("Khong co thang ",thang," trong nam")