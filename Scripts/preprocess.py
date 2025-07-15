import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r'C:\Users\Gabriel\OneDrive\Desktop\Passion Project\Data\games\BoxScore.csv')

# Fill missing numerical values with the mean
data.fillna('NA', inplace=True)
#data['COMMENT'].fillna('NA', inplace=True)




# Check for missing values
print(data.isnull().sum())

# Display the first few rows of the datasets
print(data.head(n=30))


data.to_csv(r'C:\Users\Gabriel\OneDrive\Desktop\Passion Project\Data\games\preprocessed_BoxScore.csv')