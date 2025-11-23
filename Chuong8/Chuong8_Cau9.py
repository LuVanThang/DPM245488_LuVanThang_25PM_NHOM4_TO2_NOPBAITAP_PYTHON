from tkinter import *
import tkinter.messagebox as msg
def phan_loai_bmi(bmi_score):
    """Phân loại tình trạng cân nặng dựa trên điểm BMI."""
    if bmi_score < 18.5:
        return "Gầy", "Thấp"
    elif 18.5 <= bmi_score <= 24.9:
        return "Bình thường", "Thấp"
    elif 25.0 <= bmi_score <= 29.9:
        return "Mập (Hơi Béo)", "Trung bình"
    else: 
        return "Béo phì", "Cao"

def tinh_bmi():
    try:
        chieu_cao = float(string_chieu_cao.get())
        can_nang = float(string_can_nang.get())

        if chieu_cao <= 0 or can_nang <= 0:
            msg.showerror("Lỗi", "Chiều cao và Cân nặng phải là số dương.")
            return
        bmi_score = can_nang / (chieu_cao ** 2)
        bmi_score_rounded = round(bmi_score, 2)

       
        tinh_trang, nguy_co = phan_loai_bmi(bmi_score)

    
        string_bmi.set(f"{bmi_score_rounded}")
        string_tinh_trang.set(tinh_trang)
        string_nguy_co.set(f"Nguy cơ: {nguy_co}")

    except ValueError:
        string_bmi.set("Lỗi")
        string_tinh_trang.set("")
        string_nguy_co.set("")
root = Tk()
root.title("Tính chỉ số BMI")
root.config(bg='yellow', padx=20, pady=20)


string_chieu_cao = StringVar()
string_can_nang = StringVar() 
string_bmi = StringVar()
string_tinh_trang = StringVar()
string_nguy_co = StringVar()

Label(root, text="Nhập chiều cao", bg='yellow', padx=5, pady=5).grid(row=0, column=0, sticky=W)
Entry(root, width=10, textvariable=string_chieu_cao, justify='center', font='Arial 10').grid(row=0, column=1, padx=5, pady=5)
Label(root, text="Nhập cân nặng", bg='yellow', padx=5, pady=5).grid(row=1, column=0, sticky=W)
Entry(root, width=10, textvariable=string_can_nang, justify='center', font='Arial 10').grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Tính BMI", command=tinh_bmi, bg='lightblue', fg='black', width=10).grid(row=2, column=0, columnspan=2, pady=10)
Label(root, text="BMI của bạn:", bg='yellow', padx=5, pady=5).grid(row=3, column=0, sticky=W)
Label(root, textvariable=string_bmi, bg='white', relief=SUNKEN, width=10).grid(row=3, column=1, padx=5, pady=5, sticky=W+E)
Label(root, text="Tình trạng của bạn", bg='yellow', padx=5, pady=5).grid(row=4, column=0, sticky=W)
Label(root, textvariable=string_tinh_trang, bg='white', relief=SUNKEN, width=10).grid(row=4, column=1, padx=5, pady=5, sticky=W+E)
Label(root, text="Nguy cơ\nphát triển bệnh", bg='yellow', padx=5, pady=5, justify=LEFT).grid(row=5, column=0, sticky=W)
Label(root, textvariable=string_nguy_co, bg='white', relief=SUNKEN, width=10).grid(row=5, column=1, padx=5, pady=5, sticky=W+E)
Button(root, text="Thoát", command=root.quit, bg='red', fg='white', width=10).grid(row=6, column=0, columnspan=2, pady=10)
root.mainloop()