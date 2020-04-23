from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("PyCalculator")
#logic
def calc(key):
    global memory
    if key == "=":
#Allowed characters
        str1 = "-+0123456789.*/"
        if calcEntry.get()[0] not in str1:
            calcEntry.insert(END, "First symbol not a number")
            messagebox.showerror("Error!", "You entered not a number!")

        try:
            result = eval(calcEntry.get())
            calcEntry.insert(END, "=" + str(result))
        except:
            calcEntry.insert(END, "Error!")
            messagebox.showerror("Error!", "Verify the data is correct.")
    elif key == "C":
        calcEntry.delete(0, END)

    elif key == "-/+":
        if "=" in calcEntry.get():
            calcEntry.delete(0, END)
        try:
            if calcEntry.get()[0] == "-":
                calcEntry.delete(0)
            else:
                calcEntry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calcEntry.get():
            calcEntry.delete(0, END)
        calcEntry.insert(END, key)

    

# create button
buttonList = [
    "sqrt", "pow", "Backspace",
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C", "", ""
]

r = 1
c = 0

for i in buttonList:
    rel = ""
    cmd = lambda x = i: calc(x)
    ttk.Button(root, text = i, command = cmd).grid(row = r, column = c)
    c += 1
    if c > 3:
        c = 0
        r += 1

calcEntry = Entry(root, width = 50)
calcEntry.grid(row = 0, column = 0, columnspan = 5)

root.mainloop()