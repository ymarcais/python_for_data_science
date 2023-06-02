# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_pop.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/31 11:37:53 by ymarcais          #+#    #+#              #
#    Updated: 2023/06/01 13:43:15 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter 
import matplotlib.ticker as ticker
from load_csv import load

def aff_pop():
    dataset = load("population_total.csv")
    dataset = dataset.set_index('country')
    compare = dataset.loc[['Belgium','France']][dataset.columns[0:101]]
    # Remove 'M' character from values in compare DataFrame
    compare = compare.apply(lambda x: x.str.replace('M', ''))
            
    years = range(1800, 1901)

    fig, ax = plt.subplots()
    y1 = compare.loc['France']
    y2 = compare.loc['Belgium']
        
    ax.plot(years, y1)
    plt.ylim(0, 70)
    ax.plot(years, y2)
    plt.ylim(0, 40)
    
    plt.show()
       
    return compare

def main():

    result = aff_pop()
    print(result)

if __name__ == "__main__":
    main()