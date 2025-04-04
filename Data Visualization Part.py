#Data Visualization Part
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
df = pd.read_csv('clean_movies.csv')
sns.set(style="whitegrid")

# Define columns and their corresponding colors
columns = {
    'budget': 'skyblue',
    'gross': 'orange',
    'runtime': 'purple',
    'score': 'green',
    'votes': 'blue',
    'profit': 'yellow'
}

# Function to plot distributions and boxplots
def plot_distribution_and_boxplot(df, column, color, title_suffix=''):
    plt.figure(figsize=(10, 5))
    
    # Plot histogram
    plt.subplot(1, 2, 1)
    df[column].plot(kind='hist', bins=30, color=color, edgecolor='black')
    plt.title(f'Distribution of {column.capitalize()} {title_suffix}')
    plt.xlabel(column.capitalize())
    
    # Plot boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[column], color=color)
    plt.title(f'Boxplot of {column.capitalize()} {title_suffix}')
    
    plt.tight_layout()
    plt.show()

# Function to remove outliers using IQR method
def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# Function to trim outliers using IQR method
def trim_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data[column] = data[column].clip(lower=lower_bound, upper=upper_bound)
    return data

# Iterate over columns to plot in groups
for column, color in columns.items():
    # Original data
    plot_distribution_and_boxplot(df, column, color)
    
    # After removing outliers
    df_clean = remove_outliers_iqr(df, column)
    plot_distribution_and_boxplot(df_clean, column, color, title_suffix='(After Outlier Removal)')
    
    # After trimming outliers
    df_trimmed = trim_outliers_iqr(df.copy(), column)
    plot_distribution_and_boxplot(df_trimmed, column, color, title_suffix='(After Outlier Trimming)')
