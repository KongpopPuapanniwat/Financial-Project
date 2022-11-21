def repayment(credit_buro_score,repayment_history): #refered by credit Buro
    if repayment_history == 'ไม่เคยค้าง':
        count_repayment = credit_buro_score
    elif repayment_history == 'เคยค้างในอดีต ปัจจุบันปกติ':
        count_repayment = 0.8 * credit_buro_score
    elif repayment_history == 'เคยค้างในอดีต ปิดบัญชี':
        count_repayment = 0.6 * credit_buro_score
    elif repayment_history == 'เคยค้างชำระ เข้าโครงการพักชำระหนี้':
        count_repayment = 0.4 * credit_buro_score
    elif repayment_history == 'ค้างชำระ':
        count_repayment = 0.2 * credit_buro_score
    else:
        count_repayment = 9999
        print('Error Invalid input')
    return count_repayment


def region(region_score,region_info):  #refered by Household Debt.
    if region_info == 'Middle': # 35%
        count_region = region_score
    elif region_info == 'South': #42%
        count_region = 0.75 * region_score
    elif region_info == 'North': #49%
        count_region = 0.5 * region_score
    elif region_info == 'East': #61%
        count_region = 0.25 * region_score
    else:
        count_region = 9999
        print('Error Invalid input')
    return count_region


def job(job_score,job_info):  #reference by trouble liquidity to payback loan
    if job_info == 'Specialist': # 31.8%
        count_job = job_score
    elif job_info == 'Employee': #50%
        count_job = 0.8 * job_score
    elif job_info == 'Non-agricultural business ': #53.7%
        count_job = 0.6 * job_score
    elif job_info == 'Agricultural business': #59.3%
        count_job = 0.4 * job_score
    else:
        count_job = 9999
        print('Error Invalid input')
    return count_job


def social(social_status_score,social_status): #refered by social status which can tell capability to payback
    if social_status == 'Upper-upper':
        count_social = social_status_score
    elif social_status == 'Lower-upper':
        count_social = 0.8 * social_status_score
    elif social_status == 'Upper-middle':
        count_social = 0.6 * social_status_score
    elif social_status == 'Lower-middle':
        count_social = 0.4 * social_status_score
    elif social_status == 'Lower':
        count_social = 0.2 * social_status_score
    else:
        count_social = 9999
        print('Error Invalid input')
    return count_social


def income(income_score,revenue,loan,rate,year):  #refered by income each month whick can tell capability to paydebt
    month_payback = year * 12  #จำนวนงวด
    paydebt = (loan * ((1 + (rate / 100)) ** year)) / month_payback
    rate_paydebt = round(((paydebt/revenue)*100),2)
    if rate_paydebt > 30:
        count_income = 0
    elif 30 >= rate_paydebt > 25:
        count_income = 0.2 * income_score
    elif 25 >= rate_paydebt > 20:
        count_income = 0.4 * income_score
    elif 20 >= rate_paydebt >15:
        count_income = 0.6 * income_score
    elif 15>= rate_paydebt > 10:
        count_income = 0.8 * income_score
    elif 10 >= rate_paydebt:
        count_income = income_score
    else:
        count_income = 9999
        print('Error Invalid input')
    return count_income


def health(health_score,health_info):  #refered bycapability to payback
    if health_info == 'Good health':
        count_health = health_score
    elif health_info == 'Non-serious disease':
        count_health = 0.8 * health_score
    elif health_info == 'Serious disease':
        count_health = 0.5 * health_score
    else:
        count_health = 9999
        print('Error Invalid input')
    return count_health


def job_stability(job_stability_score,job_year):   #refered by stability of income
    if job_year > 10:
        count_job_stability = job_stability_score
    elif 10 >= job_year > 5:
        count_job_stability = 0.8 * job_stability_score
    elif 5 >=job_year > 3:
        count_job_stability = 0.6 * job_stability_score
    elif 3 >= job_year >= 1:
        count_job_stability = 0.5 * job_stability_score
    elif  job_year == 0:
        count_job_stability =  0.25 * job_stability_score
    else:
        count_job_stability = 9999
        print('Error Invalid input')
    return count_job_stability


