import matplotlib.pyplot as plt
import numpy as np
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
x = np.arange(len(groups))
width = 0.35
plt.bar(x - width/2, means_men, width, label='Men', color='blue')
plt.bar(x + width/2, means_women, width, label='Women', color='pink')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)
plt.legend()
plt.show()
