import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, loan):
        #setting title
        loan.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = loan.winfo_screenwidth()
        screenheight = loan.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        loan.geometry(alignstr)
        loan.resizable(width=False, height=False)

        user_score = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=30)
        user_score["font"] = ft
        user_score["fg"] = "#333333"
        user_score["justify"] = "center"
        user_score["text"] = "User Score "
        user_score.place(x=10, y=0, width=192, height=42)

        user_carac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user_carac["font"] = ft
        user_carac["fg"] = "#333333"
        user_carac["justify"] = "center"
        user_carac["text"] = "sum_character"
        user_carac.place(x=230, y=50, width=89, height=41)

        carac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        carac["font"] = ft
        carac["fg"] = "#333333"
        carac["justify"] = "center"
        carac["text"] = "Character :"
        carac.place(x=40, y=50, width=132, height=38)

        capab = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        capab["font"] = ft
        capab["fg"] = "#333333"
        capab["justify"] = "center"
        capab["text"] = "Capability :"
        capab.place(x=40, y=80, width=128, height=32)

        user_capab = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user_capab["font"] = ft
        user_capab["fg"] = "#333333"
        user_capab["justify"] = "center"
        user_capab["text"] = "sum_capability"
        user_capab.place(x=190, y=80, width=173, height=30)

        capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        capi["font"] = ft
        capi["fg"] = "#333333"
        capi["justify"] = "center"
        capi["text"] = "Capital :"
        capi.place(x=50, y=110, width=141, height=30)

        user_capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user_capi["font"] = ft
        user_capi["fg"] = "#333333"
        user_capi["justify"] = "center"
        user_capi["text"] = "sum_capital"
        user_capi.place(x=180, y=110, width=145, height=30)

        coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        coll["font"] = ft
        coll["fg"] = "#333333"
        coll["justify"] = "center"
        coll["text"] = "Collateral :"
        coll.place(x=40, y=140, width=132, height=31)

        user_coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user_coll["font"] = ft
        user_coll["fg"] = "#333333"
        user_coll["justify"] = "center"
        user_coll["text"] = "sum_collateral"
        user_coll.place(x=190, y=140, width=153, height=30)

        condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        condi["font"] = ft
        condi["fg"] = "#333333"
        condi["justify"] = "center"
        condi["text"] = "Condition :"
        condi.place(x=40, y=170, width=128, height=30)

        user_condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user_condi["font"] = ft
        user_condi["fg"] = "#333333"
        user_condi["justify"] = "center"
        user_condi["text"] = "sum_condition"
        user_condi.place(x=190, y=170, width=142, height=30)

        max_charac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_charac["font"] = ft
        max_charac["fg"] = "#333333"
        max_charac["justify"] = "center"
        max_charac["text"] = "max_character"
        max_charac.place(x=390, y=50, width=172, height=37)

        max_capa = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_capa["font"] = ft
        max_capa["fg"] = "#333333"
        max_capa["justify"] = "center"
        max_capa["text"] = "max_capability"
        max_capa.place(x=390, y=80, width=169, height=30)

        max_capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_capi["font"] = ft
        max_capi["fg"] = "#333333"
        max_capi["justify"] = "center"
        max_capi["text"] = "max_capital"
        max_capi.place(x=390, y=110, width=137, height=30)

        max_coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_coll["font"] = ft
        max_coll["fg"] = "#333333"
        max_coll["justify"] = "center"
        max_coll["text"] = "max_collateral"
        max_coll.place(x=440, y=140, width=70, height=25)

        max_condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_condi["font"] = ft
        max_condi["fg"] = "#333333"
        max_condi["justify"] = "center"
        max_condi["text"] = "max_condition"
        max_condi.place(x=440, y=170, width=70, height=25)


if __name__ == "__main__":
    loan = tk.Tk()
    app = App(loan)
    loan.mainloop()
