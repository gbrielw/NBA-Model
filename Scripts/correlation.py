import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

summaries = pd.read_csv('C:\\Users\\Gabriel\\OneDrive\\Passion Project\\Data\\Stats\\Team Summaries.csv')
recentSummaries = summaries[summaries['season'] > 2022]

totals = pd.read_csv('C:\\Users\\Gabriel\\OneDrive\\Passion Project\\Data\\Stats\\Team Totals.csv')
recentTotals = totals[totals['season'] > 2022]

#recent_data.drop(index=30)
dfs = pd.DataFrame(recentSummaries)
dft = pd.DataFrame(recentTotals)

#calculate r
efgCorrelation = dfs['e_fg_percent'].corr(dfs['w'])
print(f"Correlation Coefficient between eFG% and Wins: {efgCorrelation:.2f}")

fgaCorrelation = dft['fga'].corr(dfs['w'])
print(f"Correlation Coefficient between FGA and Wins: {fgaCorrelation:.2f}")

#plot fga vs Wins
sns.regplot(x=recentTotals['fga'], y=recentSummaries['w'])
plt.title('FGA vs. Wins')
plt.xlabel('FGA')
plt.ylabel('Wins')
plt.show()