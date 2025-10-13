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

itm_name = "items"

q_list = [
    "What is your given name?\n(Required)",
    "What is your middle/s name?\n(Not Required)",
    "What is your last name?\n(Required)",
    "Pick an item:\n(If you want multiple items,\nwill need to submit another form)",
    f"How many {itm_name} are you issuing?",
    "Date the items will be issued:",
    "Data the items will be returned:",
]

ent_list = [
    "ent_given_name",
    "ent_mid_name",
    "ent_last_name",
    "ent_itm_name",
    "ent_itm_num",
    "ent_itm_issued",
    "ent_itm_returned",
]

input_list = [
    "given_name",
    "mid_name",
    "last_name",
    "itm_name",
    "itm_num",
    "itm_issued",
    "itm_returned",
]

itm_list = [
    "Eating Utensils\n(Spoons and Forks)",
    "Glassware",
    "Tables",
    "Chairs",
    "Party Hats",
    "Balloons",
]
error = False
def error(num, type):
    global error
    error = True
    if type == "blank":
        ent_list[num].insert(tk.END, "REQUIRED")
    if type == "not_text":
        ent_list[num].insert(tk.END, " ONLY LETTERS")

def submit():
    for g in range(7):
        input_list[g] = ent_list[g].get()
    # takes the value of the entries
    for s in range(2):
        if input_list[s] is not str:
            if input_list[s] == "":
                error(s, "blank")
            else:
                error(s, "not_text")
        s += 1
    # checks of the entries put in name is a string
    if error == False:
        c1 = Customer(
            input_list[0],
            input_list[1],
            input_list[2],
            input_list[3],
            input_list[4],
            input_list[5],
            input_list[6],
    )

form_window = tk.Tk()
# assigns the variable "q_window" (question window) to a window
form_window.title('Form Window')
# adds a title to the window
window_width = 600
window_height = 380
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
    
for r in range(7):
    frm_q = tk.Frame(form_window, relief=tk.RIDGE, borderwidth=3)
    # assigns the variable "frm_qstn" (frame_question) as the frame to put the labels in
    # its "master" is wdnw_srvy
    # its relief (border style) is set to ridged
    # its borderwidth is set to 3
    frm_q.grid(row=r, column=0, padx=5, pady=5, sticky="w")
    # puts frm_qstn into a grid
    # where its located in row "num", which is in the list_qstn list
    # and in column 0 (the first column)
    # with x and y padding to 5
    # and sticks to "w" (west / left side)
    lbl_q = tk.Label(frm_q, text=q_list[r])
    # assigns the variable "lbl_qstn" (label_question) as the label
    # its "master" is frm_qstn
    # its text is "qstn", which is in the list_qstn list
    # its width is set to 12
    lbl_q.pack()
    # runs lbl_qstn

    if r == 3:
        b = 0
        for br in range(2):
            for bc in range(3):
                frm_btn = tk.Frame(form_window, relief=tk.RIDGE, borderwidth=3)
                frm_btn.grid(row=(br+3), column=(bc+1), padx=5, pady=5, sticky="we")
                itm_list[b] = tk.Button(frm_btn, text=itm_list[b], width=15)
                itm_list[b].pack()
                b += 1
    else:
        frm_ent = tk.Frame(form_window, relief=tk.RIDGE, borderwidth=3)
        frm_ent.grid(row=r, column=1, padx=5, pady=5, sticky="we")
        ent_list[r] = tk.Entry(frm_ent, width=15)
        ent_list[r].pack()

frm_btn = tk.Frame(form_window, borderwidth=3)
frm_btn.grid(row=7, column=1, padx=5, pady=5, sticky="e")
btn_next = tk.Button(frm_btn, text="Sumbit", width=10, command=submit)
btn_next.pack()

form_window.mainloop()