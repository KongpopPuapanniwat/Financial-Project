import re
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import pandas as pd
import all_def
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from tkinter import END


class App:
    def __init__(self):
        loan = tk.Tk()
        # setting title
        loan.title('Risk Lending Assessment Program')

        # setting window size
        width = 900
        height = 650
        screenwidth = loan.winfo_screenwidth()
        screenheight = loan.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        loan.geometry(alignstr)
        loan.resizable(width=False, height=False)


        character = character_var.get()
        capability = capability_var.get()
        capital = capital_var.get()
        collateral = collateral_var.get()
        condition = condition_var.get()
        text_file_sub_c = sub_c_var.get()
        csv_loan_info = loan_info_var.get()
        print('cvs file:',csv_loan_info)


        global user1
        global user2
        print(user1)
        print(user2)

        list.append(character)
        list.append(capability)
        list.append(capital)
        list.append(collateral)
        list.append(condition)
        list.append(text_file_sub_c)
        list.append(csv_loan_info)
        #print(list)


        maxscore_character = int(character) * 10
        maxscore_capability = int(capability) * 10
        maxscore_capital = int(capital) * 10
        maxscore_collateral = int(collateral) * 10
        maxscore_condition = int(condition) * 10

        if maxscore_character+maxscore_capability+maxscore_capital+maxscore_collateral+maxscore_condition >1000:
            print('Max score more than 1000')


        try:
            file = open(list[5], 'r')  # Input proportion of sub-C & cut off
            list_maxscore_and_cutoff = []
            for x in file:
                for y in x.split():
                    list_maxscore_and_cutoff.append(int(y))

            #print(list_maxscore_and_cutoff)
            credit_buro_score = (list_maxscore_and_cutoff[0] / 100) * maxscore_character
            region_score = (list_maxscore_and_cutoff[1] / 100) * maxscore_character
            job_score = (list_maxscore_and_cutoff[2] / 100) * maxscore_character
            social_status_score = (list_maxscore_and_cutoff[3] / 100) * maxscore_character
            income_score = (list_maxscore_and_cutoff[4] / 100) * maxscore_capability
            health_score = (list_maxscore_and_cutoff[5] / 100) * maxscore_capability
            job_stability_score = (list_maxscore_and_cutoff[6] / 100) * maxscore_capability
            having_debt_score = (list_maxscore_and_cutoff[7] / 100) * maxscore_capability
            other_debt_score = (list_maxscore_and_cutoff[8] / 100) * maxscore_capability
            capital_score = (list_maxscore_and_cutoff[9] / 100) * maxscore_capital
            asset_score = (list_maxscore_and_cutoff[10] / 100) * maxscore_capital
            character_cutoffpoint = (list_maxscore_and_cutoff[11] / 100) * maxscore_character
            capability_cutoffpoint = (list_maxscore_and_cutoff[12] / 100) * maxscore_capability
            capital_cutoffpoint = (list_maxscore_and_cutoff[13] / 100) * maxscore_capital
            collateral_cutoffpoint = (list_maxscore_and_cutoff[14] / 100) * maxscore_collateral
            condition_cutoffpoint = (list_maxscore_and_cutoff[15] / 100) * maxscore_condition

        except:
            print('Doesn\'t have proportion of sub c')

        try:
            df1 = pd.read_csv(csv_loan_info, encoding='TIS-620')
            #print(len(df1.index))
            for y in range(len(df1.index)):
                if str(user1) == df1.loc[y].Username:
                    #print(user1)
                    #print(df1.loc[y].Username)
                    user_count_repayment1 = all_def.repayment(credit_buro_score, df1.loc[y].repayment_history)
                    user_count_region1 = all_def.region(region_score, df1.loc[y].region_info)
                    user_count_job1 = all_def.job(job_score, df1.loc[y].job_info)
                    user_count_social1 = all_def.social(social_status_score, df1.loc[y].social_status)
                    user_count_income1 = all_def.income(income_score, df1.loc[y].revenue, df1.loc[y].loan, df1.loc[y].rate, df1.loc[y].year)
                    user_count_health1 = all_def.health(health_score, df1.loc[y].health_info)
                    user_count_job_stability1 = all_def.job_stability(job_stability_score, df1.loc[y].job_year)
                    user_count_having_debt1 = all_def.having_debt(having_debt_score, df1.loc[y].pay_other_debt, df1.loc[y].revenue)
                    user_count_other_debt1 = all_def.other_debt(other_debt_score, df1.loc[y].debt, df1.loc[y].asset)
                    user_count_capital_structure1 = all_def.capital_structure(capital_score, df1.loc[y].asset, df1.loc[y].debt)
                    user_count_percent_asset1 = all_def.percent_asset(asset_score, df1.loc[y].asset,df1.loc[y].loan)
                    user_count_collateral1 = all_def.collateral(maxscore_collateral, df1.loc[y].collateral_asset, df1.loc[y].loan,df1.loc[y].liquidity_collateral)
                    user_count_condition1 = all_def.condition(maxscore_condition, df1.loc[y].percent_inflation, df1.loc[y].job_info)


                    sum_character1 = user_count_repayment1 + user_count_region1 + user_count_job1 + user_count_social1
                    sum_capability1 = user_count_income1 + user_count_health1 + user_count_job_stability1 + user_count_having_debt1 + user_count_other_debt1
                    sum_capital1 = user_count_capital_structure1 + user_count_percent_asset1
                    sum_collateral1 = user_count_collateral1
                    sum_condition1 = user_count_condition1


                if str(user2) == df1.loc[y].Username:
                    user_count_repayment2 = all_def.repayment(credit_buro_score, df1.loc[y].repayment_history)
                    user_count_region2 = all_def.region(region_score, df1.loc[y].region_info)
                    user_count_job2 = all_def.job(job_score, df1.loc[y].job_info)
                    user_count_social2 = all_def.social(social_status_score, df1.loc[y].social_status)
                    user_count_income2 = all_def.income(income_score, df1.loc[y].revenue, df1.loc[y].loan,
                                                        df1.loc[y].rate, df1.loc[y].year)
                    user_count_health2 = all_def.health(health_score, df1.loc[y].health_info)
                    user_count_job_stability2 = all_def.job_stability(job_stability_score, df1.loc[y].job_year)
                    user_count_having_debt2 = all_def.having_debt(having_debt_score, df1.loc[y].pay_other_debt,
                                                                  df1.loc[y].revenue)
                    user_count_other_debt2 = all_def.other_debt(other_debt_score, df1.loc[y].debt, df1.loc[y].asset)
                    user_count_capital_structure2 = all_def.capital_structure(capital_score, df1.loc[y].asset,
                                                                              df1.loc[y].debt)
                    user_count_percent_asset2 = all_def.percent_asset(asset_score, df1.loc[y].asset, df1.loc[y].loan)
                    user_count_collateral2 = all_def.collateral(maxscore_collateral, df1.loc[y].collateral_asset,
                                                                df1.loc[y].loan, df1.loc[y].liquidity_collateral)
                    user_count_condition2 = all_def.condition(maxscore_condition, df1.loc[y].percent_inflation,
                                                              df1.loc[y].job_info)

                    sum_character2 = user_count_repayment2 + user_count_region2 + user_count_job2 + user_count_social2
                    sum_capability2 = user_count_income2 + user_count_health2 + user_count_job_stability2 + user_count_having_debt2 + user_count_other_debt2
                    sum_capital2 = user_count_capital_structure2 + user_count_percent_asset2
                    sum_collateral2 = user_count_collateral2
                    sum_condition2 = user_count_condition2

        except:
            print('Does\'t have csv file')



        ### Cut-off User1
        if character_cutoffpoint <= sum_character1:
            charac_cutoff = 'Pass'

        else:
            charac_cutoff = 'Not pass'
        if capability_cutoffpoint <= sum_capability1:
            capa_cutoff = 'Pass'

        else:
            capa_cutoff = 'Not pass'

        if capital_cutoffpoint <= sum_capital1:
            capi_cutoff = 'Pass'
        else:
            capi_cutoff = 'Not pass'

        if collateral_cutoffpoint <= sum_collateral1:
            coll_cutoff = 'Pass'
        else:
            coll_cutoff = 'Not pass'

        if condition_cutoffpoint <= sum_condition1:
            condi_cutoff = 'Pass'
        else:
            condi_cutoff = 'Not pass'

        ### Cut-off point user2
        if character_cutoffpoint <= sum_character2:
            charac_cutoff2 = 'Pass'
        else:
            charac_cutoff2 = 'Not pass'

        if capability_cutoffpoint <= sum_capability2:
            capa_cutoff2 = 'Pass'
        else:
            capa_cutoff2 = 'Not pass'

        if capital_cutoffpoint <= sum_capital2:
            capi_cutoff2 = 'Pass'
        else:
            capi_cutoff2 = 'Not pass'

        if collateral_cutoffpoint <= sum_collateral2:
            coll_cutoff2 = 'Pass'
        else:
            coll_cutoff2 = 'Not pass'

        if condition_cutoffpoint <= sum_condition2:
            condi_cutoff2 = 'Pass'
        else:
            condi_cutoff2 = 'Not pass'



        ### GUI page 2
        ### ### ###
        try:
            final = tk.Label(loan)
            ft = tkFont.Font(family='Times', size=80)
            final["font"] = ft
            final["fg"] = "#333333"
            final["justify"] = "center"
            final["text"] = 'Summary'
            final.place(x=15, y=5, width=150, height=30)

            line_user1 = tk.Label(loan)
            ft = tkFont.Font(family='Times', size=35)
            line_user1["font"] = ft
            line_user1["fg"] = "#cc0000"
            line_user1["justify"] = "center"
            line_user1["text"] = 'Red line = ' + str(user1)
            line_user1.place(x=475, y=350, width=300, height=30)

            line_user2 = tk.Label(loan)
            ft = tkFont.Font(family='Times', size=35)
            line_user2["font"] = ft
            line_user2["fg"] = "#1e90ff"
            line_user2["justify"] = "center"
            line_user2["text"] = 'Blue line = ' + str(user2)
            line_user2.place(x=475, y=400, width=300, height=30)

            line_cutoff = tk.Label(loan)
            ft = tkFont.Font(family='Times', size=35)
            line_cutoff["font"] = ft
            line_cutoff["fg"] = "#009688"
            line_cutoff["justify"] = "center"
            line_cutoff["text"] = 'Green line = Cut-Off Point'
            line_cutoff.place(x=505, y=450, width=300, height=30)
        except:
            print('Invalid Username')


        #### Summary graph
        s = ttk.Style()
        s.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(loan, column=('Type of C',str(user1), 'Summary',str(user2), 'Summary', 'Max Score'),
                            show='headings', height=30)
        tree.column("# 1",width=100 ,anchor='center')
        tree.heading("# 1", text='')
        tree.column("# 2",width=100 ,anchor='center')
        tree.heading("# 2", text=str(user1))
        tree.column("# 3",width=100 ,anchor='center')
        tree.heading("# 3", text='Summary')
        tree.column("# 4",width=100 ,anchor='center')
        tree.heading("# 4", text=str(user2))
        tree.column("# 5",width=100 ,anchor='center')
        tree.heading("# 5", text='Summary')
        tree.column("# 6", width=100,anchor='center')
        tree.heading("# 6", text='Max Score')

        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1" ,values=('Character',str(sum_character1), charac_cutoff, str(sum_character2), charac_cutoff2, str(maxscore_character)))
        tree.insert('', 'end', text="2", values=('Capability',
        str(sum_capability1), capa_cutoff, str(sum_capability2), capa_cutoff2, str(maxscore_capability)))
        tree.insert('', 'end', text="3",
                    values=('Capital',str(sum_capital1), capi_cutoff, str(sum_capital2), capi_cutoff2, str(maxscore_capital)))
        tree.insert('', 'end', text="4", values=('Collateral',
        str(sum_collateral1), coll_cutoff, str(sum_capability2), coll_cutoff2, str(maxscore_capability)))
        tree.insert('', 'end', text="5", values=('Condition',
        str(sum_condition1), condi_cutoff, str(sum_condition2), condi_cutoff2, str(maxscore_condition)))

        tree.place(x=20, y=50, width=850, height=180)

        ### Graph from 100 Percent of each c and score that user get
        # convert each C to percent
        percent_character1 = (sum_character1 / maxscore_character) * 100
        percent_capability1 = (sum_capability1 / maxscore_capability) * 100
        percent_capital1 = (sum_capital1 / maxscore_capital) * 100
        percent_collateral1 = (sum_collateral1 / maxscore_collateral) * 100
        percent_condition1 = (sum_condition1 / maxscore_condition) * 100

        percent_character2 = (sum_character2 / maxscore_character) * 100
        percent_capability2 = (sum_capability2 / maxscore_capability) * 100
        percent_capital2 = (sum_capital2 / maxscore_capital) * 100
        percent_collateral2 = (sum_collateral2 / maxscore_collateral) * 100
        percent_condition2 = (sum_condition2 / maxscore_condition) * 100



        all_c_in100 = ['Character', 'Capability', 'Capital', 'Collateral', 'Condition']
        all_c_in100 = [*all_c_in100, all_c_in100[0]] #ลำดับข้อมูลทำกราฟ
        user_1_in100 = [percent_character1, percent_capability1, percent_capital1, percent_collateral1, percent_condition1] #สัดส่วนpercentของuser1
        user_1_in100 = [*user_1_in100, user_1_in100[0]] #ลำดับข้อมูลของuser
        user_2_in100 = [percent_character2, percent_capability2, percent_capital2, percent_collateral2, percent_condition2] #สัดส่วนpercentของuser2
        user_2_in100 = [*user_2_in100, user_2_in100[0]] #ลำดับข้อมูลของuser
        cut_off_in100 = [int(list_maxscore_and_cutoff[11]), int(list_maxscore_and_cutoff[12]),int(list_maxscore_and_cutoff[13]),int(list_maxscore_and_cutoff[14]),int(list_maxscore_and_cutoff[15])]  # สัดส่วนpercentของuser2
        cut_off_in100= [*cut_off_in100, cut_off_in100[0]]  # ลำดับข้อมูลของuser
        angle = np.linspace(start=0, stop=2 * np.pi, num=len(all_c_in100))  #เส้นกราฟ จากจุด 5 จุด   2*np.pi=circle  num=5C
        fig1 = plt.figure(figsize=(4, 4),dpi = 100)  # ขนาดgraph
        ax1 = fig1.add_subplot(polar=True)
        ax1.plot(angle, user_1_in100, 'o-', color='r',label='user_1_in100') #, label='User1')  #เส้นกราฟ ของuser เป็น sub-plot
        ax1.plot(angle,user_2_in100,'o-', color='b',label='user_2_in100')
        ax1.plot(angle,cut_off_in100,'o-',color='g',label='cut_off')
        ax1.fill(angle, user_1_in100, alpha=0.25, color='r')
        ax1.fill(angle, user_2_in100, alpha=0.25, color='b')
        ax1.fill(angle,cut_off_in100,alpha=0.25,color='g')
        ax1.set_thetagrids(angle * 180 / np.pi, all_c_in100)
        plt.title('Percent score from max score ', size=14,x=0.6 ,y=1.15)  # หัวข้อกราฟ
        lines, labels = plt.thetagrids(np.degrees(angle), labels=all_c_in100)
        plt.grid(True)
        plt.tight_layout() #margin ของกราฟเพื่อความเเม่นยำ
        #plt.legend() #ใช้รันlabelใน ax.plot
        graph_show = FigureCanvasTkAgg(fig1, loan)  ### คำสั่งทำหน้าที่รันกราฟเป็นรูปในหน้า tkinter (loan)
        graph_show.get_tk_widget().place(x=75, y=250, width=400, height=375) # x,y = placeในGUI   ##width,hight = ขนาดรูปของกราฟ


        print('Program done')

