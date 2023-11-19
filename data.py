import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Replace 'your_file.csv' with the actual file path
file_path = 'SalaryPrediction.csv'

# Read CSV file into a DataFrame
df = pd.read_csv(file_path)


print(df.head())
# Check for missing values
print(df.isnull().sum())

# Display basic statistics
print(df.describe())

#Square Root Rule:
num_bins = int(np.sqrt(len(df['Wage'])))
sns.histplot(df['Wage'], bins = num_bins , kde=False)  # Adjust the number of bins as needed
plt.xlabel('Player Wage')
plt.ylabel('Frequency')
plt.title('Distribution of Player Wages Square Root Rule')
plt.show()

#Sturges' Rule:
num_bins = int(np.ceil(1 + np.log2(len(df['Wage']))))
sns.histplot(df['Wage'], bins = num_bins , kde=False)  # Adjust the number of bins as needed
plt.xlabel('Player Wage')
plt.ylabel('Frequency')
plt.title('Distribution of Player Wages Sturges Rule')
plt.show()

