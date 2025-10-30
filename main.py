import tkinter as tk
import random as rdm
import datetime as dt
import os

class Customer:
    def __init__(self, given_name, mid_name, last_name, itm_name, itm_num, return_day):
        self.receipt_num = rdm.randint(10000, 99999)
        self.given_name = given_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.full_name = f"{self.last_name}, {self.given_name} {self.mid_name}"
        self.itm_name = itm_name
        self.itm_num = itm_num
        self.itm_issued = dt.datetime.now()
        # takes the date and time now
        self.return_day = int(return_day)
        self.d = int(self.itm_issued.strftime("%d"))
        self.m = self.itm_issued.strftime("%m")
        self.m_int = int(self.itm_issued.strftime("%m"))
        self.y = int(self.itm_issued.year)
        if (self.d + self.return_day) <= int(month_list[self.m]):
            self.return_day = self.d + return_day
            self.return_month = self.m_int
        if (self.d + int(return_day)) >= int(month_list[self.m]):
        # if the number of days exceeds the days in a month (ex. 34 days in October with 31 days)
            self.return_day = (self.d + return_day) - int(month_list[self.m])
            # subtracts that number with the number of days in the month
            self.return_month = self.m_int + 1
            # moves one month up
        self.return_date = f"{self.return_day}/{self.return_month}/{self.y}"
        self.issue_date = f"{self.d}/{self.m}/{self.y}"
    
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
    "Type an item:\n(If you want multiple items,\nwill need to submit another form)",
    "How many items are you issuing?",
    "How many days until items are returned?",
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
# creates an empty dictionary to be used later

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
        # checks if the type is blank{num}, if so, executes the following command
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
                
                lbl_error = tk.Label(frm_error, text="CANNOT BE UNDER 1", fg='red')
            lbl_error.pack()
    has_error = False

def submit():
    global has_error
    global confirm_window
    global lbl_status
    global Cust
    error_list.clear()
    for g in range(6):
        input_list[g] = ent_list[g].get()
    # takes the value of the entries
    b = 0
    for l in range(5):
        if input_list[b] == "":
            error_list.update({f"blank{b}":b})
            # adds the following to the dictionary
            has_error = True
            # enables "has_error" as true
        if b == 0:
            b = 1
            # skips row 1 in the loop
        b += 1
    # to check if the entries are blank
    ac = 0
    for l in range(4):
        alpha = sum(a.isalpha() for a in input_list[ac])
        # counts all the alpha symbols in the entry (letters)
        space = sum(s.isspace() for s in input_list[ac])
        # counts all the spaces in the entry
        sum_as = (alpha + space)
        # sums them up
        if sum_as != len(input_list[ac]):
        # if sum of alpha symbols and spaces is not
        # the same as the counted symbols in the text
        # executes code below
            if input_list[ac] != "":
                error_list.update({f"not_text{ac}":ac})
                has_error = True
        ac += 1
    # to check if the entries have no numbers (except entry no. 5)
    n = 4
    for l in range(2):
        if input_list[n].isnumeric() == False:
        # checks if there is a number in the entry, if not, executes the following code
            if input_list[n] != "":
                error_list.update({f"not_num{n}":n})
                has_error = True
        if input_list[n].isnumeric() == True:
        # checks if there is a number in the entry, if so, executes the following code
            input_list[n] = int(input_list[n])
            # makes the entry an integer so it'll work with operations
            if n == 4:
                if input_list[n] < 1 or input_list[n] > 500:
                # boundary checking
                    error_list.update({f"num_boundary{n}":n})
                    has_error = True
            if n == 5:
                if input_list[n] < 1:
                # boundary checking
                    error_list.update({f"num_boundary{n}":n})
                    has_error = True
        n += 1
    # to check if entry 4 and 5 is an integer
    if has_error == True:
        error()
    else:
        for e in range(6):
            frm_error = tk.Frame(form_window, relief=tk.RAISED, borderwidth=3)
            frm_error.grid(row=e, column=3, padx=5, pady=5, sticky="we")
            lbl_error = tk.Label(frm_error, text="GOOD", fg='green')
            lbl_error.pack()
        Cust = Customer(
            input_list[0],
            input_list[1],
            input_list[2],
            input_list[3],
            input_list[4],
            input_list[5],
        )
        # assigns "Cust" with the Customer class with these attributes
        confirm_window = tk.Tk()
        confirm_window.title('Confirm Window')

        frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
        frm_confirm.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        lbl_confirm = tk.Label(frm_confirm, text="Reciept Number:")
        lbl_confirm.pack()
        frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
        frm_confirm.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        lbl_confirm = tk.Label(frm_confirm, text=Cust.receipt_num)
        lbl_confirm.pack()
        for r in range(6):
            frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
            frm_confirm.grid(row=r+1, column=0, padx=5, pady=5, sticky="we")
            lbl_confirm = tk.Label(frm_confirm, text=confirm_list[r])
            lbl_confirm.pack()
            frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
            frm_confirm.grid(row=r+1, column=1, padx=5, pady=5, sticky="we")
            lbl_confirm = tk.Label(frm_confirm, text=input_list[r])
            lbl_confirm.pack()
        frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
        frm_confirm.grid(row=7, column=0, padx=5, pady=5, sticky="we")
        lbl_confirm = tk.Label(frm_confirm, text="Item Issued:")
        lbl_confirm.pack()
        frm_confirm = tk.Frame(confirm_window, relief=tk.RIDGE, borderwidth=3)
        frm_confirm.grid(row=7, column=1, padx=5, pady=5, sticky="we")
        lbl_confirm = tk.Label(frm_confirm, text=Cust.issue_date)
        lbl_confirm.pack()

        frm_confirm = tk.Frame(confirm_window, borderwidth=3)
        frm_confirm.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        btn_confirm = tk.Button(frm_confirm, text="Cancel", width=10, command=cancel)
        btn_confirm.pack()
        frm_confirm = tk.Frame(confirm_window, borderwidth=3)
        frm_confirm.grid(row=8, column=1, padx=5, pady=5, sticky="e")
        btn_confirm = tk.Button(frm_confirm, text="Confirm", width=10, command=save_file)
        btn_confirm.pack()

        frm_status = tk.Frame(confirm_window)
        frm_status.grid(row=9, column=0, padx=5, pady=5, sticky="we")
        lbl_status = tk.Label(frm_status, text="")
        lbl_status.pack()

        confirm_window.mainloop()

