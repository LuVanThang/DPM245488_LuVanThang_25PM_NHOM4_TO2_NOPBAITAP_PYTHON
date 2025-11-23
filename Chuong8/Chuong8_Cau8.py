from tkinter import *
def chuyen_doi():
    try:
        do_f = float(string_F.get())
        do_c = (do_f - 32) * 5 / 9
        ket_qua = f"{do_c:.2f} °C"
        string_C.set(ket_qua)

    except ValueError:
        string_C.set("Loi cu phap") 


root = Tk()
root.title("Chuyển đổi F sang C")
root.minsize(width=300, height=150)
root.config(bg='yellow', padx=15, pady=15) 

string_F = StringVar(value="350")
string_C = StringVar(value="Độ C ở đây") 

Label(root, text="Nhập độ F", bg='yellow', padx=5, pady=5).grid(row=0, column=0, sticky=W)
Entry(root, width=10, textvariable=string_F, justify='center', font='Arial 12 bold').grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Chuyển", command=chuyen_doi, bg='blue', fg='white', width=8, font='Arial 10').grid(row=1, column=1, padx=5, pady=5, sticky=E)
Label(root, text="Độ C", bg='yellow', padx=5, pady=5).grid(row=2, column=0, sticky=W)
Label(root, textvariable=string_C, bg='yellow', padx=5, pady=5, font='Arial 10 italic').grid(row=2, column=1, sticky=W)
root.mainloop()