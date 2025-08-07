import tkinter as tk
import random as rdm

wdnw_srvy = tk.Tk()

wdnw_srvy.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=25)
wdnw_srvy.columnconfigure([0, 1], minsize=25)

list_qstn = {
    "Given name:" : "0",
    "Middle name:" : "1",
    "Family name:" : "2",
    "Item name:" : "3",
    "Quantity of items:" : "4",
    "Date the item/s will be issued:" : "5",
    "Data the item/s will be returned" : "6",
}

list_inpt = {
    "nm_gvn" : "0",
    "nm_mid" : "1",
    "nm_lst" : "2",
    "itm_nm" : "3",
    "itm_num" : "4",
    "itm_issued" : "5",
    "itm_returned" : "6",
}

for qstn, num in list_qstn.items():
    frm_qstn = tk.Frame(wdnw_srvy, relief=tk.RIDGE, borderwidth=3)
    frm_qstn.grid(row=num, column=0, padx=5, pady=5, sticky="w")
    lbl_qstn = tk.Label(frm_qstn, text=qstn)
    lbl_qstn.pack()

for inpt, num in list_inpt.items():
    frm_inpt = tk.Frame(wdnw_srvy, borderwidth=3)
    frm_inpt.grid(row=num, column=1, padx=5, pady=5, sticky="w")
    inpt = tk.Entry(frm_inpt)
    inpt.pack()


wdnw_srvy.mainloop()