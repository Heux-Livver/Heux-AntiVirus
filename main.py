from pyamsi import Amsi
from tkinter.filedialog import askopenfilename
from customtkinter import *
from functools import cache

istr= """
Little Info:
If Risk Lvl = 0 its clean
If Risk Lvl = 1 no thread
If Risk Lvl = 16384 blocked by admin
If Risk Lvl = 20479 blocked by admin end
If Risk Lvl = 32768 file is considered malware
"""
app = CTk()
app.geometry("500x400")
app.title("Heux-AntiVirus")
set_appearance_mode("dark")

@cache
def scan():
    file_path = askopenfilename()
    result = Amsi.scan_file(file_path, debug=True)
    risklevel = f"Risk Level:{result["Risk Level"]}"
    rslt = result["Message"]
    resultlabel = CTkLabel(master=app, text=rslt, font=("Arial", 11.5), text_color="white", fg_color="purple", corner_radius=32)
    resultlabel.place(relx=0.5, rely= 0.5333, anchor="center")
    risklvlabel = CTkLabel(master=app, text=risklevel, font=("Arial", 11.5), text_color="white", fg_color="purple", corner_radius=32)
    risklvlabel.place(relx=0.5, rely= 0.4333, anchor="center")

scanbtn = CTkButton(master=app, text="Select and Scan File", corner_radius=32, fg_color="blue", hover_color="purple", command=scan)
scanbtn.place(relx=0.5, rely=0.2333, anchor="center")

info = CTkLabel(master=app, text=istr, font=("Italic", 13), text_color="white", fg_color="dark blue", corner_radius=128) 
info.place(relx=0.5, rely=0.655, anchor="center")

app.mainloop()
