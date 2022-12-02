import pandas as pd
username = 'Tom'
df = pd.read_csv('D:\pycharm\Project\ExampleUser.csv', encoding = 'TIS-620')
for y in range(len(df.index)):
    if username == df.loc[y].Username:
        print(df.loc[y])