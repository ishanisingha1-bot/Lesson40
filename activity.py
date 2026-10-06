import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('penguins')
df=df.dropna()
print(df.head())
print(df.info())
print(df.describe())
print('Species:',df['species'].unique())
print('Islands:',df['island'])