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

print(maxscore_character)
print(maxscore_capability)
print(maxscore_capital)
print(maxscore_collateral)
print(maxscore_condition)


file = open('D:\pycharm\Project\ExCharacter proportion.txt','r')
list_maxscore = []
list_capability = []
list_capital = []
for x in file:
    for y in x.split():
        list_maxscore.append(int(y))
print(list_maxscore)
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

print(credit_buro_score)
print(region_score)
print(job_score)
print(social_status_score)
print(income_score)
print(health_score)
print(job_stability_score)
print(having_debt_score)
print(other_debt_score)
print(capital_score)
print(asset_score)


file = open('D:\pycharm\Project\Ex cut-off point.txt','r')
