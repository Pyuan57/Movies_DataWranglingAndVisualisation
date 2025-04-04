# Data Wrangling & EDA Part
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movies.csv')

#missing data handling
# Show the initial number of missing values
print("Missing values before handling:")
print(df.isnull().sum())
numeric_columns = ['score', 'votes', 'budget', 'gross', 'runtime']

for col in numeric_columns:
    # Ensure columns are treated as numeric
    df[col] = pd.to_numeric(df[col], errors='coerce')  
    # Fill missing values with the median
    df[col].fillna(df[col].median(), inplace=True) 

categorical_columns = ['rating', 'released', 'writer', 'star', 'country', 'company']
for col in categorical_columns:
    # Fill missing values with the most frequent valu
    df[col].fillna(df[col].mode()[0], inplace=True)  

# Check the number of missing values after handling
print("\nMissing values after handling:")
print(df.isnull().sum())

df.to_csv('clean_movies.csv', index=False)

#Find out the row and column of the dataset 
print("\nThe shape of the dataset is :" ,df.shape)
print (df.info())

#Add new ' Profit ' column 
#Formula for profit
profit = df['gross'] - df['budget']
df["profit"]= profit

df.to_csv('clean_movies.csv', index=False)
print("\nMovies and Their Profits:")
print(df[['name', 'profit']].head())


#runtime categorization
def categorize_runtime(runtime_value):
    if runtime_value <= 0:
        return 'Invalid Runtime'
    elif runtime_value < 90:
        return 'Short (Less than 1.5 hour)'
    elif 60 <= runtime_value <=120 :
        return 'Medium (1.5-2 hours)'
    elif runtime_value > 120:
        return 'Long (More than 2 hours)'
    else:
        return 'Unknown'
        
df['runtime_category'] = df['runtime'].apply(categorize_runtime)

print("\nRuntime and runtime_category:")
print(df[['runtime', 'runtime_category']])

runtime_summary = df['runtime_category'].value_counts()

print("\nSummary of movies by runtime category:")
print(runtime_summary)

plt.figure(figsize=(8, 5))
runtime_summary.plot(kind='bar', color='skyblue')
plt.title('Summary of Movies by Runtime Category')
plt.xlabel('Runtime Category')
plt.ylabel('Number of Movies')
plt.xticks(rotation=0)
plt.show()
df.to_csv('clean_movies.csv', index=False)

# Categorize scores
def categorize_score(score):
    if score >= 8.0:
        return 'Excellent'
    elif 7.0 <= score < 8.0:
        return 'Good'
    elif 5.0 <= score < 7.0:
        return 'Average'
    else:
        return 'Poor'

df['score_category'] = df['score'].apply(categorize_score)

print("\nMovie name and score_category:")
print(df[['name', 'score_category']])

print("\nSummary of movies by score category:")
score_summary = df['score_category'].value_counts()
print(score_summary)

plt.figure(figsize=(8, 5))
score_summary.plot(kind='bar', color='skyblue')
plt.title('Summary of Movies by Score Category')
plt.xlabel('Score Category')
plt.ylabel('Number of Movies')
plt.xticks(rotation=0)
plt.show()
df.to_csv('clean_movies.csv', index=False)

# Handle incorrect numeric data
numeric_columns = ['score', 'votes', 'budget', 'gross', 'runtime','profit']

for col in numeric_columns:

     # Coerce invalid values to NaN
    df[col] = pd.to_numeric(df[col], errors='coerce') 
    
    if col == 'score':
        
        # Make sure the range for score is from 0 to 10 
        df = df[(df['score'] >= 0) & (df['score'] <= 10)]
        
    elif col in ['budget', 'gross']:
        
        # Make sure 'budget' and 'gross' are not negative numbers
        df = df[df[col] >= 0]
        
    elif col == 'runtime':
        
        # Make sure 'runtime' is not negative number   
        df = df[df['runtime'] >= 0]

df.to_csv('clean_movies.csv', index=False)



#Exploratory Data Analysis
numeric_cols = ['score', 'votes', 'budget', 'gross', 'runtime', 'profit']
pd.set_option('display.float_format', '{:.2f}'.format)

# Calculate all the statistics
range_values = df[numeric_cols].max() - df[numeric_cols].min()
variance_values = df[numeric_cols].var()
std_dev_values = df[numeric_cols].std()
mean_values = df[numeric_cols].mean()
median_values = df[numeric_cols].median()
sum_values = df[numeric_cols].sum()
min_values = df[numeric_cols].min()
max_values = df[numeric_cols].max()

# Create a DataFrame with the additional statistics
stats = pd.DataFrame({
    'Mean': mean_values,
    'Median': median_values,
    'Sum': sum_values,
    'Min': min_values,
    'Max': max_values,
    'Range': range_values,
    'Variance': variance_values,
    'Standard Deviation': std_dev_values
})

stats = stats.T
print("Statistics:")
print(stats.to_string())
