import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import all_def
import numpy as np
import matplotlib.pyplot as plt



class App:
    def __init__(self):
        loan = tk.Tk()
        # setting title
        loan.title('Risk Lending Assessment Program')

        # setting window size
        width = 600
        height = 500
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








# setting title
root = tk.Tk()
root.title('Risk Lending Assessment Program')

# setting window size
width = 600
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

list = []
GLabel_221 = tk.Label(root)                # Input proportion of each C
ft = tkFont.Font(family='Times', size=18)
GLabel_221["font"] = ft
GLabel_221["fg"] = "#333333"
GLabel_221["justify"] = "center"
GLabel_221["text"] = "Input proportion of each C"
GLabel_221.place(x=20, y=50, width=251, height=30)

GLabel_430 = tk.Label(root)                # Risk lending assessment program
ft = tkFont.Font(family='Times', size=28)
GLabel_430["font"] = ft
GLabel_430["fg"] = "#333333"
GLabel_430["justify"] = "center"
GLabel_430["text"] = "Risk lending assessment program"
GLabel_430.place(x=50, y=10, width=511, height=30)

GLabel_810 = tk.Label(root)                # Character
GLabel_810["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_810["font"] = ft
GLabel_810["fg"] = "#333333"
GLabel_810["justify"] = "center"
GLabel_810["text"] = "Character"
GLabel_810.place(x=60, y=80, width=58, height=30)

character = tk.IntVar()                    # Entry Character
character_var = tk.Entry(root,textvariable=character)
character_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
character_var["font"] = ft
character_var["fg"] = "#333333"
character_var["justify"] = "center"
character_var.place(x=10, y=80, width=52, height=30)

capability = tk.IntVar()                  # Entry Capability
capability_var = tk.Entry(root,textvariable = capability)
capability_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
capability_var["font"] = ft
capability_var["fg"] = "#333333"
capability_var["justify"] = "center"
capability_var.place(x=130, y=80, width=49, height=30)

GLabel_99 = tk.Label(root)                 # capability
GLabel_99["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_99["font"] = ft
GLabel_99["fg"] = "#333333"
GLabel_99["justify"] = "center"
GLabel_99["text"] = "Capability"
GLabel_99.place(x=180, y=80, width=55, height=30)

capital = tk.IntVar()                      # Entry capital
capital_var = tk.Entry(root,textvariable = capital)
capital_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
capital_var["font"] = ft
capital_var["fg"] = "#333333"
capital_var["justify"] = "center"
capital_var.place(x=250, y=80, width=51, height=30)

GLabel_739 = tk.Label(root)                # Capital
GLabel_739["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_739["font"] = ft
GLabel_739["fg"] = "#333333"
GLabel_739["justify"] = "center"
GLabel_739["text"] = "Capital"
GLabel_739.place(x=300, y=80, width=50, height=30)

collateral = tk.IntVar()                                      # Entry Collateral
collateral_var = tk.Entry(root,textvariable = collateral)
collateral_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
collateral_var["font"] = ft
collateral_var["fg"] = "#333333"
collateral_var["justify"] = "center"
collateral_var.place(x=360, y=80, width=51, height=30)

GLabel_932 = tk.Label(root)                                   # Collateral
GLabel_932["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_932["font"] = ft
GLabel_932["fg"] = "#333333"
GLabel_932["justify"] = "center"
GLabel_932["text"] = "Collateral"
GLabel_932.place(x=410, y=80, width=62, height=30)

condition = tk.IntVar()                                       # Entry Condition
condition_var = tk.Entry(root,textvariable = condition)
condition_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
condition_var["font"] = ft
condition_var["fg"] = "#333333"
condition_var["justify"] = "center"
condition_var.place(x=480, y=80, width=50, height=30)

GLabel_666 = tk.Label(root)                                   # Condition
GLabel_666["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_666["font"] = ft
GLabel_666["fg"] = "#333333"
GLabel_666["justify"] = "center"
GLabel_666["text"] = "Condition"
GLabel_666.place(x=530, y=80, width=55, height=30)


GLabel_118 = tk.Label(root)                                   # Input sub C
ft = tkFont.Font(family='Times', size=16)
GLabel_118["font"] = ft
GLabel_118["fg"] = "#333333"
GLabel_118["justify"] = "center"
GLabel_118["text"] = "Input proportion of sub C"
GLabel_118.place(x=0, y=130, width=221, height=30)

text_file_sub_c = tk.StringVar()
sub_c_var = tk.Entry(root,textvariable=text_file_sub_c)  # Entry sub c
sub_c_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=18)
sub_c_var["font"] = ft
sub_c_var["fg"] = "#333333"
sub_c_var["justify"] = "center"
sub_c_var.place(x=30, y=160, width=70, height=25)

GLabel_692 = tk.Label(root)                                 # Text file sub-C
GLabel_692["bg"] = "#c71585"
ft = tkFont.Font(family='Times', size=16)
GLabel_692["font"] = ft
GLabel_692["fg"] = "#333333"
GLabel_692["justify"] = "center"
GLabel_692["text"] = "text file"
GLabel_692.place(x=100, y=160, width=70, height=25)

GLabel_507 = tk.Label(root)                                # Input cut-off point
ft = tkFont.Font(family='Times', size=16)
GLabel_507["font"] = ft
GLabel_507["fg"] = "#333333"
GLabel_507["justify"] = "center"
GLabel_507["text"] = "Input cut off point "
GLabel_507.place(x=240, y=130, width=179, height=30)

text_file_cut_off = tk.StringVar()                          # Entry text cut-off
cut_off_var = tk.Entry(root,textvariable= text_file_cut_off)
cut_off_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=18)
cut_off_var["font"] = ft
cut_off_var["fg"] = "#333333"
cut_off_var["justify"] = "center"
cut_off_var.place(x=260, y=160, width=74, height=30)

GLabel_987 = tk.Label(root)                                    # text file cut-off
GLabel_987["bg"] = "#90ee90"
ft = tkFont.Font(family='Times', size=15)
GLabel_987["font"] = ft
GLabel_987["fg"] = "#333333"
GLabel_987["justify"] = "center"
GLabel_987["text"] = "text file"
GLabel_987.place(x=330, y=160, width=57, height=30)

GLabel_865 = tk.Label(root)                                # Input loan info
ft = tkFont.Font(family='Times', size=16)
GLabel_865["font"] = ft
GLabel_865["fg"] = "#333333"
GLabel_865["justify"] = "center"
GLabel_865["text"] = "Input loaner info"
GLabel_865.place(x=430, y=130, width=159, height=30)

csv_loan_info = tk.StringVar()                            # Entry loan info
loan_info_var = tk.Entry(root,textvariable= csv_loan_info)
loan_info_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=18)
loan_info_var["font"] = ft
loan_info_var["fg"] = "#333333"
loan_info_var["justify"] = "center"
loan_info_var.place(x=440, y=160, width=70, height=25)

GLabel_307 = tk.Label(root)                               # csv loan info
GLabel_307["bg"] = "#ffb800"
ft = tkFont.Font(family='Times', size=18)
GLabel_307["font"] = ft
GLabel_307["fg"] = "#333333"
GLabel_307["justify"] = "center"
GLabel_307["text"] = "csv file"
GLabel_307.place(x=510, y=160, width=70, height=25)

GLabel_728 = tk.Label(root)                                # pick User
ft = tkFont.Font(family='Times', size=23)
GLabel_728["font"] = ft
GLabel_728["fg"] = "#333333"
GLabel_728["justify"] = "center"
GLabel_728["text"] = "Pick user "
GLabel_728.place(x=20, y=220, width=113, height=30)

username = tk.StringVar()
username_var = tk.Entry(root,textvariable= username)  # Entry username
username_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=23)
username_var["font"] = ft
username_var["fg"] = "#333333"
username_var["justify"] = "center"
username_var.place(x=140, y=220, width=81, height=30)

submit = tk.Radiobutton(root,command= App)                             # Submit all info
submit["bg"] = "#cc0000"
ft = tkFont.Font(family='Times', size=23)
submit["font"] = ft
submit["fg"] = "#333333"
submit["justify"] = "center"
submit["text"] = "Submit"
submit.place(x=240,y=220,width=108,height=30)




root.mainloop()
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
#
















# # #Backup
# # Run program
# character = character_var.get()
#         capability = capability_var.get()
#         capital = capital_var.get()
#         collateral = collateral_var.get()
#         condition = condition_var.get()
#         text_file_sub_c = sub_c_var.get()
#         text_file_cut_off = cut_off_var.get()
#         csv_loan_info = loan_info_var.get()
#         username = username_var.get()
#
#         list.append(character)
#         list.append(capability)
#         list.append(capital)
#         list.append(collateral)
#         list.append(condition)
#         list.append(text_file_sub_c)
#         list.append(text_file_cut_off)
#         list.append(csv_loan_info)
#         list.append(username)
#         print(list)
#
#         character = list[0]
#         capability = list[1]
#         capital = list[2]
#         collateral = list[3]
#         condition = list[4]
#
#         maxscore_character = int(character) * 10
#         maxscore_capability = int(capability) * 10
#         maxscore_capital = int(capital) * 10
#         maxscore_collateral = int(collateral) * 10
#         maxscore_condition = int(condition) * 10
#
#         print('maxscore_character:', maxscore_character)
#         print('maxscore_capability:', maxscore_capability)
#         print('maxscore_capital:', maxscore_capital)
#         print('maxscore_collateral:', maxscore_collateral)
#         print('maxscore_condition', maxscore_condition)
#
#         file = open(list[5], 'r')  # Input proportion of sub-C
#         list_maxscore = []
#         for x in file:
#             for y in x.split():
#                  list_maxscore.append(int(y))
#
#
#         credit_buro_score = (list_maxscore[0] / 100) * maxscore_character
#         region_score = (list_maxscore[1] / 100) * maxscore_character
#         job_score = (list_maxscore[2] / 100) * maxscore_character
#         social_status_score = (list_maxscore[3] / 100) * maxscore_character
#         income_score = (list_maxscore[4] / 100) * maxscore_capability
#         health_score = (list_maxscore[5] / 100) * maxscore_capability
#         job_stability_score = (list_maxscore[6] / 100) * maxscore_capability
#         having_debt_score = (list_maxscore[7] / 100) * maxscore_capability
#         other_debt_score = (list_maxscore[8] / 100) * maxscore_capability
#         capital_score = (list_maxscore[9] / 100) * maxscore_capital
#         asset_score = (list_maxscore[10] / 100) * maxscore_capital
#
#         print('credit_buro_score:',credit_buro_score)
#         print('region_score:',region_score)
#         print('job_score:',job_score)
#         print('social_status_score:',social_status_score)
#         print('income_score:',income_score)
#         print('health_score:',health_score)
#         print('job_stability_score:',job_stability_score)
#         print('having_debt_score:',having_debt_score)
#         print('other_debt_score:',other_debt_score)
#         print('capital_score:',capital_score)
#         print('asset_score:',asset_score)
#         print('maxscore_collateral:',maxscore_collateral)
#         print('maxscore_condition:',maxscore_condition)
#
#
#         df = pd.read_csv(list[7], encoding='TIS-620')
#         found = 'N'
#         for y in range(len(df.index)):
#              if username == df.loc[y].Username:
#                  found = 'Y'
#                  user_count_repayment = all_def.repayment(credit_buro_score, df.loc[y].repayment_history)
#                  user_count_region = all_def.region(region_score, df.loc[y].region_info)
#                  user_count_job = all_def.job(job_score, df.loc[y].job_info)
#                  user_count_social = all_def.social(social_status_score, df.loc[y].social_status)
#                  user_count_income = all_def.income(income_score, df.loc[y].revenue, df.loc[y].loan, df.loc[y].rate, df.loc[y].year)
#                  user_count_health = all_def.health(health_score, df.loc[y].health_info)
#                  user_count_job_stability = all_def.job_stability(job_stability_score, df.loc[y].job_year)
#                  user_count_having_debt = all_def.having_debt(having_debt_score, df.loc[y].pay_other_debt, df.loc[y].revenue)
#                  user_count_other_debt = all_def.other_debt(other_debt_score, df.loc[y].debt, df.loc[y].asset)
#                  user_count_capital_structure = all_def.capital_structure(capital_score, df.loc[y].asset, df.loc[y].debt)
#                  user_count_percent_asset = all_def.percent_asset(asset_score, df.loc[y].asset,df.loc[y].loan)
#                  user_count_collateral = all_def.collateral(maxscore_collateral, df.loc[y].collateral_asset, df.loc[y].loan,df.loc[y].liquidity_collateral)
#                  user_count_condition = all_def.condition(maxscore_condition, df.loc[y].percent_inflation, df.loc[y].job_info)
#
#                  sum_character = user_count_repayment + user_count_region + user_count_job + user_count_social
#                  sum_capability = user_count_income + user_count_health + user_count_job_stability + user_count_having_debt + user_count_other_debt
#                  sum_capital = user_count_capital_structure + user_count_percent_asset
#                  sum_collateral = user_count_collateral
#                  sum_condition = user_count_condition
#
#                  print(sum_character)
#                  print(sum_capability)
#                  print(sum_capital)
#                  print(sum_collateral)
#                  print(sum_condition)
#
#
#                  file_cut_off = open(list[6], 'r')  # Input เป็น Percent
#                  list_cutoff_point = []
#                  for x in file_cut_off:
#                      for y in x.split():
#                          list_cutoff_point.append(int(y))
#                  haracter_cutoffpoint = (list_cutoff_point[0] / 100) * maxscore_character
#                  capability_cutoffpoint = (list_cutoff_point[1] / 100) * maxscore_capability
#                  capital_cutoffpoint = (list_cutoff_point[2] / 100) *maxscore_capital
#                  collateral_cutoffpoint = (list_cutoff_point[3] / 100) * maxscore_collateral
#                  condition_cutoffpoint = (list_cutoff_point[4] / 100) * maxscore_condition
#                  all_cutoffpoint = (list_cutoff_point[5] / 100) * 1000
#
#
#
#
#         ### Graph from 100 Percent of each c and score that user get
#         # convert each C to percent
#         percent_character = (sum_character / maxscore_character) * 100
#         percent_capability = (sum_capability /maxscore_capability) * 100
#         percent_capital = (sum_capital / maxscore_capital) * 100
#         percent_collateral = (sum_collateral / maxscore_collateral) * 100
#         percent_condition = (sum_condition / maxscore_condition) * 100
#         all_c = ['Character', 'Capability', 'Capital', 'Collateral', 'Condition']
#         all_c = [*all_c, all_c[0]]
#         user_1 = [percent_character,percent_capability,percent_capital,percent_collateral,percent_condition]
#         user_1 = [*user_1, user_1[0]]
#         angle = np.linspace(start=0, stop=2 * np.pi, num=len(user_1))  # 2*np.pi=circle  num=5C
#         fig = plt.figure(figsize=(6, 6))  # ขนาดgraph
#         ax = fig.add_subplot(polar=True)
#         ax.plot(angle, user_1, 'o-', color='g', label='user_1')
#         ax.fill(angle, user_1, alpha=0.25, color='g')
#         ax.set_thetagrids(angle * 180 / np.pi, all_c)
#         plt.title('User overview graph ', size=20, y=1.05)  # หัวข้อกราฟ
#         lines, labels = plt.thetagrids(np.degrees(angle), labels=all_c)
#         plt.grid(True)
#         plt.tight_layout()
#         plt.legend()  #
#         plt.show()
#
#         if found == 'N':
#             print('No username')






