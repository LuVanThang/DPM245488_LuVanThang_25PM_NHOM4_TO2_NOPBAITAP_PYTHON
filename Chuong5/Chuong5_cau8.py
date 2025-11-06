import os 
def lay_ten_file_day_du(duong_dan):
    ten_file = os.path.basename(duong_dan)
    return ten_file
def lay_ten_file_khong_duoi(duong_dan):
    ten_file = os.path.basename(duong_dan)
    ten_goc, phan_mo_rong = os.path.splitext(ten_file)
    return ten_goc
duong_dan_1 = r"d:\music\muabui.mp3"

print(f"Đường dẫn gốc: {duong_dan_1}")
print(f"Tên đầy đủ: {lay_ten_file_day_du(duong_dan_1)}")
print(f"Tên không đuôi: {lay_ten_file_khong_duoi(duong_dan_1)}")

print("---")

duong_dan_2 = r"C:\Users\Admin\Documents\Nhac\bai_hat.Phép.Màu.wav"

print(f"Đường dẫn gốc: {duong_dan_2}")
print(f"Tên đầy đủ: {lay_ten_file_day_du(duong_dan_2)}")
print(f"Tên không đuôi: {lay_ten_file_khong_duoi(duong_dan_2)}")