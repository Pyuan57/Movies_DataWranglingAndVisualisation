#Discussion Part
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clean_movies.csv')

# 1. Does a higher budget lead to higher box office returns?
plt.figure(figsize=(8, 6))
sns.scatterplot(x='budget', y='gross', size='profit', data=df, hue='profit', palette='coolwarm', edgecolor='black', sizes=(20, 200), alpha=0.6)
plt.title('Scatter Bubble Plot: Budget vs Gross Earnings')
plt.xlabel('Budget')
plt.ylabel('Gross Earnings')
plt.legend(title='Profit', bbox_to_anchor=(1, 1))
plt.show()

# 2. Does the IMDb score correlate with the movie’s box office success?
# Create bins for score and gross
score_bins = pd.cut(df['score'], bins=10)
profit_bins = pd.cut(df['profit'], bins=10)

# Create a pivot table with average profit for each score bin
heatmap_data = df.pivot_table(index=score_bins, columns=profit_bins, values='profit', aggfunc='mean')
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.0f', cbar_kws={'label': 'Avg Profit'})
plt.title('Heatmap: Score vs Profit')
plt.xlabel('Profit')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.show()

# 3. What are the most successful genres in terms of box office gross and scores?
# Average Gross Earnings by Genre:
plt.figure(figsize=(8, 6))
avg_gross_by_genre = df.groupby('genre')['gross'].mean().sort_values(ascending=False)
avg_gross_by_genre.plot(kind='bar', color='orange')
plt.title('Average Gross Earnings by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Gross Earnings')
plt.show()
# Average Score by Genre
plt.figure(figsize=(8, 6))
avg_score_by_genre = df.groupby('genre')['score'].mean().sort_values(ascending=False)
avg_score_by_genre.plot(kind='bar', color='skyblue')
plt.title('Average Score by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Score')
plt.show()

# 4. How do movie runtimes influence audience ratings?
plt.figure(figsize=(10, 6))
sns.boxplot(x='runtime_category', y='score', data=df)
plt.title('Box Plot: Score by Runtime Category')
plt.xlabel('Runtime Category')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.show()