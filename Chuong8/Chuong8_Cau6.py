from tkinter import *

# Danh sách các kiểu relief (nổi/chìm)
RELIEF_STYLES = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

def create_button_grid(root):
    for col, relief_style in enumerate(RELIEF_STYLES):
        Label(root, text=relief_style, padx=10, pady=5).grid(row=0, column=col + 1)
    for row_index in range(5):
        borderwidth_val = row_index 
        Label(root, text=f"borderwidth = {borderwidth_val}", padx=10, pady=5).grid(row=row_index + 1, column=0, sticky='w')
        for col_index, relief_style in enumerate(RELIEF_STYLES):
           Button(root,text=relief_style,relief=relief_style,borderwidth=borderwidth_val
                  ).grid(row=row_index + 1, column=col_index + 1, padx=5, pady=5)

root = Tk()
root.title("frame 2") 
create_button_grid(root)
root.mainloop()