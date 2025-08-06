import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('train.csv')

# Fill missing 'Age' with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Drop 'Cabin' column
df.drop(columns=['Cabin'], inplace=True)

# Fill missing 'Embarked' with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Convert columns to categorical where appropriate
'''
df['Pclass'] = df['Pclass'].astype('category')
df['Survived'] = df['Survived'].astype('category')
df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')


# Show cleaned DataFrame info
print(df.info())

# Summary statistics
print(df.describe(include='all'))

# Survival rate by gender
print("\nSurvival rate by gender")
print(df.groupby('Sex')['Survived'].mean())

# Survival rate by class
print("\nSurvival rate by class")
print(df.groupby('Pclass')['Survived'].mean())

# Survival by gender and class
print("\nSurvival rate by gender and class")
print(df.groupby(['Sex', 'Pclass'])['Survived'].mean())

'''

# --- Visualizations ---
# Bar plot: Survival by gender
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

# Bar plot: Survival by class
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

# Bar plot: Survival by class and gender
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df)
plt.title('Survival Rate by Class and Gender')
plt.show()

# Heatmap: Survival by class and embarkation
pivot = df.pivot_table(index='Pclass', columns='Embarked', values='Survived', aggfunc='mean')
sns.heatmap(pivot, annot=True, cmap='YlGnBu')
plt.title('Survival Rate by Class and Embarkation Port')
plt.show()