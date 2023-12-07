# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:18:42 2023

@author: panne
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_distribution(data, column_name):
    plt.hist(data[column_name], bins=30, density=True, alpha=0.6, color='g', label='Histogram')

    mu, std = norm.fit(data[column_name])
    x_min, x_max = plt.xlim()
    x_values = np.linspace(x_min, x_max, 100)
    pdf_values = norm.pdf(x_values, mu, std)
    plt.plot(x_values, pdf_values, 'k', linewidth=2, label='PDF')

    return mu, std

def plot_mean_salary(mean_salary):
    plt.axvline(mean_salary, color='b', linestyle='dashed', linewidth=2, label=f'Mean Salary ($W={mean_salary}$)')

def plot_x_as_std(std):
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2, label=f'$X$ ($std={std}$)')

def customize_plot():
    plt.xlabel('Salary')
    plt.ylabel('Probability Density')
    plt.title('Distribution of Salaries')
    plt.legend()
    plt.show()

def calculate_and_display_std(std):
    standard_deviation = round(std, 2)
    print(f'Standard Deviation: {standard_deviation}')

def main():
    # Step 1: Load salary data from the CSV file
    file_path = 'data8.csv'  # Replace with the actual path
    salary_data = load_data(file_path)

    # Step 2: Plot the distribution using a histogram and probability density function
    column_name = salary_data.columns[0]
    mean, std = plot_distribution(salary_data, column_name)

    # Step 3: Calculate and display the mean annual salary (W)
    mean_salary = round(mean, 2)
    plot_mean_salary(mean_salary)

    # Step 4: Calculate and display the standard deviation
    calculate_and_display_std(std)

    # Step 5: Plot X as the standard deviation
    plot_x_as_std(std)

    # Step 6: Customize the plot with labels, title, and legend
    customize_plot()

if __name__ == "__main__":
    main()
