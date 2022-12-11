import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import pandas as pd
import all_def
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


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
        text_file_cut_off = cut_off_var.get()
        csv_loan_info = loan_info_var.get()
        username1 = username_var1.get()
        username2 = username_var2.get()


        list.append(character)
        list.append(capability)
        list.append(capital)
        list.append(collateral)
        list.append(condition)
        list.append(text_file_sub_c)
        list.append(text_file_cut_off)
        list.append(csv_loan_info)
        list.append(username1)
        list.append(username2)


        # character = list[0]
        # capability = list[1]
        # capital = list[2]
        # collateral = list[3]
        # condition = list[4]

        maxscore_character = int(character) * 10
        maxscore_capability = int(capability) * 10
        maxscore_capital = int(capital) * 10
        maxscore_collateral = int(collateral) * 10
        maxscore_condition = int(condition) * 10

        if maxscore_character+maxscore_capability+maxscore_capital+maxscore_collateral+maxscore_condition >1000:
            print('Max score more than 1000')


        # print('maxscore_character:', maxscore_character)
        # print('maxscore_capability:', maxscore_capability)
        # print('maxscore_capital:', maxscore_capital)
        # print('maxscore_collateral:', maxscore_collateral)
        # print('maxscore_condition', maxscore_condition)

        try:
            file = open(list[5], 'r')  # Input proportion of sub-C
            list_maxscore = []
            for x in file:
                for y in x.split():
                    list_maxscore.append(int(y))


            credit_buro_score = (list_maxscore[0] / 100) * maxscore_character
            region_score = (list_maxscore[1] / 100) * maxscore_character
            job_score = (list_maxscore[2] / 100) * maxscore_character
            social_status_score = (list_maxscore[3] / 100) * maxscore_character
            income_score = (list_maxscore[4] / 100) * maxscore_capability
            health_score = (list_maxscore[5] / 100) * maxscore_capability
            job_stability_score = (list_maxscore[6] / 100) * maxscore_capability
            having_debt_score = (list_maxscore[7] / 100) * maxscore_capability
            other_debt_score = (list_maxscore[8] / 100) * maxscore_capability
            capital_score = (list_maxscore[9] / 100) * maxscore_capital
            asset_score = (list_maxscore[10] / 100) * maxscore_capital

            # print('credit_buro_score:',credit_buro_score)
            # print('region_score:',region_score)
            # print('job_score:',job_score)
            # print('social_status_score:',social_status_score)
            # print('income_score:',income_score)
            # print('health_score:',health_score)
            # print('job_stability_score:',job_stability_score)
            # print('having_debt_score:',having_debt_score)
            # print('other_debt_score:',other_debt_score)
            # print('capital_score:',capital_score)
            # print('asset_score:',asset_score)
            # print('maxscore_collateral:',maxscore_collateral)
            # print('maxscore_condition:',maxscore_condition)
        except:
            print('Doesn\'t have proportion of sub c')
        scoll = []
        try:
            df = pd.read_csv(list[7], encoding='TIS-620')
            for y in range(len(df.index)):
                scoll.append(str(df.loc[y].Username))
                if username1 == df.loc[y].Username:
                    user_count_repayment1 = all_def.repayment(credit_buro_score, df.loc[y].repayment_history)
                    user_count_region1 = all_def.region(region_score, df.loc[y].region_info)
                    user_count_job1 = all_def.job(job_score, df.loc[y].job_info)
                    user_count_social1 = all_def.social(social_status_score, df.loc[y].social_status)
                    user_count_income1 = all_def.income(income_score, df.loc[y].revenue, df.loc[y].loan, df.loc[y].rate, df.loc[y].year)
                    user_count_health1 = all_def.health(health_score, df.loc[y].health_info)
                    user_count_job_stability1 = all_def.job_stability(job_stability_score, df.loc[y].job_year)
                    user_count_having_debt1 = all_def.having_debt(having_debt_score, df.loc[y].pay_other_debt, df.loc[y].revenue)
                    user_count_other_debt1 = all_def.other_debt(other_debt_score, df.loc[y].debt, df.loc[y].asset)
                    user_count_capital_structure1 = all_def.capital_structure(capital_score, df.loc[y].asset, df.loc[y].debt)
                    user_count_percent_asset1 = all_def.percent_asset(asset_score, df.loc[y].asset,df.loc[y].loan)
                    user_count_collateral1 = all_def.collateral(maxscore_collateral, df.loc[y].collateral_asset, df.loc[y].loan,df.loc[y].liquidity_collateral)
                    user_count_condition1 = all_def.condition(maxscore_condition, df.loc[y].percent_inflation, df.loc[y].job_info)


                    sum_character1 = user_count_repayment1 + user_count_region1 + user_count_job1 + user_count_social1
                    sum_capability1 = user_count_income1 + user_count_health1 + user_count_job_stability1 + user_count_having_debt1 + user_count_other_debt1
                    sum_capital1 = user_count_capital_structure1 + user_count_percent_asset1
                    sum_collateral1 = user_count_collateral1
                    sum_condition1 = user_count_condition1


                if username2 == df.loc[y].Username:
                    user_count_repayment2 = all_def.repayment(credit_buro_score, df.loc[y].repayment_history)
                    user_count_region2 = all_def.region(region_score, df.loc[y].region_info)
                    user_count_job2 = all_def.job(job_score, df.loc[y].job_info)
                    user_count_social2 = all_def.social(social_status_score, df.loc[y].social_status)
                    user_count_income2 = all_def.income(income_score, df.loc[y].revenue, df.loc[y].loan,
                                                        df.loc[y].rate, df.loc[y].year)
                    user_count_health2 = all_def.health(health_score, df.loc[y].health_info)
                    user_count_job_stability2 = all_def.job_stability(job_stability_score, df.loc[y].job_year)
                    user_count_having_debt2 = all_def.having_debt(having_debt_score, df.loc[y].pay_other_debt,
                                                                  df.loc[y].revenue)
                    user_count_other_debt2 = all_def.other_debt(other_debt_score, df.loc[y].debt, df.loc[y].asset)
                    user_count_capital_structure2 = all_def.capital_structure(capital_score, df.loc[y].asset,
                                                                              df.loc[y].debt)
                    user_count_percent_asset2 = all_def.percent_asset(asset_score, df.loc[y].asset, df.loc[y].loan)
                    user_count_collateral2 = all_def.collateral(maxscore_collateral, df.loc[y].collateral_asset,
                                                                df.loc[y].loan, df.loc[y].liquidity_collateral)
                    user_count_condition2 = all_def.condition(maxscore_condition, df.loc[y].percent_inflation,
                                                              df.loc[y].job_info)

                    sum_character2 = user_count_repayment2 + user_count_region2 + user_count_job2 + user_count_social2
                    sum_capability2 = user_count_income2 + user_count_health2 + user_count_job_stability2 + user_count_having_debt2 + user_count_other_debt2
                    sum_capital2 = user_count_capital_structure2 + user_count_percent_asset2
                    sum_collateral2 = user_count_collateral2
                    sum_condition2 = user_count_condition2

        except:
            print('Does\' have csv file')


        try:
            file_cut_off = open(list[6], 'r')  # Input เป็น Percent
            list_cutoff_point = []
            for x in file_cut_off:
                for y in x.split():
                    list_cutoff_point.append(int(y))

            ### Cut-off User1
            character_cutoffpoint = (list_cutoff_point[0] / 100) * maxscore_character
            if character_cutoffpoint <= sum_character1:
                charac_cutoff = 'Pass'
            else:
                charac_cutoff = 'Not pass'
            capability_cutoffpoint = (list_cutoff_point[1] / 100) * maxscore_capability
            if capability_cutoffpoint <= sum_capability1:
                capa_cutoff = 'Pass'
            else:
                capa_cutoff = 'Not pass'
            capital_cutoffpoint = (list_cutoff_point[2] / 100) *maxscore_capital
            if capital_cutoffpoint <= sum_capital1:
                capi_cutoff = 'Pass'
            else:
                capi_cutoff = 'Not pass'
            collateral_cutoffpoint = (list_cutoff_point[3] / 100) * maxscore_collateral
            if collateral_cutoffpoint <= sum_collateral1:
                coll_cutoff = 'Pass'
            else:
                coll_cutoff = 'Not pass'
            condition_cutoffpoint = (list_cutoff_point[4] / 100) * maxscore_condition
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

        except:
            print('Doesn\'t have cut-off point file')





        ### GUI page 2
        ### ### ###
        #try:



        user1_score = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=30)
        user1_score["font"] = ft
        user1_score["fg"] = "#333333"
        user1_score["justify"] = "center"
        user1_score["text"] = "User1 Score "
        user1_score.place(x=105, y=0, width=180, height=42)

        cutoff_point = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=33)
        cutoff_point["font"] = ft
        cutoff_point["fg"] = "#333333"
        cutoff_point["justify"] = "center"
        cutoff_point["text"] = "Summary"
        cutoff_point.place(x=252, y=0, width=224, height=51)

        user2_score = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=30)
        user2_score["font"] = ft
        user2_score["fg"] = "#333333"
        user2_score["justify"] = "center"
        user2_score["text"] = "User2 Score "
        user2_score.place(x=410, y=0, width=180, height=42)

        cutoff_point2 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=33)
        cutoff_point2["font"] = ft
        cutoff_point2["fg"] = "#333333"
        cutoff_point2["justify"] = "center"
        cutoff_point2["text"] = "Summary"
        cutoff_point2.place(x=555, y=0, width=224, height=51)

        max_score = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=33)
        max_score["font"] = ft
        max_score["fg"] = "#333333"
        max_score["justify"] = "center"
        max_score["text"] = "Max score"
        max_score.place(x=715, y=10, width=210, height=30)

        user1_charac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user1_charac["font"] = ft
        user1_charac["fg"] = "#333333"
        user1_charac["justify"] = "right"
        user1_charac["text"] = sum_character1
        user1_charac.place(x=155, y=50, width=89, height=41)

        carac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        carac["font"] = ft
        carac["fg"] = "#333333"
        carac["justify"] = "center"
        carac["text"] = "Character"
        carac.place(x=20, y=50, width=132, height=38)

        cutoff_charac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_charac["font"] = ft
        cutoff_charac["fg"] = "#333333"
        cutoff_charac["justify"] = "center"
        cutoff_charac["text"] = charac_cutoff
        cutoff_charac.place(x=300, y=50, width=89, height=41)

        user2_charac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user2_charac["font"] = ft
        user2_charac["fg"] = "#333333"
        user2_charac["justify"] = "right"
        user2_charac["text"] = sum_character2
        user2_charac.place(x=450, y=50, width=89, height=41)

        cutoff_charac2 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_charac2["font"] = ft
        cutoff_charac2["fg"] = "#333333"
        cutoff_charac2["justify"] = "center"
        cutoff_charac2["text"] = charac_cutoff2
        cutoff_charac2.place(x=590, y=50, width=89, height=41)

        capab = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        capab["font"] = ft
        capab["fg"] = "#333333"
        capab["justify"] = "center"
        capab["text"] = "Capability"
        capab.place(x=12, y=80, width=128, height=32)

        user1_capab = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user1_capab["font"] = ft
        user1_capab["fg"] = "#333333"
        user1_capab["justify"] = "right"
        user1_capab["text"] = sum_capability1
        user1_capab.place(x=125, y=80, width=173, height=30)

        cutoff_capa = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_capa["font"] = ft
        cutoff_capa["fg"] = "#333333"
        cutoff_capa["justify"] = "center"
        cutoff_capa["text"] = capa_cutoff
        cutoff_capa.place(x=260, y=80, width=173, height=30)

        user2_capab = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user2_capab["font"] = ft
        user2_capab["fg"] = "#333333"
        user2_capab["justify"] = "right"
        user2_capab["text"] = sum_capability2
        user2_capab.place(x=415, y=80, width=173, height=30)

        cutoff_capa2 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_capa2["font"] = ft
        cutoff_capa2["fg"] = "#333333"
        cutoff_capa2["justify"] = "center"
        cutoff_capa2["text"] = capa_cutoff2
        cutoff_capa2.place(x=575, y=80, width=173, height=30)

        capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        capi["font"] = ft
        capi["fg"] = "#333333"
        capi["justify"] = "right"
        capi["text"] = "Capital"
        capi.place(x=30, y=110, width=141, height=30)

        user1_capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user1_capi["font"] = ft
        user1_capi["fg"] = "#333333"
        user1_capi["justify"] = "right"
        user1_capi["text"] = sum_capital1
        user1_capi.place(x=140, y=110, width=145, height=30)

        cutoff_capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_capi["font"] = ft
        cutoff_capi["fg"] = "#333333"
        cutoff_capi["justify"] = "center"
        cutoff_capi["text"] = capi_cutoff
        cutoff_capi.place(x=265, y=110, width=145, height=30)

        user2_capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user2_capi["font"] = ft
        user2_capi["fg"] = "#333333"
        user2_capi["justify"] = "right"
        user2_capi["text"] = sum_capital2
        user2_capi.place(x=415, y=110, width=145, height=30)

        cutoff_capi2 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_capi2["font"] = ft
        cutoff_capi2["fg"] = "#333333"
        cutoff_capi2["justify"] = "center"
        cutoff_capi2["text"] = capi_cutoff2
        cutoff_capi2.place(x=575, y=110, width=145, height=30)

        coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        coll["font"] = ft
        coll["fg"] = "#333333"
        coll["justify"] = "center"
        coll["text"] = "Collateral"
        coll.place(x=15, y=140, width=132, height=31)

        user1_coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user1_coll["font"] = ft
        user1_coll["fg"] = "#333333"
        user1_coll["justify"] = "right"
        user1_coll["text"] = sum_collateral1
        user1_coll.place(x=130, y=140, width=153, height=30)

        cutoff_coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_coll["font"] = ft
        cutoff_coll["fg"] = "#333333"
        cutoff_coll["justify"] = "center"
        cutoff_coll["text"] = coll_cutoff
        cutoff_coll.place(x=260, y=140, width=153, height=30)

        user2_coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user2_coll["font"] = ft
        user2_coll["fg"] = "#333333"
        user2_coll["justify"] = "right"
        user2_coll["text"] = sum_collateral2
        user2_coll.place(x=415, y=140, width=153, height=30)

        cutoff_coll2 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_coll2["font"] = ft
        cutoff_coll2["fg"] = "#333333"
        cutoff_coll2["justify"] = "center"
        cutoff_coll2["text"] = coll_cutoff2
        cutoff_coll2.place(x=570, y=140, width=153, height=30)

        condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=20)
        condi["font"] = ft
        condi["fg"] = "#333333"
        condi["justify"] = "center"
        condi["text"] = "Condition"
        condi.place(x=20, y=170, width=128, height=30)

        user1_condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user1_condi["font"] = ft
        user1_condi["fg"] = "#333333"
        user1_condi["justify"] = "right"
        user1_condi["text"] = sum_condition1
        user1_condi.place(x=130, y=170, width=142, height=30)

        cutoff_condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_condi["font"] = ft
        cutoff_condi["fg"] = "#333333"
        cutoff_condi["justify"] = "center"
        cutoff_condi["text"] = condi_cutoff
        cutoff_condi.place(x=260, y=170, width=142, height=30)

        user2_condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=15)
        user2_condi["font"] = ft
        user2_condi["fg"] = "#333333"
        user2_condi["justify"] = "right"
        user2_condi["text"] = sum_condition2
        user2_condi.place(x=415, y=170, width=142, height=30)

        cutoff_condi2 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=23)
        cutoff_condi2["font"] = ft
        cutoff_condi2["fg"] = "#333333"
        cutoff_condi2["justify"] = "center"
        cutoff_condi2["text"] = condi_cutoff2
        cutoff_condi2.place(x=570, y=170, width=142, height=30)

        max_charac = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_charac["font"] = ft
        max_charac["fg"] = "#333333"
        max_charac["justify"] = "center"
        max_charac["text"] = maxscore_character                  ### เลือกระหว่างmax score กับ cutoff point ###
        max_charac.place(x=730, y=50, width=172, height=37)

        max_capa = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_capa["font"] = ft
        max_capa["fg"] = "#333333"
        max_capa["justify"] = "center"
        max_capa["text"] = maxscore_capability
        max_capa.place(x=735, y=80, width=169, height=30)

        max_capi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_capi["font"] = ft
        max_capi["fg"] = "#333333"
        max_capi["justify"] = "center"
        max_capi["text"] = maxscore_capital
        max_capi.place(x=745, y=110, width=137, height=30)

        max_coll = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_coll["font"] = ft
        max_coll["fg"] = "#333333"
        max_coll["justify"] = "center"
        max_coll["text"] = maxscore_collateral
        max_coll.place(x=780, y=140, width=70, height=25)

        max_condi = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=18)
        max_condi["font"] = ft
        max_condi["fg"] = "#333333"
        max_condi["justify"] = "center"
        max_condi["text"] = maxscore_condition
        max_condi.place(x=780, y=170, width=70, height=25)

        line_user1 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=35)
        line_user1["font"] = ft
        line_user1["fg"] = "#cc0000"
        line_user1["justify"] = "center"
        line_user1["text"] = 'Red line = User1'
        line_user1.place(x=450, y=350, width=300, height=30)

        line_user2 = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=35)
        line_user2["font"] = ft
        line_user2["fg"] = "#1e90ff"
        line_user2["justify"] = "center"
        line_user2["text"] = 'Blue line = User2'
        line_user2.place(x=450, y=400, width=300, height=30)

        line_cutoff = tk.Label(loan)
        ft = tkFont.Font(family='Times', size=35)
        line_cutoff["font"] = ft
        line_cutoff["fg"] = "#009688"
        line_cutoff["justify"] = "center"
        line_cutoff["text"] = 'Green line = Cut-Off Point'
        line_cutoff.place(x=450, y=450, width=300, height=30)
        #except:
            #print('Invalid Username')


        #### Summary graph
        s = ttk.Style()
        s.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(loan, column=('User1 Score', 'Summary', 'User2 Score', 'Summary', 'Max Score'),
                            show='headings', height=15)

        tree.column("# 1", anchor='center')
        tree.heading("# 1", text='User1 Score')
        tree.column("# 2", anchor='center')
        tree.heading("# 2", text='Summary')
        tree.column("# 3", anchor='center')
        tree.heading("# 3", text='User2 Score')
        tree.column("# 4", anchor='center')
        tree.heading("# 4", text='Summary')
        tree.column("# 5", anchor='center')
        tree.heading("# 5", text='Max Score')

        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=(str(sum_character1), charac_cutoff, str(sum_character2), charac_cutoff2, str(maxscore_character)))
        tree.insert('', 'end', text="2", values=(
        str(sum_capability1), capa_cutoff, str(sum_capability2), capa_cutoff2, str(maxscore_capability)))
        tree.insert('', 'end', text="3",
                    values=(str(sum_capital1), capi_cutoff, str(sum_capital2), capi_cutoff2, str(maxscore_capital)))
        tree.insert('', 'end', text="4", values=(
        str(sum_collateral1), coll_cutoff, str(sum_capability2), coll_cutoff2, str(maxscore_capability)))
        tree.insert('', 'end', text="5", values=(
        str(sum_condition1), condi_cutoff, str(sum_condition2), condi_cutoff2, str(maxscore_condition)))

        tree.place(x=20, y=50, width=875, height=200)

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
        cut_off_in100 = [int(list_cutoff_point[0]), int(list_cutoff_point[1]),int(list_cutoff_point[2]),int(list_cutoff_point[3]),int(list_cutoff_point[4])]  # สัดส่วนpercentของuser2
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
        graph_show.get_tk_widget().place(x=35, y=250, width=350, height=350) # x,y = placeในGUI   ##width,hight = ขนาดรูปของกราฟ


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


