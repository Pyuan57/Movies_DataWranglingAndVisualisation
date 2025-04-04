# 🎬 Movie Dataset Analysis with Python

This project focuses on **data wrangling** and **visualization** of a movie dataset. Using Python in a Jupyter Notebook environment, we explore patterns and insights hidden within the data — such as relationships between budget, gross revenue, scores, runtime, and more.

---

## 📁 Dataset Overview

- **Dataset Name:** `movies.csv`  
- **Source:** [Kaggle - Daniel Grijalva](https://www.kaggle.com/datasets/danielgrijalvas/movies)  
- **Total Records:** 7,668 movies  
- **Attributes:**  

  | Attribute | Description |
  |-----------|-------------|
  | `Name`    | Title of the movie |
  | `Rating`  | Film rating (e.g. R, PG) |
  | `Genre`   | Movie genre (e.g. Drama, Comedy) |
  | `Year`    | Year the movie was produced |
  | `Released`| Release date (including country) |
  | `Score`   | User ratings |
  | `Votes`   | Number of votes |
  | `Director`| Director of the movie |
  | `Writer`  | Writer of the movie |
  | `Star`    | Main actor/actress |
  | `Country` | Country of production |
  | `Budget`  | Budget in dollars |
  | `Gross`   | Gross revenue |
  | `Company` | Production company |
  | `Runtime` | Duration in minutes |

This dataset provides a rich source of information for analyzing various aspects of movie production and performance.

---

## 🚀 Getting Started

Follow these steps to run the notebook and explore the full project.

### 1. Download the the dataset and ipynb files.

### 2. Open with Anaconda (Jupyter Notebook)

Make sure you have [Anaconda](https://www.anaconda.com/products/distribution) installed.
Launch Jupyter Notebook via terminal or Anaconda Navigator.
This will open a browser window.
Navigate to `project.ipynb` and open it.

---

## 📊 What's Inside the Notebook?

The `project.ipynb` notebook includes:

### 🧹 Data Wrangling
- Reading and inspecting `movies.csv`
- Handling missing values
- Converting data types
- Cleaning and standardizing columns
- Removing duplicates

### 📈 Data Visualization & EDA
- Histograms and distribution plots for numerical features
- Scatter plots (e.g., Budget vs Gross, Score vs Votes)
- Box plots and bar charts for categorical data
- Correlation heatmaps
- Aggregation using `groupby` (e.g., average gross by genre or year)

### 💬 Discussion
- Summary of findings
- Analysis of trends and outliers
- Relationships between variables like budget, gross, score, and runtime
- Potential data limitations and ideas for future work

---

## 🛠 Requirements

You can install all required libraries using pip:

pip install pandas numpy matplotlib seaborn

Or use a conda environment with Jupyter pre-installed.

---

## 🧠 Purpose of the Project

We selected this dataset because of its variety of numerical and categorical data, which allows for in-depth data wrangling and visualization. It serves as a solid foundation for practicing exploratory data analysis (EDA) and storytelling with data.

---

## 📌 License & Credits

- **Dataset by:** [Daniel Grijalva on Kaggle](https://www.kaggle.com/datasets/danielgrijalvas/movies)  
- **Purpose:** Educational / Data Science practice  
