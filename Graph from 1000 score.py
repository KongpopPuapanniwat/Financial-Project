### Graph from 1000 score
# Overview graph
import numpy as np
import matplotlib.pyplot as plt
all_c = ['Character', 'Capability', 'Capital', 'Collateral', 'Condition']
all_c = [*all_c, all_c[0]]
# User graph
user_1 = [sum_character,sum_capability,sum_capital,sum_collateral,sum_condition]
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
