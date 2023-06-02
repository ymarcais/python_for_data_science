# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_life.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/29 11:37:16 by ymarcais          #+#    #+#              #
#    Updated: 2023/06/02 14:16:06 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

def plot_campus_life_expectancy(y):
    
    dataset = load("life_expectancy_years.csv")
    dataset = dataset.set_index('country')

    if dataset is not None:
        if str(y) in dataset.index:
            country_data =  dataset.loc[str(y)]
            years = dataset.columns.astype(int)
            life_expectancy = country_data.values
            print (life_expectancy)
            
            #plt.yticks(tick)
            plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(base=40))
            plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=10))
            plt.xlim(1790, 2110)
            plt.ylim(25, 99)
            
            plt.plot(years, life_expectancy)
            plt.xlabel("Year")
            plt.ylabel("Life Expectancy")
            plt.title(f"{y} Life expectancy Projections ")
            plt.show()
        else:
            print(f"No data available for {str(y)}.")

# Example usage
from aff_life import plot_campus_life_expectancy

def main():
    
    plot_campus_life_expectancy("France")

if __name__ == "__main__":
    main()