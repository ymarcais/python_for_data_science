# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_pop.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/31 11:37:53 by ymarcais          #+#    #+#              #
#    Updated: 2023/06/02 15:13:04 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter 
import matplotlib.ticker as ticker
from load_csv import load

def format_millions(x, pos):
    return f"{int(x)}M"

def aff_pop():
    dataset = load("population_total.csv")
    dataset = dataset.set_index('country')
    compare = dataset.loc[['Belgium','France']][dataset.columns[0:250]]
    compare = compare.apply(lambda x: x.str.replace('M', '').str.replace('k', ''))
    compare = compare.apply(pd.to_numeric)
            
    #years = range(1800, 2050)
    years = compare.columns.astype(int)
    y1 = compare.loc['France']
    y2 = compare.loc['Belgium']
    formatter = FuncFormatter(format_millions)
    plt.gca().yaxis.set_major_formatter(formatter)

    
        
    #plt.yticks(tick)
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(base=40))
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=20))
    
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(" Population Projections")
    plt.plot(years, y1, label = 'France')
    plt.ylim(bottom=0, top=70)
    plt.plot(years, y2, label = 'Belgium')
    plt.legend(loc='lower right')    
    plt.show()
       
    return compare

def main():

    result = aff_pop()
    print(result)

if __name__ == "__main__":
    main()