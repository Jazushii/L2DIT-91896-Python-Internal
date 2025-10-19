import tkinter as tk
import random as rdm
import math
import datetime as dt
from tkinter.filedialog import asksaveasfilename

class Customer:
    def __init__(self, given_name, mid_name, last_name, itm_name, itm_num, return_day):
        self.reciept_num = rdm.randint(10000, 99999)
        self.given_name = given_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.full_name = f"{self.last_name}, {self.given_name} {self.mid_name}"
        self.itm_name = itm_name
        self.itm_num = itm_num
        self.itm_issued = dt.datetime.now()
        self.return_day = int(return_day)
        self.d = int(self.itm_issued.strftime("%d"))
        self.m = self.itm_issued.strftime("%m")
        self.m_int = int(self.itm_issued.strftime("%m"))
        self.y = int(self.itm_issued.year)
        if (self.d + self.return_day) <= int(month_list[self.m]):
            self.return_day = self.d + return_day
            self.return_month = self.m_int
        if (self.d + int(return_day)) >= int(month_list[self.m]):
            self.return_day = (self.d + return_day) - int(month_list[self.m])
            self.return_month = self.m_int + 1
        self.return_date = f"{self.return_day}/{self.return_month}/{self.y}"
    
month_list = {
    "1":int(31),
    "2":int(28),
    "3":int(31),
    "4":int(30),
    "5":int(31),
    "6":int(30),
    "7":int(31),
    "8":int(31),
    "9":int(30),
    "10":int(31),
    "11":int(30),
    "12":int(31),
}

q_list = [
    "What is your given name?",
    "What is your middle name/s?",
    "What is your last name?",
    "Pick an item:\n(If you want multiple items,\nwill need to submit another form)",
    "How many items are you issuing?",
    "How many days until items returned?",
]

ent_list = [
    "ent_given_name",
    "ent_mid_name",
    "ent_last_name",
    "ent_itm_name",
    "ent_itm_num",
    "ent_return_day",
]

input_list = [
    "given_name",
    "mid_name",
    "last_name",
    "itm_name",
    "itm_num",
    "return_day",
]

confirm_list = [
    "Given name:",
    "Middle name/s:",
    "Last name:",
    "Item:",
    "Amount:",
    "Days until returned:",
]

error_list = {}

has_error = False
def error():
    global has_error
    for e in range(6):
            frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
            frm_error.grid(row=e, column=3, padx=5, pady=5, sticky="we")
            lbl_error = tk.Label(frm_error, text="GOOD", fg='green')
            lbl_error.pack()
    for type, num in error_list.items():
        if type == f"blank{num}":
            frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
            frm_error.grid(row=num, column=3, padx=5, pady=5, sticky="we")
            lbl_error = tk.Label(frm_error, text="REQUIRED", fg='red')
            lbl_error.pack()
        if type == f"not_text{num}":
            frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
            frm_error.grid(row=num, column=3, padx=5, pady=5, sticky="we")
            lbl_error = tk.Label(frm_error, text="ONLY LETTERS", fg='red')
            lbl_error.pack()
        if type == f"not_num{num}":
            frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
            frm_error.grid(row=num, column=3, padx=5, pady=5, sticky="we")
            lbl_error = tk.Label(frm_error, text="ONLY NUMBERS", fg='red')
            lbl_error.pack()
        if type == f"num_boundary{num}":
            frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
            frm_error.grid(row=num, column=3, padx=5, pady=5, sticky="we")
            if num == 4:
                lbl_error = tk.Label(frm_error, text="BETWEEEN 1 & 500", fg='red')
            if num == 5:
                
                lbl_error = tk.Label(frm_error, text="CANNOT BE UNDER 0", fg='red')
            lbl_error.pack()
    has_error = False

