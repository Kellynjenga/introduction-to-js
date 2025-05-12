# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nDataset Info:")
    print(df.info())

    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean the dataset (no missing values in Iris dataset, but here's an example)
    # df.fillna(method='ffill', inplace=True)

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Group by species and compute the mean of numerical columns
    print("\nMean values grouped by species:")
    print(df.groupby('species').mean())

except Exception as e:
    print(f"An error occurred during analysis: {e}")

# Task 3: Data Visualization
try:
    # Line chart: Trends over features (example with sepal length)
    plt.figure(figsize=(10, 6))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.plot(subset.index, subset['sepal length (cm)'], label=species)
    plt.title("Sepal Length Trends by Species")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    plt.show()

    # Bar chart: Average petal length per species
    plt.figure(figsize=(8, 6))
    sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
    plt.title("Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.show()

    # Histogram: Distribution of sepal width
    plt.figure(figsize=(8, 6))
    sns.histplot(df['sepal width (cm)'], kde=True, bins=15, color='green')
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot: Sepal length vs Petal length
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")