list = []
GLabel_221 = tk.Label(root)                # Input proportion of each C
ft = tkFont.Font(family='Times', size=18)
GLabel_221["font"] = ft
GLabel_221["fg"] = "#333333"
GLabel_221["justify"] = "center"
GLabel_221["text"] = "Input proportion of each C"
GLabel_221.place(x=20, y=50, width=270, height=30)

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
GLabel_118.place(x=0, y=130, width=230, height=30)

text_file_sub_c = tk.StringVar()
sub_c_var = tk.Entry(root,textvariable=text_file_sub_c)     # Entry sub c
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
GLabel_507.place(x=240, y=130, width=185, height=30)

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
GLabel_987.place(x=330, y=160, width=70, height=30)

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
GLabel_307.place(x=510, y=160, width=75, height=25)

user1 = tk.Label(root)                                # pick User
ft = tkFont.Font(family='Times', size=21)
user1["font"] = ft
user1["fg"] = "#333333"
user1["justify"] = "center"
user1["text"] = "Pick user1 "
user1.place(x=50, y=220, width=130, height=30)

username1 = tk.StringVar()
username_var1 = tk.Entry(root,textvariable= username1)      # Entry username1
username_var1["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=23)
username_var1["font"] = ft
username_var1["fg"] = "#333333"
username_var1["justify"] = "center"
username_var1.place(x=180, y=220, width=81, height=30)

user2 = tk.Label(root)                                          # pick User2
ft = tkFont.Font(family='Times', size=21)
user2["font"] = ft
user2["fg"] = "#333333"
user2["justify"] = "center"
user2["text"] = "Pick user2 "
user2.place(x=50, y=275, width=130 ,height=30)

username2 = tk.StringVar()
username_var2 = tk.Entry(root,textvariable= username2)          # Entry username
username_var2["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=23)
username_var2["font"] = ft
username_var2["fg"] = "#333333"
username_var2["justify"] = "center"
username_var2.place(x=180, y=275, width=81, height=30)


submit = tk.Radiobutton(root,command= App)                      # Submit all info
submit["bg"] = "#cc0000"
ft = tkFont.Font(family='Times', size=23)
submit["font"] = ft
submit["fg"] = "#333333"
submit["justify"] = "center"
submit["text"] = "Submit"
submit.place(x=275,y=275,width=120,height=30)






root.mainloop()
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
#
















# # #Backup
# # Run program
# character = character_var.get()
# capability = capability_var.get()
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






