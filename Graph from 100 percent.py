import numpy as np
import matplotlib.pyplot as plt
### Graph from 100 Percent of each c and score that user get
# convert each C to percent
percent_character = (sum_character / maxscore_character) * 100
percent_capability = (sum_capability / maxscore_capability) * 100
percent_capital = (sum_capital / maxscore_capital) * 100
percent_collateral = (sum_collateral / maxscore_collateral) * 100
percent_condition = (sum_condition / maxscore_condition) * 100
all_c = ['Character', 'Capability', 'Capital', 'Collateral', 'Condition']
all_c = [*all_c, all_c[0]]
user_1 = [percent_character,percent_capability,percent_capital,percent_collateral,percent_condition]
user_1 = [*user_1, user_1[0]]
angle = np.linspace(start=0, stop=2 * np.pi, num=len(user_1)) # 2*np.pi=circle  num=5C
fig = plt.figure(figsize=(6, 6)) #ขนาดgraph
ax=fig.add_subplot(polar=True)
ax.plot(angle,user_1, 'o-', color='g', label='user_1')
ax.fill(angle, user_1, alpha=0.25, color='g')
ax.set_thetagrids(angle * 180/np.pi, all_c)
plt.title('User overview graph ', size=20,y=1.05) #หัวข้อกราฟ
lines, labels = plt.thetagrids(np.degrees(angle), labels=all_c)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

