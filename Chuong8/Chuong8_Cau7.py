from tkinter import *
def chuyen_doi_nam():
    try:
        nam_duong = int(entry_nam_duong.get())
        ds_can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
        ds_chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
        can = ds_can[nam_duong % 10]
        chi = ds_chi[nam_duong % 12]
        ket_qua = f"{can} {chi}"
        stringKQ.set(ket_qua)

    except ValueError:
        stringKQ.set("Loi cu phap")
root = Tk()
root.title("Chuyển đổi Dương - Âm")
root.minsize(height=150, width=350)
root.configure(bg="yellow") # Đặt màu nền vàng cho cửa sổ chính
stringKQ = StringVar()
Label(root, text="Nhập năm dương:", bg="yellow", font=("Arial", 12)).place(x=30, y=30)
entry_nam_duong = Entry(root, font=("Arial", 12), fg="red", width=15)
entry_nam_duong.place(x=180, y=30)
entry_nam_duong.focus() 
btn_chuyen = Button(root, text="Chuyển", bg="blue", fg="white", font=("Arial", 11), command=chuyen_doi_nam)
btn_chuyen.place(x=220, y=70, width=80, height=35)
Label(root, text="Năm âm lịch:", bg="yellow", font=("Arial", 12)).place(x=30, y=120)
Button(root, textvariable=stringKQ, font=("Arial", 12), fg="red", width=20).place(x=180, y=120)
root.mainloop()