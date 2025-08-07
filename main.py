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

wdnw_srvy.mainloop()