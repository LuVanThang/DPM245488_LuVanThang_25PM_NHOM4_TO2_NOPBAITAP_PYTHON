def tinh_tong_uoc_so(n):
    tong = 0
    for i in range(1, n // 2 + 1):
       
        if n % i == 0:
            tong += i            
    return tong

def kiem_tra_so_hoan_thien(n):
    tong_uoc = tinh_tong_uoc_so(n)
    if tong_uoc == n:
        return True
    else:
        return False

def kiem_tra_so_thinh_vuong(n):
    tong_uoc = tinh_tong_uoc_so(n)
    if tong_uoc > n:
        return True
    else:
        return False

n = int(input("Nhập một số nguyên dương n: "))

while n <= 0:
    print("Vui lòng nhập số lớn hơn 0.")
    n = int(input("Nhập lại một số nguyên dương n: "))
print(f"\n--- Kiểm tra số {n} ---")
print(f"Tổng các ước số của {n} (không kể {n}) là:", tinh_tong_uoc_so(n))
print("\nTổng các ước số của {0} (không kể {0}) là: {1}".format(n, tinh_tong_uoc_so(n)))    
if kiem_tra_so_hoan_thien(n):
    print(f"{n} LÀ số hoàn thiện.")
else:
    print(f"{n} KHÔNG PHẢI là số hoàn thiện.")
if kiem_tra_so_thinh_vuong(n):
    print(f"{n} LÀ số thịnh vượng.")
else:
    print(f"{n} KHÔNG PHẢI là số thịnh vượng.")