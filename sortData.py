import pandas as pd
import numpy as np

import readWrite


def filter_na(inputPath, outputPath):
    df = pd.read_csv(inputPath)
    non_null = df[df.operating.notnull() | df.investing.notnull() | df.financing.notnull()]
    non_null.to_csv(outputPath)

def count_incomplete(filepath):
    df = pd.read_csv(filepath)
    df.info()
    incomplete = df[df.operating.isnull() | df.investing.isnull() | df.financing.isnull()]
    incomplete.info()
    """
    260 out of 3830
    """
def check_order(df, key):
    """
        returns true if the rows are organized by symbol, false otherwise.
        In other words, checks if all equivalent symbol values are adjacent.
    """
    d = {}
    length = df.shape[0]
    i = 0
    while i < length:
        val = df.iloc[i][key]
        while i < length - 1 and val == df.iloc[i + 1][key]:
            i += 1
        if val in d:
            return False
        else:
            d[val] = i
        i += 1
    return True

def count_consecutive(arr, required_start):
    print(f"\narr:\n{arr}")
    if not arr[0] == required_start:
        print(f'does not start at {required_start}')
        print(arr)
        return 0
    count = 1
    prev = required_start
    for i in range(1,len(arr)):
        print(f"\ni = {i}")
        print(f"prev: {prev}, arr[i]: {arr[i]}")
        if arr[i] != prev - 1:
            print("arr[i] != prev - 1")
            return count
        count += 1
        prev = arr[i]
    print("ran through array\n")
    return count
    


def get_velocity_row(df, key='netIncome', compare = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]):
    vel_row = [df.iloc[0]['symbol'], df.iloc[0]['industry'], df.iloc[0]['marketCap']]
    init_length = len(vel_row)
    placeholders = [np.nan] * len(compare)
    vel_row.extend(placeholders)
    years = df['year'].tolist()
    compare_indx = 0
    for i in range(len(years) - 1):
        while compare_indx < len(compare) and years[i] != compare[compare_indx]:
            compare_indx += 1
        if years[i] - 1 == years[i+1]:
            if compare_indx >= len(compare):
                break
            this_vel = df.iloc[i][key] - df.iloc[i+1][key]
            vel_row[compare_indx + init_length] = this_vel
        compare_indx += 1
    return vel_row

def get_velocities(inputPath, outputPath):
    df = pd.read_csv(inputPath, index_col=0)
    
    velocity_rows = []
    # 2019vel is: netIncome(2019) - netIncome(2018)
    cols = ['symbol', 'industry', 'marketcap', '2019vel', '2018vel', '2017vel', '2016vel', '2015vel', '2014vel', '2013vel', '2012vel', '2011vel']
    # Ensure all of each company's rows are adjacent
    df.sort_values(by=['symbol', 'year'])

    length = df.shape[0]
    symb = df.iloc[0]['symbol']
    i = 0
    while i < length:
        symb = df.iloc[i]['symbol']
        print(f"\non symb = {symb}")
        df_this_symb = df[df['symbol'] == symb]
        newRow = get_velocity_row(df_this_symb)
        print(f"\nnewRow:\n{newRow}\n\n")
        velocity_rows.append(newRow)
        while i < length and df.iloc[i]['symbol'] == symb:
            i += 1
    vel_df = pd.DataFrame(velocity_rows, columns=cols)
    vel_df.info()
    print(vel_df.head(20))
    vel_df.to_csv(outputPath)
    





if __name__ == "__main__":
    #filter_na('SP10K_data.csv', 'SP10k_data_clean.csv')
    #count_incomplete('SP10k_data_clean.csv')
    get_velocities('SP10K_data.csv', 'SP_netIncome_vel.csv')