# setting title
print('Start')
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

#defind image
bg = tk.PhotoImage(file='D:\FinancialProject\Financial-Project\Background financial.png')

#create label
my_label =tk.Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

scroll = []
user_list = []
user1 = ''
user2 = ''
def read_csv():
    csv_loan_info = loan_info_var.get()
    df = pd.read_csv(csv_loan_info, encoding='TIS-620')
    for y in range(len(df.index)):
        scroll.append(str(df.loc[y].Username))
    scroll.sort()

    ### Pick User1
    frame1 = tk.Frame(root)
    scrollbar1 = tk.Scrollbar(frame1, orient='vertical')
    listbox1 = tk.Listbox(frame1, width=15, yscrollcommand=scrollbar1.set)
    # configure scroll bar
    scrollbar1.config(command=listbox1.yview)
    scrollbar1.pack(side='right', fill='y')
    frame1.place(x=165, y=215, width=90, height=90)
    listbox1.pack(pady=15)

    # add item to list
    for x in scroll:
        listbox1.insert('end', x)
    def select1():
        global user1
        for i in listbox1.curselection():
            user_get1 = listbox1.get(i)
            user1 = user_get1

    button1 = tk.Button(root, text='Select', command=select1)
    button1.place(x=75, y=275, width=50, height=30)




    ### Pick User2
    frame2 = tk.Frame(root)
    scrollbar2 = tk.Scrollbar(frame2, orient='vertical')
    listbox2 = tk.Listbox(frame2, width=15, yscrollcommand=scrollbar2.set)
    # configure scroll bar
    scrollbar2.config(command=listbox2.yview)
    scrollbar2.pack(side='right', fill='y')
    frame2.place(x=425, y=215, width=90, height=90)
    listbox2.pack(pady=15)

    # add item to list
    for x in scroll:
        listbox2.insert('end', x)

    def select2():
        global user2
        for i in listbox2.curselection():
            user_get2 = listbox2.get(i)
            user2 = user_get2

    button2 = tk.Button(root, text='Select', command=select2)
    button2.place(x=325, y=275, width=50, height=30)



