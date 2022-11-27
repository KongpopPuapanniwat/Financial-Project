import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import all_def

class App:
    def __init__(self,root):
        self.list = []

        # setting title
        root.title("Risk Lending Assessment Program")

        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLabel_221 = tk.Label(root)                # Input proportion of each C
        ft = tkFont.Font(family='Times', size=18)
        self.GLabel_221["font"] = ft
        self.GLabel_221["fg"] = "#333333"
        self.GLabel_221["justify"] = "center"
        self.GLabel_221["text"] = "Input proportion of each C"
        self.GLabel_221.place(x=20, y=50, width=251, height=30)

        self.GLabel_430 = tk.Label(root)                # Risk lending assessment program
        ft = tkFont.Font(family='Times', size=28)
        self.GLabel_430["font"] = ft
        self.GLabel_430["fg"] = "#333333"
        self.GLabel_430["justify"] = "center"
        self.GLabel_430["text"] = "Risk lending assessment program"
        self.GLabel_430.place(x=50, y=10, width=511, height=30)

        self.GLabel_810 = tk.Label(root)                # Character
        self.GLabel_810["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=9)
        self.GLabel_810["font"] = ft
        self.GLabel_810["fg"] = "#333333"
        self.GLabel_810["justify"] = "center"
        self.GLabel_810["text"] = "Character"
        self.GLabel_810.place(x=60, y=80, width=58, height=30)

        self.character = tk.IntVar()                    # Entry Character
        self.character_var = tk.Entry(root,textvariable=self.character)
        self.character_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.character_var["font"] = ft
        self.character_var["fg"] = "#333333"
        self.character_var["justify"] = "center"
        self.character_var.place(x=10, y=80, width=52, height=30)

        self.capability = tk.IntVar()                  # Entry Capability
        self.capability_var = tk.Entry(root,textvariable = self.capability)
        self.capability_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.capability_var["font"] = ft
        self.capability_var["fg"] = "#333333"
        self.capability_var["justify"] = "center"
        self.capability_var.place(x=130, y=80, width=49, height=30)

        self.GLabel_99 = tk.Label(root)                 # capability
        self.GLabel_99["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=9)
        self.GLabel_99["font"] = ft
        self.GLabel_99["fg"] = "#333333"
        self.GLabel_99["justify"] = "center"
        self.GLabel_99["text"] = "Capability"
        self.GLabel_99.place(x=180, y=80, width=55, height=30)

        self.capital = tk.IntVar()                      # Entry capital
        self.capital_var = tk.Entry(root,textvariable = self.capital)
        self.capital_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.capital_var["font"] = ft
        self.capital_var["fg"] = "#333333"
        self.capital_var["justify"] = "center"
        self.capital_var.place(x=250, y=80, width=51, height=30)

        self.GLabel_739 = tk.Label(root)                # Capital
        self.GLabel_739["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=9)
        self.GLabel_739["font"] = ft
        self.GLabel_739["fg"] = "#333333"
        self.GLabel_739["justify"] = "center"
        self.GLabel_739["text"] = "Capital"
        self.GLabel_739.place(x=300, y=80, width=50, height=30)

        self.collateral = tk.IntVar()                                      # Entry Collateral
        self.collateral_var = tk.Entry(root,textvariable = self.collateral)
        self.collateral_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.collateral_var["font"] = ft
        self.collateral_var["fg"] = "#333333"
        self.collateral_var["justify"] = "center"
        self.collateral_var.place(x=360, y=80, width=51, height=30)

        self.GLabel_932 = tk.Label(root)                                   # Collateral
        self.GLabel_932["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=9)
        self.GLabel_932["font"] = ft
        self.GLabel_932["fg"] = "#333333"
        self.GLabel_932["justify"] = "center"
        self.GLabel_932["text"] = "Collateral"
        self.GLabel_932.place(x=410, y=80, width=62, height=30)

        self.condition = tk.IntVar()                                       # Entry Condition
        self.condition_var = tk.Entry(root,textvariable = self.condition)
        self.condition_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.condition_var["font"] = ft
        self.condition_var["fg"] = "#333333"
        self.condition_var["justify"] = "center"
        self.condition_var.place(x=480, y=80, width=50, height=30)

        self.GLabel_666 = tk.Label(root)                                   # Condition
        self.GLabel_666["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=9)
        self.GLabel_666["font"] = ft
        self.GLabel_666["fg"] = "#333333"
        self.GLabel_666["justify"] = "center"
        self.GLabel_666["text"] = "Condition"
        self.GLabel_666.place(x=530, y=80, width=55, height=30)


        self.GLabel_118 = tk.Label(root)                                   # Input sub C
        ft = tkFont.Font(family='Times', size=16)
        self.GLabel_118["font"] = ft
        self.GLabel_118["fg"] = "#333333"
        self.GLabel_118["justify"] = "center"
        self.GLabel_118["text"] = "Input proportion of sub C"
        self.GLabel_118.place(x=0, y=130, width=221, height=30)

        self.text_file_sub_c = tk.StringVar()
        self.sub_c_var = tk.Entry(root,textvariable=self.text_file_sub_c)  # Entry sub c
        self.sub_c_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.sub_c_var["font"] = ft
        self.sub_c_var["fg"] = "#333333"
        self.sub_c_var["justify"] = "center"
        self.sub_c_var.place(x=30, y=160, width=70, height=25)

        self.GLabel_692 = tk.Label(root)                                 # Text file sub-C
        self.GLabel_692["bg"] = "#c71585"
        ft = tkFont.Font(family='Times', size=18)
        self.GLabel_692["font"] = ft
        self.GLabel_692["fg"] = "#333333"
        self.GLabel_692["justify"] = "center"
        self.GLabel_692["text"] = "text file"
        self.GLabel_692.place(x=100, y=160, width=70, height=25)

        self.GLabel_507 = tk.Label(root)                                # Input cut-off point
        ft = tkFont.Font(family='Times', size=16)
        self.GLabel_507["font"] = ft
        self.GLabel_507["fg"] = "#333333"
        self.GLabel_507["justify"] = "center"
        self.GLabel_507["text"] = "Input cut off point "
        self.GLabel_507.place(x=240, y=130, width=179, height=30)

        self.text_file_cut_off = tk.StringVar()                          # Entry text cut-off
        self.cut_off_var = tk.Entry(root,textvariable=self.text_file_cut_off)
        self.cut_off_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.cut_off_var["font"] = ft
        self.cut_off_var["fg"] = "#333333"
        self.cut_off_var["justify"] = "center"
        self.cut_off_var.place(x=260, y=160, width=74, height=30)

        self.GLabel_987 = tk.Label(root)  # text file cut-off
        self.GLabel_987["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times', size=17)
        self.GLabel_987["font"] = ft
        self.GLabel_987["fg"] = "#333333"
        self.GLabel_987["justify"] = "center"
        self.GLabel_987["text"] = "text file"
        self.GLabel_987.place(x=330, y=160, width=57, height=30)

        self.GLabel_865 = tk.Label(root)                                # Input loan info
        ft = tkFont.Font(family='Times', size=16)
        self.GLabel_865["font"] = ft
        self.GLabel_865["fg"] = "#333333"
        self.GLabel_865["justify"] = "center"
        self.GLabel_865["text"] = "Input loaner info"
        self.GLabel_865.place(x=430, y=130, width=159, height=30)

        self.csv_loan_info = tk.StringVar()                            # Entry loan info
        self.loan_info_var = tk.Entry(root,textvariable=self.csv_loan_info)
        self.loan_info_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.loan_info_var["font"] = ft
        self.loan_info_var["fg"] = "#333333"
        self.loan_info_var["justify"] = "center"
        self.loan_info_var.place(x=440, y=160, width=70, height=25)

        self.GLabel_307 = tk.Label(root)                               # csv loan info
        self.GLabel_307["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times', size=18)
        self.GLabel_307["font"] = ft
        self.GLabel_307["fg"] = "#333333"
        self.GLabel_307["justify"] = "center"
        self.GLabel_307["text"] = "csv file"
        self.GLabel_307.place(x=510, y=160, width=70, height=25)

        self.GLabel_728 = tk.Label(root)                                # pick User
        ft = tkFont.Font(family='Times', size=23)
        self.GLabel_728["font"] = ft
        self.GLabel_728["fg"] = "#333333"
        self.GLabel_728["justify"] = "center"
        self.GLabel_728["text"] = "Pick user "
        self.GLabel_728.place(x=20, y=220, width=113, height=30)

        self.username = tk.StringVar()
        self.username_var = tk.Entry(root,textvariable=self.username)  # Entry username
        self.username_var["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=23)
        self.username_var["font"] = ft
        self.username_var["fg"] = "#333333"
        self.username_var["justify"] = "center"
        self.username_var.place(x=140, y=220, width=81, height=30)

        self.submit = tk.Radiobutton(root)                             # Submit all info
        self.submit["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times', size=23)
        self.submit["font"] = ft
        self.submit["fg"] = "#333333"
        self.submit["justify"] = "center"
        self.submit["text"] = "Submit"
        self.submit.place(x=240,y=220,width=108,height=30)
        self.submit["command"] = self.submit_command



    def submit_command(self):
        self.character = self.character_var.get()
        self.capability = self.capability_var.get()
        self.capital = self.capital_var.get()
        self.collateral = self.collateral_var.get()
        self.condition = self.condition_var.get()
        self.text_file_sub_c = self.sub_c_var.get()
        self.text_file_cut_off = self.cut_off_var.get()
        self.csv_loan_info = self.loan_info_var.get()
        self.username = self.username_var.get()

        self.list.append(self.character)
        self.list.append(self.capability)
        self.list.append(self.capital)
        self.list.append(self.collateral)
        self.list.append(self.condition)
        self.list.append(self.text_file_sub_c)
        self.list.append(self.text_file_cut_off)
        self.list.append(self.csv_loan_info)
        self.list.append(self.username)
        print(self.list)

        self.character = self.list[0]
        self.capability = self.list[1]
        self.capital = self.list[2]
        self.collateral = self.list[3]
        self.condition = self.list[4]

        self.maxscore_character = int(self.character) * 10
        self.maxscore_capability = int(self.capability) * 10
        self.maxscore_capital = int(self.capital) * 10
        self.maxscore_collateral = int(self.collateral) * 10
        self.maxscore_condition = int(self.condition) * 10

        print('maxscore_character:', self.maxscore_character)
        print('maxscore_capability:', self.maxscore_capability)
        print('maxscore_capital:', self.maxscore_capital)
        print('maxscore_collateral:', self.maxscore_collateral)
        print('maxscore_condition', self.maxscore_condition)

        self.file = open(self.list[5], 'r')  # Input proportion of sub-C
        self.list_maxscore = []
        for x in self.file:
            for y in x.split():
                self.list_maxscore.append(int(y))
        print(self.list_maxscore)


        self.credit_buro_score = (self.list_maxscore[0] / 100) * self.maxscore_character
        self.region_score = (self.list_maxscore[1] / 100) * self.maxscore_character
        self.job_score = (self.list_maxscore[2] / 100) * self.maxscore_character
        self.social_status_score = (self.list_maxscore[3] / 100) * self.maxscore_character
        self.income_score = (self.list_maxscore[4] / 100) * self.maxscore_capability
        self.health_score = (self.list_maxscore[5] / 100) * self.maxscore_capability
        self.job_stability_score = (self.list_maxscore[6] / 100) * self.maxscore_capability
        self.having_debt_score = (self.list_maxscore[7] / 100) * self.maxscore_capability
        self.other_debt_score = (self.list_maxscore[8] / 100) * self.maxscore_capability
        self.capital_score = (self.list_maxscore[9] / 100) * self.maxscore_capital
        self.asset_score = (self.list_maxscore[10] / 100) * self.maxscore_capital

        #print('credit_buro_score:',self.credit_buro_score)
        #print('region_score:',self.region_score)
        #print('job_score:',self.job_score)
        #print('social_status_score:',self.social_status_score)
        #print('income_score:',self.income_score)
        #print('health_score:',self.health_score)
        #print('job_stability_score:',self.job_stability_score)
        #print('having_debt_score:',self.having_debt_score)
        #print('other_debt_score:',self.other_debt_score)
        #print('capital_score:',self.capital_score)
        #print('asset_score:',self.asset_score)
        #print('maxscore_collateral:',self.maxscore_collateral)
        #print('maxscore_condition:',self.maxscore_condition)


        self.df = pd.read_csv(self.list[7], encoding='TIS-620')
        print(self.df)
        for y in range(len(self.df.index)):
            if self.username == self.df.loc[y].Username:
                self.user_count_repayment = all_def.repayment(self.credit_buro_score, self.df.loc[y].repayment_history)
                self.user_count_region = all_def.region(self.region_score, self.df.loc[y].region_info)
                self.user_count_job = all_def.job(self.job_score, self.df.loc[y].job_info)
                self.user_count_social = all_def.social(self.social_status_score, self.df.loc[y].social_status)
                self.user_count_income = all_def.income(self.income_score, self.df.loc[y].revenue, self.df.loc[y].loan, self.df.loc[y].rate, self.df.loc[y].year)
                self.user_count_health = all_def.health(self.health_score, self.df.loc[y].health_info)
                self.user_count_job_stability = all_def.job_stability(self.job_stability_score, self.df.loc[y].job_year)
                self.user_count_having_debt = all_def.having_debt(self.having_debt_score, self.df.loc[y].pay_other_debt, self.df.loc[y].revenue)
                self.user_count_other_debt = all_def.other_debt(self.other_debt_score, self.df.loc[y].debt, self.df.loc[y].asset)
                self.user_count_capital_structure = all_def.capital_structure(self.capital_score, self.df.loc[y].asset, self.df.loc[y].debt)
                self.user_count_percent_asset = all_def.percent_asset(self.asset_score, self.df.loc[y].asset,self.df.loc[y].loan)
                self.user_count_collateral = all_def.collateral(self.maxscore_collateral, self.df.loc[y].collateral_asset, self.df.loc[y].loan,self.df.loc[y].liquidity_collateral)
                self.user_count_condition = all_def.condition(self.maxscore_condition, self.df.loc[y].percent_inflation, self.df.loc[y].job_info)

                self.sum_character = self.user_count_repayment + self.user_count_region + self.user_count_job + self.user_count_social
                self.sum_capability = self.user_count_income + self.user_count_health + self.user_count_job_stability + self.user_count_having_debt + self.user_count_other_debt
                self.sum_capital = self.user_count_capital_structure + self.user_count_percent_asset
                self.sum_collateral = self.user_count_collateral
                self.sum_condition = self.user_count_condition

                print('sum_character:', self.sum_character)
                print('sum_capability:', self.sum_capability)
                print('sum_capital:', self.sum_capital)
                print('sum_collateral:', self.sum_collateral)
                print('sum_condition:', self.sum_condition)

            else:
                print('Username = ',self.df.loc[y].Username)
                print('self.username = ',self.username)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
