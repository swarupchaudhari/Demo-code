import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1. Read the data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Line of best fit for all data
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(1880, 2051)
    sea_level = result.slope * years + result.intercept
    plt.plot(years, sea_level, color='red')

    # 4. Line of best fit from year 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    result_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000 = np.arange(2000, 2051)
    sea_level_2000 = result_2000.slope * years_2000 + result_2000.intercept
    plt.plot(years_2000, sea_level_2000, color='green')

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # 6. Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()