def having_debt(having_debt_score,pay_other_debt,revenue): #capability to pay other debt / income
    percent_debt = (pay_other_debt / revenue) *100
    if 10 > percent_debt >= 0:
        count_having_debt = having_debt_score
    elif 10 >= percent_debt > 5:
        count_having_debt = 0.8 * having_debt_score
    elif 15 >= percent_debt > 10:
        count_having_debt = 0.6 * having_debt_score
    elif 20 >= percent_debt > 15:
        count_having_debt = 0.4 * having_debt_score
    elif 25 >= percent_debt > 20:
        count_having_debt = 0.2 * having_debt_score
    elif percent_debt > 25:
        count_having_debt = 0
    else:
        count_having_debt = 9999
        print('Error Invalid input')
    return count_having_debt


def other_debt(other_debt_score,debt,asset): #proportion of other debt / asset loaner have
    percent_other_debt = (debt/asset)*100
    if 25 >= percent_other_debt >= 0:
        count_other_debt = other_debt_score
    elif 50 >= percent_other_debt > 25:
        count_other_debt = 0.75 * other_debt_score
    elif 75 >= percent_other_debt > 50:
        count_other_debt = 0.5 * other_debt_score
    elif 100 >= percent_other_debt > 75:
        count_other_debt = 0.25 * other_debt_score
    elif percent_other_debt > 100:
        count_other_debt = 0
    else:
        count_other_debt = 9999
        print('Error Invalid input')
    return count_other_debt

#debt means other debt
def capital_structure(capital_score,asset,debt):  #structure of money laoner have which can tell financial stability
    capital = asset - debt                       #if other debt more than capital it implied that loaner may cant afford  other debt
    if capital > debt:
        count_capital_structure = capital_score
    elif capital < debt:
        count_capital_structure = 0.25 * capital_score
    else:
        count_capital_structure = 9999
        print('Error Invalid input')
    return count_capital_structure


def percent_asset(asset_score,asset,loan): #referenced by proportion of loan / asset
    percent_fund = (loan /asset) *100
    if 50 > percent_fund >= 0 :
        count_percent_asset = asset_score
    elif 75 > percent_fund >= 50:
        count_percent_asset = 0.75 * asset_score
    elif 100 > percent_fund >= 75:
        count_percent_asset = 0.5 * asset_score
    elif 120 > percent_fund >= 100:
        count_percent_asset = 0.25 * asset_score
    elif percent_fund > 120:
        count_percent_asset = 0
    else:
        count_percent_asset = 9999
        print('Error Invalid input')
    return count_percent_asset

# refered by proportion of collateral and amount of loan loaner ask and liquidity of collateral asset
def collateral(maxscore_collateral,collateral_asset,loan,liquidity_collateral):
    percent_collateral = (loan /collateral_asset) *100
    if 25 > percent_collateral >= 0 :
        if liquidity_collateral == 'High':
            count_collateral = maxscore_collateral
        elif liquidity_collateral == 'Low':
            count_collateral = 0.8 * maxscore_collateral

    elif 50 > percent_collateral >= 25:
        if liquidity_collateral == 'High':
            count_collateral = 0.75 * maxscore_collateral
        elif liquidity_collateral == 'Low':
            count_collateral = 0.6 * maxscore_collateral

    elif 75 > percent_collateral >= 50:
        if liquidity_collateral == 'High':
            count_collateral = 0.5 *maxscore_collateral
        elif liquidity_collateral == 'Low':
            count_collateral = 0.4 * maxscore_collateral

    elif 100 > percent_collateral >= 75:
        if liquidity_collateral == 'High':
            count_collateral = 0.25 * maxscore_collateral
        elif liquidity_collateral == 'Low':
            count_collateral = 0.2 * maxscore_collateral

    elif percent_collateral >= 100:
        count_collateral = 0
    else:
        count_collateral = 9999
        print('Error Invalid input')
    return count_collateral

#refered to other condition which not directly related to the borrower
def condition(maxscore_condition,percent_inflation,job_info):
    if 5 >= percent_inflation >= 0 :
        count_inflation =  maxscore_condition
    elif 20 >= percent_inflation > 5:
        if job_info == 'Agricultural business' or job_info == 'Agricultural business':
            count_inflation = 0.8 * maxscore_condition
        elif job_info == 'Specialist' or job_info == 'Employee':
            count_inflation = 0.6 * maxscore_condition
    elif 0 >= percent_inflation > -5:
        count_inflation = maxscore_condition
    elif -20 <= percent_inflation <= -5:
        if job_info == 'Specialist' or job_info == 'Employee':
            count_inflation = 0.8 * maxscore_condition
        elif job_info == 'Agricultural business' or job_info == 'Agricultural business':
            count_inflation = 0.6 * maxscore_condition
    else:
        count_inflation = 9999
        print('Error Invalid input')
    return count_inflation

    #hello