list = []
GLabel_221 = tk.Label(root)                                     # Input proportion of each C
ft = tkFont.Font(family='Times', size=18)
GLabel_221["font"] = ft
GLabel_221["fg"] = "#fcfcfc"
GLabel_221["bg"] = "#0B0B42"
GLabel_221["justify"] = "center"
GLabel_221["text"] = "Input proportion of each C"
GLabel_221.place(x=20, y=50, width=270, height=30)

GLabel_430 = tk.Label(root)                                      # Risk lending assessment program
ft = tkFont.Font(family='Times', size=28)
GLabel_430["font"] = ft
GLabel_430["fg"] = "#fcfcfc"
GLabel_430["bg"] = "#0B0B42"
GLabel_430["justify"] = "center"
GLabel_430["text"] = "Risk lending assessment program"
GLabel_430.place(x=50, y=10, width=511, height=40)

GLabel_810 = tk.Label(root)                                      # Character
GLabel_810["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_810["font"] = ft
GLabel_810["fg"] = "#fcfcfc"
GLabel_810["justify"] = "center"
GLabel_810["text"] = "Character"
GLabel_810.place(x=60, y=95, width=58, height=30)

character = tk.IntVar()                                         # Entry Character
character_var = tk.Entry(root,textvariable=character)
character_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
character_var["font"] = ft
character_var["fg"] = "#333333"
character_var["justify"] = "center"
character_var.place(x=10, y=95, width=52, height=30)

capability = tk.IntVar()                                        # Entry Capability
capability_var = tk.Entry(root,textvariable = capability)
capability_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
capability_var["font"] = ft
capability_var["fg"] = "#333333"
capability_var["justify"] = "center"
capability_var.place(x=130, y=95, width=49, height=30)

GLabel_99 = tk.Label(root)                                      # capability
GLabel_99["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_99["font"] = ft
GLabel_99["fg"] = "#fcfcfc"
GLabel_99["justify"] = "center"
GLabel_99["text"] = "Capability"
GLabel_99.place(x=180, y=95, width=55, height=30)

capital = tk.IntVar()                                           # Entry capital
capital_var = tk.Entry(root,textvariable = capital)
capital_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
capital_var["font"] = ft
capital_var["fg"] = "#333333"
capital_var["justify"] = "center"
capital_var.place(x=250, y=95, width=51, height=30)

GLabel_739 = tk.Label(root)                                     # Capital
GLabel_739["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_739["font"] = ft
GLabel_739["fg"] = "#fcfcfc"
GLabel_739["justify"] = "center"
GLabel_739["text"] = "Capital"
GLabel_739.place(x=300, y=95, width=50, height=30)

collateral = tk.IntVar()                                      # Entry Collateral
collateral_var = tk.Entry(root,textvariable = collateral)
collateral_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
collateral_var["font"] = ft
collateral_var["fg"] = "#333333"
collateral_var["justify"] = "center"
collateral_var.place(x=360, y=95, width=51, height=30)

GLabel_932 = tk.Label(root)                                   # Collateral
GLabel_932["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_932["font"] = ft
GLabel_932["fg"] = "#fcfcfc"
GLabel_932["justify"] = "center"
GLabel_932["text"] = "Collateral"
GLabel_932.place(x=410, y=95, width=62, height=30)

condition = tk.IntVar()                                       # Entry Condition
condition_var = tk.Entry(root,textvariable = condition)
condition_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
condition_var["font"] = ft
condition_var["fg"] = "#333333"
condition_var["justify"] = "center"
condition_var.place(x=480, y=95, width=50, height=30)

GLabel_666 = tk.Label(root)                                     # Condition
GLabel_666["bg"] = "#01aaed"
ft = tkFont.Font(family='Times', size=9)
GLabel_666["font"] = ft
GLabel_666["fg"] = "#fcfcfc"
GLabel_666["justify"] = "center"
GLabel_666["text"] = "Condition"
GLabel_666.place(x=530, y=95, width=55, height=30)

GLabel_118 = tk.Label(root)                                     # Label sub C
ft = tkFont.Font(family='Times', size=16)
GLabel_118["font"] = ft
GLabel_118["fg"] = "#fcfcfc"
GLabel_118["bg"] = "#0B0B42"
GLabel_118["justify"] = "center"
GLabel_118["text"] = "Proportion of sub C & Cut-off"
GLabel_118.place(x=20, y=145, width=270, height=30)

text_file_sub_c = tk.StringVar()
sub_c_var = tk.Entry(root,textvariable=text_file_sub_c)         # Entry sub c and Cut-off
sub_c_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=18)
sub_c_var["font"] = ft
sub_c_var["fg"] = "#333333"
sub_c_var["justify"] = "center"
sub_c_var.place(x=30, y=180, width=180, height=25)

GLabel_692 = tk.Label(root)                                     # Label textfile sub c and Cut-off
GLabel_692["bg"] = "#c71585"
ft = tkFont.Font(family='Times', size=18)
GLabel_692["font"] = ft
GLabel_692["fg"] = "#fcfcfc"
GLabel_692["justify"] = "center"
GLabel_692["text"] = "text file"
GLabel_692.place(x=200, y=180, width=85, height=25)



GLabel_865 = tk.Label(root)                                     # Label Input loan info
ft = tkFont.Font(family='Times', size=18)
GLabel_865["font"] = ft
GLabel_865["fg"] = "#fcfcfc"
GLabel_865["bg"] = "#0B0B42"
GLabel_865["justify"] = "center"
GLabel_865["text"] = "Input loaner info"
GLabel_865.place(x=320, y=145, width=180, height=30)

csv_loan_info = tk.StringVar()                                  # Entry loan info
loan_info_var = tk.Entry(root,textvariable= csv_loan_info)
loan_info_var["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=18)
loan_info_var["font"] = ft
loan_info_var["fg"] = "#333333"
loan_info_var["justify"] = "center"
loan_info_var.place(x=320, y=180, width=180, height=25)

GLabel_307 = tk.Button(root,command=read_csv)                   # Button to input csv loan info
GLabel_307["bg"] = "#cc0000"
ft = tkFont.Font(family='Times', size=18)
GLabel_307["font"] = ft
GLabel_307["fg"] = "#fcfcfc"
GLabel_307["justify"] = "center"
GLabel_307["text"] = "csv file"
GLabel_307.place(x=495, y=180, width=75, height=25)

user_1 = tk.Label(root)                                          # Label pick User 1
ft = tkFont.Font(family='Times', size=21)
user_1["font"] = ft
user_1["fg"] = "#fcfcfc"
user_1["bg"] = "#0B0B42"
user_1["justify"] = "center"
user_1["text"] = "Pick user1 "
user_1.place(x=30, y=230, width=130, height=30)

user_2 = tk.Label(root)                                          # Lebal pick User2
ft = tkFont.Font(family='Times', size=21)
user_2["font"] = ft
user_2["fg"] = "#fcfcfc"
user_2["bg"] = "#0B0B42"
user_2["justify"] = "center"
user_2["text"] = "Pick user2 "
user_2.place(x=295, y=230, width=130 ,height=30)


submit = tk.Radiobutton(root,command= App)                      # Submit all info
submit["bg"] = "#cc0000"
ft = tkFont.Font(family='Times', size=30)
submit["font"] = ft
submit["fg"] = "#fcfcfc"
submit["justify"] = "center"
submit["text"] = "Submit"
submit.place(x=200,y=385,width=200,height=50)


root.mainloop()
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
#














