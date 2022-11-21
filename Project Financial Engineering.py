file = open('D:\pycharm\Project\Ex2proportion.txt') #หาmax score ทั้ง C เเละ Sub-factor ใน C
proportion = []
for x in file:
    proportion.append(int(x))
file.close()

character = proportion[0]
capability = proportion[1]
capital = proportion[2]
collateral = proportion[3]
condition = proportion[4]

maxscore_character = character * 10
maxscore_capability = capability * 10
maxscore_capital = capital * 10
maxscore_collateral = collateral * 10
maxscore_condition = condition * 10


print('maxscore_character:',maxscore_character)
print('maxscore_capability:',maxscore_capability)
print('maxscore_capital:',maxscore_capital)
print('maxscore_collateral:',maxscore_collateral)
print('maxscore_condition',maxscore_condition)

file = open('D:\pycharm\Project\ExCharacter proportion.txt','r')
list_maxscore = []
list_capability = []
list_capital = []
for x in file:
    for y in x.split():
        list_maxscore.append(int(y))

credit_buro_score = (list_maxscore[0]/100) * maxscore_character
region_score = (list_maxscore[1]/100) * maxscore_character
job_score = (list_maxscore[2]/100) * maxscore_character
social_status_score = (list_maxscore[3]/100) * maxscore_character
income_score = (list_maxscore[4]/100) * maxscore_capability
health_score = (list_maxscore[5]/100) * maxscore_capability
job_stability_score = (list_maxscore[6]/100) * maxscore_capability
having_debt_score = (list_maxscore[7]/100) * maxscore_capability
other_debt_score = (list_maxscore[8]/100) * maxscore_capability
capital_score  = (list_maxscore[9]/100) * maxscore_capital
asset_score = (list_maxscore[10]/100) * maxscore_capital


#print('credit_buro_score:',credit_buro_score)
#print('region_score:',region_score)
#print('job_score:',job_score)
#print('social_status_score:',social_status_score)
#print('income_score:',income_score)
#print('health_score:',health_score)
#print('job_stability_score:',job_stability_score)
#print('having_debt_score:',having_debt_score)
#print('other_debt_score:',other_debt_score)
#print('capital_score:',capital_score)
#print('asset_score:',asset_score)
#print('maxscore_collateral:',maxscore_collateral)
#print('maxscore_condition:',maxscore_condition)



# Input ค่า จากไฟล์
repayment_history = input() #ไม่เคยค้าง / เคยค้างในอดีต ปัจจุบันปกติ / เคยค้างในอดีต ปิดบัญชี / เคยค้างชำระ เข้าโครงการพักชำระหนี้ / ค้างชำระ
region_info = input()   #Middle / South / North / East
job_info = input()      #Specialist / Employee / Non-agricultural business / Agricultural business
social_status = input() #Upper-upper / Lower-upper / Upper-middle / Lower-middle / Lower
health_info = input()   #Good health / Non-serious disease / Serious disease
revenue = int(input())
loan = int(input())
rate = float(input()) # rate ดอกเบี้ยเงินกู้ของธนาคาร
year = int(input())
job_year = int(input())
pay_other_debt = int(input())
debt = float(input())
asset = float(input())
collateral_asset = float(input())
liquidity_collateral = input()  # High or low
percent_inflation = float(input())

import all_def
user_count_repayment = all_def.repayment(credit_buro_score,repayment_history)
user_count_region = all_def.region(region_score,region_info)
user_count_job = all_def.job(job_score,job_info)
user_count_social = all_def.social(social_status_score,social_status)
user_count_income = all_def.income(income_score,revenue,loan,rate,year)
user_count_health = all_def.health(health_score,health_info)
user_count_job_stability = all_def.job_stability(job_stability_score,job_year)
user_count_having_debt = all_def.having_debt(having_debt_score,pay_other_debt,revenue)
user_count_other_debt = all_def.other_debt(other_debt_score,debt,asset)
user_count_capital_structure = all_def.capital_structure(capital_score,asset,debt)
user_count_percent_asset = all_def.percent_asset(asset_score,asset,loan)
user_count_collateral = all_def.collateral(maxscore_collateral,collateral_asset,loan,liquidity_collateral)
user_count_condition = all_def.condition(maxscore_condition,percent_inflation,job_info)


sum_character = user_count_repayment + user_count_region + user_count_job + user_count_social
sum_capability = user_count_income + user_count_health + user_count_job_stability +user_count_having_debt + user_count_other_debt
sum_capital = user_count_capital_structure + user_count_percent_asset
sum_collateral = user_count_collateral
sum_condition = user_count_condition

print('sum_character:',sum_character)
print('sum_capability:',sum_capability)
print('sum_capital:',sum_capital)
print('sum_collateral:',sum_collateral)
print('sum_condition:',sum_condition)


print('sum_all:',sum_character+sum_capability+sum_capital+sum_collateral+sum_condition)


file = open('D:\pycharm\Project\Ex cut-off point.txt','r') #Input เป็น Percent
list_cutoff_point = []
for x in file:
    for y in x.split():
        list_cutoff_point.append(int(y))
print('list_cutoff_point:',list_cutoff_point)
character_cutoffpoint = (list_cutoff_point[0]/100) * maxscore_character
capability_cutoffpoint = (list_cutoff_point[1]/100) * maxscore_capability
capital_cutoffpoint = (list_cutoff_point[2]/100) * maxscore_capital
collateral_cutoffpoint = (list_cutoff_point[3]/100) * maxscore_collateral
condition_cutoffpoint = (list_cutoff_point[4]/100) * maxscore_condition
all_cutoffpoint = (list_cutoff_point[5]/100) * 1000

print('character_cutoffpoint:',character_cutoffpoint)
print('capability_cutoffpoint:',capability_cutoffpoint)
print('capital_cutoffpoint:',capital_cutoffpoint)
print('collateral_cutoffpoint:',collateral_cutoffpoint)
print('condition_cutoffpoint:',condition_cutoffpoint)
print('all_cutoffpoint:',all_cutoffpoint)





