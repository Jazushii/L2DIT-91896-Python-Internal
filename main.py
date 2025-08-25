import tkinter as tk
import random as rdm

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
    "Data the item/s\nwill be returned" : "6",
}
# assigns the variable "list_qstn" (list_question) to the list of questions
# and their respective rows in the first column
# question : row number

list_inpt = {
    "nm_gvn" : "0",
    "nm_mid" : "1",
    "nm_lst" : "2",
    "itm_nm" : "3",
    "itm_num" : "4",
    "itm_issued" : "5",
    "itm_returned" : "6",
}
# assigns the variable "list_inpt" (list_input) to  the list of names for the entries
# and their respective rows in the second column
# entry name : row number

for qstn, num in list_qstn.items():
    frm_qstn = tk.Frame(wndw_srvy, relief=tk.RIDGE, borderwidth=3)
    # assigns the variable "frm_qstn" (frame_question) as the frame to put the labels in
    # its "master" is wdnw_srvy
    # its relief (border style) is set to ridged
    # its borderwidth is set to 3
    frm_qstn.grid(row=num, column=0, padx=5, pady=5, sticky="w")
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

for inpt, num in list_inpt.items():
    frm_inpt = tk.Frame(wndw_srvy, borderwidth=3)
    frm_inpt.grid(row=num, column=1, padx=5, pady=5, sticky="w")
    inpt = tk.Entry(frm_inpt, width=20)
    inpt.pack()
# loops for the amount of items in list_inpt,
# and replaces the entry name as the first given variable in the list,
# and replaces the row number as the second given variable in the list

def cnfrm_sbmt():
    wndw_cnfrm = tk.Tk()
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