import tkinter as tk
import random as rdm
import datetime

class Customer:
    def __init__(self, given_name, mid_name, last_name, itm_name, itm_num, itm_issued, itm_returned):
        self.reciept_num = rdm.randint(10000, 99999)
        self.given_name = given_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.full_name = f"{self.last_name}, {self.given_name} {self.mid_name}"
        self.itm_name = itm_name
        self.itm_num = itm_num
        self.itm_issued = itm_issued
        self.itm_returned = itm_returned
    def __str__(self):
        return f"Customer reciept no: {self.reciept_num}\n{self.last_name}, {self.given_name} {self.mid_name}\nOrdered {self.itm_num} {self.itm_name}\nIssued on {self.itm_issued} and to be returned on {self.itm_returned}"

list_question = {
    "Given name:" : "0",
    "Middle name:" : "1",
    "Family name:" : "2",
    "Item name:" : "3",
    "Quantity of\nitems:" : "4",
    "Date the item/s\nwill be issued:" : "5",
    "Data the item/s\nwill be returned:" : "6",
}
# assigns the variable "list_qstn" (list_question) to the list of questions
# and their respective rows in the first column
# question : row number

main_window = tk.Tk()
# assigns the variable "wdnw_srvy" (window_survey) to a window

main_window.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=25)
main_window.columnconfigure([0, 1], minsize=25)
# configures the grid (rows and columns)

for question, row in list_question.items():
    frm_question = tk.Frame(main_window, relief=tk.RIDGE, borderwidth=3)
    # assigns the variable "frm_qstn" (frame_question) as the frame to put the labels in
    # its "master" is wdnw_srvy
    # its relief (border style) is set to ridged
    # its borderwidth is set to 3
    frm_question.grid(row=row, column=0, padx=5, pady=5, sticky="w")
    # puts frm_qstn into a grid
    # where its located in row "num", which is in the list_qstn list
    # and in column 0 (the first column)
    # with x and y padding to 5
    # and sticks to "w" (west / left side)
    lbl_question = tk.Label(frm_question, text=question, width=12)
    # assigns the variable "lbl_qstn" (label_question) as the label
    # its "master" is frm_qstn
    # its text is "qstn", which is in the list_qstn list
    # its width is set to 12
    lbl_question.pack()
    # runs lbl_qstn
# loops for the amount of items in list_qstn,
# and replaces the label text as the first given variable in the list,
# and replaces the row number as the second given variable in the list

frm_ent = tk.Frame(main_window, borderwidth=3)
frm_ent.grid(row=0, column=1, padx=5, pady=5, sticky="w")
ent_given_name = tk.Entry(frm_ent, width=20)
ent_given_name.pack()

frm_ent = tk.Frame(main_window, borderwidth=3)
frm_ent.grid(row=1, column=1, padx=5, pady=5, sticky="w")
ent_mid_name = tk.Entry(frm_ent, width=20)
ent_mid_name.pack()

frm_ent = tk.Frame(main_window, borderwidth=3)
frm_ent.grid(row=2, column=1, padx=5, pady=5, sticky="w")
ent_last_name = tk.Entry(frm_ent, width=20)
ent_last_name.pack()

frm_ent = tk.Frame(main_window, borderwidth=3)
frm_ent.grid(row=3, column=1, padx=5, pady=5, sticky="w")
ent_itm_name = tk.Entry(frm_ent, width=20)
ent_itm_name.pack()

frm_ent = tk.Frame(main_window, borderwidth=3)
frm_ent.grid(row=4, column=1, padx=5, pady=5, sticky="w")
ent_itm_num = tk.Entry(frm_ent, width=20)
ent_itm_num.pack()

frm_ent = tk.Frame(main_window, borderwidth=3)
frm_ent.grid(row=5, column=1, padx=5, pady=5, sticky="w")
ent_itm_issued = tk.Entry(frm_ent, width=20)
ent_itm_issued.pack()

frm_ent = tk.Frame(main_window, borderwidth=3)
frm_ent.grid(row=6, column=1, padx=5, pady=5, sticky="w")
ent_itm_returned = tk.Entry(frm_ent, width=20)
ent_itm_returned.pack()

def confirm_submit():
    given_name = ent_given_name.get()
    mid_name = ent_mid_name.get()
    last_name = ent_last_name.get()
    itm_name = ent_itm_name.get()
    itm_num = ent_itm_num.get()
    itm_issued = ent_itm_issued.get()
    itm_returned = ent_itm_returned.get()
    ctm = Customer(given_name, mid_name, last_name, itm_name, itm_num, itm_issued, itm_returned)

    confirm_window = tk.Tk()
    print(ctm)
    print(ctm.full_name)
    frm_ctm = tk.Frame(confirm_window)
    frm_ctm.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    lbl_ctm = tk.Label(frm_ctm, text=ctm, width=20)
    lbl_ctm.pack()
    confirm_window.mainloop()
# defines the command "confirm_submit" which creates a separate window

frm_submit = tk.Frame(main_window, borderwidth=3)
frm_submit.grid(row=7, column=1, padx=5, pady=5, sticky="we")
btn_submit = tk.Button(frm_submit, text="Confirm Submission", command=confirm_submit)
# "comman=confirm_submit" makes the button "btn_submit" excute "cnfrm_sbmt"
btn_submit.pack()
# creates a button to confirm submissions

main_window.mainloop()
# loops and runs wdnw_srvy