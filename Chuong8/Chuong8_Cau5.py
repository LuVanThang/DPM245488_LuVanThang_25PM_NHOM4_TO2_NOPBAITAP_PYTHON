from tkinter import *
root=Tk()
root.title("Enter new password")
root.minsize(height=150,width=300)
oldpass=StringVar()
newpass=StringVar()
confirmpass=StringVar()
Label(root, text="Old Password:").grid(row=0, column=0, sticky='w', pady=5)
Entry(root, textvariable=oldpass, show='*').grid(row=0, column=1, padx=10, pady=5)
Label(root, text="New Password:").grid(row=1, column=0, sticky='w', pady=5)
Entry(root, textvariable=newpass, show='*').grid(row=1, column=1, padx=10, pady=5)
Label(root, text="Enter New Password Again:").grid(row=2, column=0, sticky='w', pady=5)
Entry(root, textvariable=confirmpass, show='*').grid(row=2, column=1, padx=10, pady=5)


button_frame = Frame(root, pady=10)
button_frame.grid(row=3, column=0, columnspan=2)
Button(button_frame, text="OK", width=10).pack(side=LEFT, padx=10)
Button(button_frame, text="Cancel", command=root.quit, width=10).pack(side=LEFT, padx=10)


root.mainloop()