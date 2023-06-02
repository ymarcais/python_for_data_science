# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    projection_life.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/31 15:06:35 by ymarcais          #+#    #+#              #
#    Updated: 2023/06/02 15:32:16 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load

def thousands_formatter(x, pos):
    if x >= 1000:
        value = 10 ** (x - 3)
        return f"{value:.0f}k"
    else:
        return int(x)


def projection_life(y):
    
        income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        income = income.set_index('country')
        income = income[str(y)] 
        income = income.apply(pd.to_numeric)
        income = income[(income != float('inf')) & (income != float('-inf'))]
        life = load("life_expectancy_years.csv")
        life = life.set_index('country')
        life = life[str(y)]
        
        year_ = pd.merge(income, life, on="country")
        year_ = year_.dropna()
        fig, ax = plt.subplots()
        plt.xscale('log')       
                
        plt.scatter(income, life)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.title(str(y))
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(thousands_formatter))
        # Show the plot
        plt.show()
        return life
        
    
def main():
    
    result = projection_life(1900)
    print(result)

if __name__ == "__main__" :    
    main()