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

itm_name = "hi"

q_list = [
    "What is your given name? (Required)",
    "What is your middle/s name? (Not Required)",
    "What is your last name? (Required)",
    "Pick an item: (If you want multiple items, will need to submit another form)",
    f"How many {itm_name} are you issuing?",
    "Date the items will be issued:",
    "Data the items will be returned:",
]
q_list_num = 0

ent_list = [
    "given_name",
    "mid_name",
    "last_name",
    "itm_name",
    "itm_num",
    "itm_issued",
    "itm_returned",
]
ent_list_num = 0

itm_list = [
    "Eating Utensils (Spoon and Fork)",
    "Glassware"
    "Tables",
    "Chairs",
    "Party Hats",
    "Balloons",
]
itm_list_num = 0

def next():
    global q_list_num
    global ent_list_num

    ent_list[ent_list_num] = ent_q.get()

    q_list_num += 1
    ent_list_num += 1
    q_window.destroy()

main = True
while main:

    if q_list_num == 7:
        c1 = Customer(
            ent_list[0],
            ent_list[1],
            ent_list[2],
            ent_list[3],
            ent_list[4],
            ent_list[5],
            ent_list[6])
        submit_window = tk.Tk()

        submit_window.mainloop()
        main = False

    else:
        q_window = tk.Tk()
        # assigns the variable "q_window" (question window) to a window
        q_window.title('Form Window')
        # adds a title to the window
        window_width = 800
        window_height = 450
        # setting up variables
        screen_width = q_window.winfo_screenwidth()
        screen_height = q_window.winfo_screenheight()
        # gets the screen's dimensions
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        # finds the center point of the screen
        q_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        # set the position of the window to the center of the screen'
        q_window.resizable(False, False)
        # does not allow to resize the window
        q_window.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=25)
        q_window.columnconfigure([0, 1], minsize=25)
        # configures the grid (rows and columns)
    

        frm_q = tk.Frame(q_window, relief=tk.RIDGE, borderwidth=3)
        frm_q.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        lbl_q = tk.Label(frm_q, text=q_list[q_list_num], width=12)
        lbl_q.pack()

        frm_ent = tk.Frame(q_window, relief=tk.RIDGE, borderwidth=3)
        frm_ent.grid(row=2, column=0, padx=5, pady=5, sticky="we")
        ent_q = tk.Entry(frm_ent, width=12)
        ent_q.pack()

        frm_btn = tk.Frame(q_window, borderwidth=3)
        frm_btn.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        btn_next = tk.Button(frm_btn, text="Next", command=next)
        btn_next.pack()

        q_window.mainloop()