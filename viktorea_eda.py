import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
url = "https://web.vscht.cz/~steinbaj/python_intro/diabetes_assignment.htm"
df = pd.read_html(url)[0]

# Display few rows of the dataset to identify error
print("Original dataset:")
print(df.head())

# Identify and clean error-values

# Calculate the IQR for the 'Glucose' column
Q1 = df['Glucose'].quantile(0.25)
Q3 = df['Glucose'].quantile(0.75)
IQR = Q3 - Q1

# Filter values within the range [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR]
df = df[(df['Glucose'] >= Q1 - 1.5 * IQR) & (df['Glucose'] <= Q3 + 1.5 * IQR)]

# Drop rows with NaN values
df = df.dropna()

# Save the cleaned dataset to CSV
df.to_csv("cleaned_diabetes_data.csv", index=False)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
# Display the histogram of the distribution of the number of pregnancies
sns.histplot(df['Pregnancies'], bins=20, kde=False, color='blue', ax=ax1)
ax1.set_title('Distribution of number of pregnancies')
ax1.set_xlabel('Number of pregnancies')
ax1.set_ylabel('Frequency')

# Display the scatter plot of Glucose, Age
sns.scatterplot(x='Glucose', y='Age', hue='Outcome', data=df, palette='coolwarm', ax=ax2)
ax2.set_title('Relationship between Glucose and Age')
ax2.set_xlabel('Glucose')
ax2.set_ylabel('Age')

plt.show()