def cancel():
    global confirm_window
    confirm_window.destroy()
    # destroys the window (closes)

def save_file():
    global lbl_status
    global Cust
    # Save the current file as a new file
    filepath = f"{Cust.receipt_num}.txt"
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as output_file:
        text = f"{Cust.receipt_num}\n{input_list[0]}\n{input_list[1]}\n{input_list[2]}\n{input_list[3]}\n{input_list[4]}\n{input_list[5]}\n{Cust.issue_date}"
        output_file.write(text)
        lbl_status.config(text=f"File saved: {filepath}")
    form_window.title(f"Party Hire - {filepath}")

def del_file(del_file):
    os.remove(del_file)

def file_info(file):
    info_window = tk.Tk()
    info_window.title(f"{file} Info")
    filepath = file
    if not filepath:
        return
    with open(filepath, "r", encoding="utf-8") as open_file:
        line = open_file.read()
        frm_info = tk.Frame(info_window, relief=tk.RIDGE, borderwidth=3)
        frm_info.grid(row=0, column=0, padx=10, pady=5, sticky="we")
        lbl_info = tk.Label(frm_info, text=line)
        lbl_info.pack()
        frm_delete = tk.Frame(info_window, relief=tk.RIDGE, borderwidth=3)
        frm_delete.grid(row=0, column=0, padx=10, pady=5, sticky="we")
        btn_delete = tk.Label(frm_delete, text="Delete?", command=del_file(file))
        btn_delete.pack()

    info_window.mainloop()

form_window = tk.Tk()
# assigns the variable "form_window" to a window
form_window.title('Party Hire')
# adds a title to the window
window_width = 500
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
# loops the following code 6 times
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
    # if r is equal to 1, executes the following code
        lbl_error = tk.Label(frm_error, text="NOT REQUIRED")
    else:
    # else, it executes this code
        lbl_error = tk.Label(frm_error, text="REQUIRED")
    lbl_error.pack()

frm_btn = tk.Frame(form_window, borderwidth=3)
frm_btn.grid(row=7, column=1, padx=5, pady=5, sticky="e")
btn_next = tk.Button(frm_btn, text="Submit", width=10, command=submit)
# creates a button assigned to "btn_next"
# with the text "Submit"
# and executes command "submit" when clicked
btn_next.pack()

files_window = tk.Tk()
files_window.title('Saved Files')

path = os.getcwd()
cust_files = []
for f in os.listdir(path):
    if f.endswith(".txt"):
        cust_files.append(f)

frm_files = tk.Frame(files_window, relief=tk.RIDGE, borderwidth=3)
frm_files.grid(row=0, column=0, padx=10, pady=5, sticky="we")
lbl_files = tk.Label(frm_files, text="Pick a file to open:")
lbl_files.pack()
if len(cust_files) != 0:
    for cf in range(len(cust_files)):
        frm_list = tk.Frame(files_window, borderwidth=3)
        frm_list.grid(row=(cf+1), column=0, padx=10, pady=5, sticky="we")
        btn_list = tk.Button(frm_list, text=cust_files[cf], command=file_info(cust_files[cf]))
        btn_list.pack()

files_window.mainloop()

form_window.mainloop()
# runs and loops the form window