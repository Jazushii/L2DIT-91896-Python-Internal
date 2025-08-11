import tkinter as tk
import random as rdm

wdnw_srvy = tk.Tk()
# assigns the variable "wdnw_srvy" (window_survey) to a window

wdnw_srvy.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=25)
wdnw_srvy.columnconfigure([0, 1], minsize=25)
# configures the grid (rows and columns)

list_qstn = {
    "Given name:" : "0",
    "Middle name:" : "1",
    "Family name:" : "2",
    "Item name:" : "3",
    "Quantity of items:" : "4",
    "Date the item/s will be issued:" : "5",
    "Data the item/s will be returned" : "6",
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
    frm_qstn = tk.Frame(wdnw_srvy, relief=tk.RIDGE, borderwidth=3)
    frm_qstn.grid(row=num, column=0, padx=5, pady=5, sticky="w")
    lbl_qstn = tk.Label(frm_qstn, text=qstn)
    lbl_qstn.pack()
# loops for the amount of items in list_qstn,
# and replaces the label text as the first given variable in the list,
# and replaces the row number as the second given variable in the list

for inpt, num in list_inpt.items():
    frm_inpt = tk.Frame(wdnw_srvy, borderwidth=3)
    frm_inpt.grid(row=num, column=1, padx=5, pady=5, sticky="w")
    inpt = tk.Entry(frm_inpt)
    inpt.pack()
# loops for the amount of items in list_inpt,
# and replaces the entry name as the first given variable in the list,
# and replaces the row number as the second given variable in the list

wdnw_srvy.mainloop()
# loops and runs the window "wdnw_srvy"