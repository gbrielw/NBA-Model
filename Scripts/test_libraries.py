import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\Gabriel\OneDrive\Passion Project\Data\Stats\Team Summaries.csv')
#print(data.info())

#basic statistics
#print(data.describe())

recent_data = data[data['season'] > 2023]

#league average index
#print(recent_data[recent_data['team']=='League Average'].index)

#remove league average
recent_data.drop(index=30)

#plot efg% vs Wins
#sns.scatterplot(x=filtered_data['e_fg_percent'], y=filtered_data['w'])
#plt.title('Effective FG% vs. Wins')
#plt.show()

