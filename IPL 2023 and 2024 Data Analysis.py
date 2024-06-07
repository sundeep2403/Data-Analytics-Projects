import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
BATSMEN PERFORMANCE IN IPL 2023
org_2023 = pd.read_csv('Orange Cap 2023.csv')
org_2023
org_2023.head()
innings_2023 = org_2023.sort_values(by= 'Innings', ascending = False).head(50)
innings_2023
sixes_2023 = org_2023.sort_values(by = '6s', ascending = False).head(16)
sixes_2023_filtered = sixes_2023[['Player Name','Team Name','6s']]
sixes_2023_filtered
sixes_2023.groupby('Team Name').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)