def submit():
    print(f"{error_list}before")
    global has_error
    error_list.clear()
    for g in range(6):
        input_list[g] = ent_list[g].get()
    # takes the value of the entries
    b = 0
    for l in range(5):
        print(b)
        if input_list[b] == "":
            error_list.update({f"blank{b}":b})
            has_error = True
        if b == 0:
            b = 1
        b += 1
    # to check if the entries are blank
    c = 0
    for l in range(4):
        alpha = sum(a.isalpha() for a in input_list[c])
        space = sum(s.isspace() for s in input_list[c])
        sum_as = (alpha + space)
        if sum_as != len(input_list[c]):
            if input_list[c] != "":
                error_list.update({f"not_text{c}":c})
                has_error = True
        c += 1
    # to check if the entries have no numbers (except entry no. 5)
    n = 4
    for l in range(2):
        if input_list[n].isnumeric() == False:
            if input_list[n] != "":
                error_list.update({f"not_num{n}":n})
                has_error = True
        if input_list[n].isnumeric() == True:
            input_list[n] = int(input_list[n])
            if n == 4:
                if input_list[n] < 1 or input_list[n] > 500:
                    error_list.update({f"num_boundary{n}":n})
                    has_error = True
            if n == 5:
                if input_list[n] < 1:
                    error_list.update({f"num_boundary{n}":n})
                    has_error = True
        n += 1
    # to check if entry 4 is an integer
    print(f"{error_list}after")
    if has_error == True:
        error()
    else:
        for e in range(6):
            frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
            frm_error.grid(row=e, column=3, padx=5, pady=5, sticky="we")
            lbl_error = tk.Label(frm_error, text="GOOD", fg='green')
            lbl_error.pack()
        c = Customer(
            input_list[0],
            input_list[1],
            input_list[2],
            input_list[3],
            input_list[4],
            input_list[5],
        )
        confirm_window = tk.Tk()
        confirm_window.title('Confirm Window')

        for r in range(6):
            frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
            frm_confirm.grid(row=r, column=0, padx=5, pady=5, sticky="we")
            lbl_confirm = tk.Label(frm_confirm, text=confirm_list[r])
            lbl_confirm.pack()
            frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
            frm_confirm.grid(row=r, column=1, padx=5, pady=5, sticky="we")
            lbl_confirm = tk.Label(frm_confirm, text=input_list[r])
            lbl_confirm.pack()

        frm_confirm = tk.Frame(confirm_window, borderwidth=3)
        frm_confirm.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        btn_confirm = tk.Button(frm_confirm, text="Cancel", width=10)
        btn_confirm.pack()
        frm_confirm = tk.Frame(confirm_window, borderwidth=3)
        frm_confirm.grid(row=7, column=1, padx=5, pady=5, sticky="e")
        btn_confirm = tk.Button(frm_confirm, text="Confirm", width=10)
        btn_confirm.pack()

        confirm_window.mainloop()

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        given_name = input_list[0]
        output_file.write(given_name)
    form_window.title(f"Simple Text Editor - {filepath}")

form_window = tk.Tk()
# assigns the variable "form_window" to a window
form_window.title('Form Window')
# adds a title to the window
window_width = 470
window_height = 290
# setting up variables
screen_width = form_window.winfo_screenwidth()
screen_height = form_window.winfo_screenheight()
# gets the screen's dimensions
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
# finds the center point of the screen
form_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# set the position of the window to the center of the screen'
form_window.resizable(False, False)
# does not allow to resize the window
    
for r in range(6):
    frm_q = tk.Frame(form_window, relief=tk.RIDGE, borderwidth=3)
    # assigns the variable "frm_q" (frame_question) as the frame to put the labels in
    # its "master" is form_window
    # its relief (border style) is set to ridged
    # its borderwidth is set to 3
    frm_q.grid(row=r, column=0, padx=20, pady=5, sticky="w")
    # puts frm_q into a grid
    # where its located in row "r", which is in the q_list list
    # and in column 0 (the first column)
    # with x and y padding to 5
    # and sticks to "w" (west / left side)
    lbl_q = tk.Label(frm_q, text=q_list[r])
    # its text is q_list[r], takes the corresponding variable from the list as text
    lbl_q.pack()
    # runs lbl_q

    frm_ent = tk.Frame(form_window, relief=tk.SUNKEN, borderwidth=3)
    frm_ent.grid(row=r, column=1, padx=5, pady=5, sticky="we")
    ent_list[r] = tk.Entry(frm_ent, width=15)
    ent_list[r].pack()

    frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
    frm_error.grid(row=r, column=3, padx=5, pady=5, sticky="we")
    if r == 1:
        lbl_error = tk.Label(frm_error, text="NOT REQUIRED")
    else:
        lbl_error = tk.Label(frm_error, text="REQUIRED", fg='red')
    lbl_error.pack()

frm_btn = tk.Frame(form_window, borderwidth=3)
frm_btn.grid(row=7, column=1, padx=5, pady=5, sticky="e")
btn_next = tk.Button(frm_btn, text="Sumbit", width=10, command=submit)
btn_next.pack()

form_window.mainloop()
# runs and loops the form window