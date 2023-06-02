# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_csv.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/29 11:20:34 by ymarcais          #+#    #+#              #
#    Updated: 2023/05/31 14:00:35 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from typing import Optional

def load(path: str) -> Optional[pd.DataFrame]:
    try:
        dataset = pd.read_csv(path)

        rows, columns = dataset.shape
        print("Dataset dimensions:", rows, "rows x", columns, "columns")
        return dataset
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError):
        print("Error: Unable to load the dataset.")
        return None

from load_csv import load

def main():

    print(load("population_total.csv"))

if __name__ == "__main__":
    main()