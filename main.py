import tkinter as tk
import random as rdm

class Customer:
    def __init__(self, nm_given, nm_mid, nm_last, itm_nm, itm_num, itm_issued, itm_returned):
        self.nm_given = nm_given
        self.nm_mid = nm_mid
        self.nm_last = nm_last
        self.itm_nm = itm_nm
        self.itm_num = itm_num
        self.itm_issued = itm_issued
        self.itm_returned = itm_returned
    def __str__(self):
        return f"{self.nm_last}, {self.nm_given} {self.nm_mid}"

wndw_srvy = tk.Tk()
# assigns the variable "wdnw_srvy" (window_survey) to a window

wndw_srvy.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=25)
wndw_srvy.columnconfigure([0, 1], minsize=25)
# configures the grid (rows and columns)

list_qstn = {
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

for qstn, row in list_qstn.items():
    frm_qstn = tk.Frame(wndw_srvy, relief=tk.RIDGE, borderwidth=3)
    # assigns the variable "frm_qstn" (frame_question) as the frame to put the labels in
    # its "master" is wdnw_srvy
    # its relief (border style) is set to ridged
    # its borderwidth is set to 3
    frm_qstn.grid(row=row, column=0, padx=5, pady=5, sticky="w")
    # puts frm_qstn into a grid
    # where its located in row "num", which is in the list_qstn list
    # and in column 0 (the first column)
    # with x and y padding to 5
    # and sticks to "w" (west / left side)
    lbl_qstn = tk.Label(frm_qstn, text=qstn, width=12)
    # assigns the variable "lbl_qstn" (label_question) as the label
    # its "master" is frm_qstn
    # its text is "qstn", which is in the list_qstn list
    # its width is set to 12
    lbl_qstn.pack()
    # runs lbl_qstn
# loops for the amount of items in list_qstn,
# and replaces the label text as the first given variable in the list,
# and replaces the row number as the second given variable in the list

frm_ent = tk.Frame(wndw_srvy, borderwidth=3)
frm_ent.grid(row=0, column=1, padx=5, pady=5, sticky="w")
ent_nm_gvn = tk.Entry(frm_ent, width=20)
ent_nm_gvn.pack()

def cnfrm_sbmt():
    nm_gvn = ent_nm_gvn.get()
    nm_mid = ent_nm_gvn.get()
    nm_lst = ent_nm_gvn.get()
    itm_nm = ent_nm_gvn.get()
    itm_num = ent_nm_gvn.get()
    itm_issued = ent_nm_gvn.get()
    itm_returned = ent_nm_gvn.get()
    cstmr = Customer(nm_gvn, nm_mid, nm_lst, itm_nm, itm_num, itm_issued, itm_returned)

    wndw_cnfrm = tk.Tk()
    frm_cstmr = tk.Frame()
    wndw_cnfrm.mainloop()
# defines the command "cnfrm_sbmt" which creates a separate window

frm_sbmt = tk.Frame(wndw_srvy, borderwidth=3)
frm_sbmt.grid(row=7, column=1, padx=5, pady=5, sticky="we")
btn_sbmt = tk.Button(frm_sbmt, text="Confirm Submission", command=cnfrm_sbmt)
# "comman=cnfrm_sbmt" makes the button "btn_sbmt" excute "cnfrm_sbmt"
btn_sbmt.pack()
# creates a button to confirm submissions

wndw_srvy.mainloop()
# loops and runs wdnw_srvy