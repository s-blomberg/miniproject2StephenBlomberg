# INF601 - Advanced Programming in Python
# Stephen Blomberg
# Mini Project 2

import pandas as pd
import os
import matplotlib.pyplot as plt

#Checks for folder to place charts into.
os.makedirs("charts", exist_ok=True)

# reading in the autism study I downloaded from kaggle
df = pd.read_csv('Most Popular Programming Languages.csv')

# Display the first few rows of the DataFrame
# print(df.head())
# print(df.columns)

# Convert 'Month' column to datetime if it's not already
df['Month'] = pd.to_datetime(df['Month'])

# List of programming languages to plot (excluding 'Month')
languages = ['Python Worldwide(%)', 'JavaScript Worldwide(%)', 'Java Worldwide(%)',
             'C# Worldwide(%)', 'PhP Worldwide(%)', 'Flutter Worldwide(%)',
             'React Worldwide(%)', 'Swift Worldwide(%)', 'TypeScript Worldwide(%)',
             'Matlab Worldwide(%)']

# Find the global min and max values across all languages
y_min = df[languages].min().min()
y_max = df[languages].max().max()

# Create a separate plot for each language
for language in languages:
    plt.figure(figsize=(8, 5))
    plt.plot(df['Month'], df[language], label=language)

    # Set the same y-axis scale for all plots
    plt.ylim(y_min, y_max)

    # Adding titles and labels
    plt.title(f'Popularity of {language} Over Time')
    plt.xlabel('Time')
    plt.ylabel('Worldwide Popularity (%)')

    # Output to charts/
    plt.legend()
    plt.grid(True)
    plt.savefig(f"charts/{language}.png")

# Plot all languages on the same graph
plt.figure(figsize=(10, 6))

for language in languages:
    plt.plot(df['Month'], df[language], label=language)

# Adding titles and labels
plt.title('Popularity of Programming Languages Over Time')
plt.xlabel('Time')
plt.ylabel('Worldwide Popularity (%)')

# Display the legend and the grid
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Legend outside the plot
plt.grid(True)
plt.tight_layout()  # Adjust layout so everything fits nicely

# Show the plot
plt.savefig(f"charts/All_Languages.png")
