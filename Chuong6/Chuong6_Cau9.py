
def so_nguyen_to(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("Mời nhập vào một dãy số tự nhiên, cách nhau bằng dấu cách.")
input_string = input("Nhập dãy số: ") 


try:
    mang_so = [int(so) for so in input_string.split()]
except ValueError:
    print("Lỗi: Bạn đã nhập ký tự không phải là số. Vui lòng chạy lại chương trình.")
    exit() 

print(f"Mảng bạn đã nhập: {mang_so}")

so_le = []
so_chan = []
cac_so_nguyen_to = []
khong_phai_nguyen_to = []

for so in mang_so:
    if so % 2 == 0:
        so_chan.append(so)
    else:
        so_le.append(so)
    
    if so_nguyen_to(so):
        cac_so_nguyen_to.append(so)
    else:
        khong_phai_nguyen_to.append(so)


print("KẾT QUẢ PHÂN LOẠI:")

print(f"Dòng 1 (Số lẻ): {so_le}, Tổng cộng có: {len(so_le)} số lẻ.")

print(f"Dòng 2 (Số chẵn): {so_chan}, Tổng cộng có: {len(so_chan)} số chẵn.")

print(f"Dòng 3 (Số nguyên tố): {cac_so_nguyen_to}")

print(f"Dòng 4 (Không phải số nguyên tố): {khong_phai_nguyen_to}")