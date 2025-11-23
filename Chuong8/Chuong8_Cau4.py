from tkinter import *


class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.expression = ""
        self.input_text = StringVar()
        input_frame = Frame(self.root)
        input_frame.pack(side=TOP, fill=BOTH)

        input_field = Entry(input_frame, font=('arial', 18, 'bold'), 
                               textvariable=self.input_text, width=50, 
                               bd=10, insertwidth=4, bg="white", justify='right')
        input_field.pack(ipady=10) 
        btns_frame = Frame(self.root)
        btns_frame.pack()
        btn_w = 8  # Chiều rộng
        btn_h = 2  # Chiều cao
        Button(btns_frame, text="1", width=btn_w, height=btn_h, command=lambda: self.btn_click(1)).grid(row=0, column=0, padx=1, pady=1)
        Button(btns_frame, text="2", width=btn_w, height=btn_h, command=lambda: self.btn_click(2)).grid(row=0, column=1, padx=1, pady=1)
        Button(btns_frame, text="3", width=btn_w, height=btn_h, command=lambda: self.btn_click(3)).grid(row=0, column=2, padx=1, pady=1)

        Button(btns_frame, text="4", width=btn_w, height=btn_h, command=lambda: self.btn_click(4)).grid(row=1, column=0, padx=1, pady=1)
        Button(btns_frame, text="5", width=btn_w, height=btn_h, command=lambda: self.btn_click(5)).grid(row=1, column=1, padx=1, pady=1)
        Button(btns_frame, text="6", width=btn_w, height=btn_h, command=lambda: self.btn_click(6)).grid(row=1, column=2, padx=1, pady=1)

        Button(btns_frame, text="7", width=btn_w, height=btn_h, command=lambda: self.btn_click(7)).grid(row=2, column=0, padx=1, pady=1)
        Button(btns_frame, text="8", width=btn_w, height=btn_h, command=lambda: self.btn_click(8)).grid(row=2, column=1, padx=1, pady=1)
        Button(btns_frame, text="9", width=btn_w, height=btn_h, command=lambda: self.btn_click(9)).grid(row=2, column=2, padx=1, pady=1)

        Button(btns_frame, text="-", width=btn_w, height=btn_h, command=lambda: self.btn_click("-")).grid(row=3, column=0, padx=1, pady=1)
        Button(btns_frame, text="0", width=btn_w, height=btn_h, command=lambda: self.btn_click(0)).grid(row=3, column=1, padx=1, pady=1)
        Button(btns_frame, text=".", width=btn_w, height=btn_h, command=lambda: self.btn_click(".")).grid(row=3, column=2, padx=1, pady=1)

        ops_frame = Frame(self.root)
        ops_frame.pack()
        
        op_w = 4
        op_h = 2

        Button(ops_frame, text="+", width=op_w, height=op_h, command=lambda: self.btn_click("+")).pack(side=LEFT, padx=1, pady=1)
        Button(ops_frame, text="-", width=op_w, height=op_h, command=lambda: self.btn_click("-")).pack(side=LEFT, padx=1, pady=1)
        Button(ops_frame, text="*", width=op_w, height=op_h, command=lambda: self.btn_click("*")).pack(side=LEFT, padx=1, pady=1)
        Button(ops_frame, text="/", width=op_w, height=op_h, command=lambda: self.btn_click("/")).pack(side=LEFT, padx=1, pady=1)
        Button(ops_frame, text="=", width=op_w, height=op_h, command=self.btn_equal).pack(side=LEFT, padx=1, pady=1)

        clr_frame = Frame(self.root)
        clr_frame.pack(fill=X, padx=10, pady=5)
        
        Button(clr_frame, text="Clr", height=2, command=self.btn_clear).pack(fill=X)


    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        try:
            result = str(eval(self.expression)) 
            self.input_text.set(result)
            self.expression = result # Lưu kết quả để tính tiếp
        except ZeroDivisionError:
            self.input_text.set("Lỗi chia 0")
            self.expression = ""
        except SyntaxError:
            self.input_text.set("Lỗi cú pháp")
            self.expression = ""
        except:
            self.input_text.set("Lỗi")
            self.expression = ""


root = Tk()
app = SimpleCalculator(root)
root.mainloop()