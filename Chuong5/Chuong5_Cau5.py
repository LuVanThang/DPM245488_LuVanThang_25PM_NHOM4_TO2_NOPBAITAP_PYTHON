def phan_tich_chuoi(s):
    hoa_count = 0
    thuong_count = 0
    so_count = 0
    kytudb_count = 0
    khoang_trang_count = 0
    nguyenam_count = 0
    phuam_count = 0
    NGUYEN_AM = "aeiouyáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"
    for char in s:
        if char.isalpha(): 
            if char.lower() in NGUYEN_AM:
                nguyenam_count += 1
            else:
                phuam_count += 1
            if char.isupper():
                hoa_count += 1
            else:
                thuong_count += 1
        elif char.isdigit():
            so_count += 1
        elif char.isspace():
            khoang_trang_count += 1
        else:
            kytudb_count += 1
    print("\n--- KẾT QUẢ PHÂN TÍCH CHUỖI ---")
    print(f"Chuỗi của bạn dài: {len(s)} ký tự")
    print(f"\nSố lượng chữ IN HOA:     {hoa_count}")
    print(f"Số lượng chữ in thường:  {thuong_count}")
    print(f"Số lượng chữ số:        {so_count}")
    print(f"Số lượng khoảng trắng:    {khoang_trang_count}")
    print(f"Số lượng ký tự đặc biệt: {kytudb_count}")
    print(f"\nTổng số Nguyên âm: {nguyenam_count} (trong số các chữ cái)")
    print(f"Tổng số Phụ âm:   {phuam_count} (trong số các chữ cái)")
    print("---------------------------------")

def main():
    chuoi_nhap = input("Nhập vào một chuỗi để phân tích: ")
    phan_tich_chuoi(chuoi_nhap)
while True:
    main()
    print("Tiếp không?(c/k):")
    s = input()
    if s=="k":
        break
print("Chương trình kết thúc")