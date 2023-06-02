# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    projection_life.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/31 15:06:35 by ymarcais          #+#    #+#              #
#    Updated: 2023/06/01 11:21:28 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def projection_life(y):
    
        income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        income = income.set_index('country')
        income = income[str(y)]
        life = load("life_expectancy_years.csv")
        life = life.set_index('country')
        life = life[str(y)]
        
        year_ = pd.merge(income, life, on="country")
        year_ = year_.dropna()
        
        plt.xscale('log')
        plt.scatter(income, life)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.title(str(y))

        # Show the plot
        plt.show()
        return life
        
    
def main():
    
    result = projection_life(1900)
    print(result)

if __name__ == "__main__" :    
    main()