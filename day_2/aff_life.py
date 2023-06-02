# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_life.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/29 11:37:16 by ymarcais          #+#    #+#              #
#    Updated: 2023/05/31 11:32:50 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
from load_csv import load

def plot_campus_life_expectancy(country: str):
    
    dataset = load("life_expectancy_years.csv")
    dataset = dataset.set_index('country')

    if dataset is not None:
        if 'Yemen' in dataset.index:
            country_data =  dataset.loc['Yemen']
            years = dataset.index[1:]
            life_expectancy = country_data.values
            print (life_expectancy)
            
            '''plt.plot(years, life_expectancy)
            plt.xlabel("Year")
            plt.ylabel("Life Expectancy")
            plt.title(f"Life Expectancy at {Yemen}")
            plt.legend([Yemen])
            plt.show()
        else:
            print(f"No data available for {Yemne}.")'''

# Example usage
from aff_life import plot_campus_life_expectancy

def main():
    
    plot_campus_life_expectancy("Angola")

if __name__ == "__main__":
    main()