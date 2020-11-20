import pandas as pd
import numpy as np


def calc_acc(df, start_yr, end_yr):
    start_str, end_str = str(start_yr) + 'vel', str(end_yr) + 'vel'
    df = df[df[start_str].notnull()]
    df = df[df[end_str].notnull()]
    acc_arr = []
    for index, row in df.iterrows():
        acc_arr.append(row[start_str] - row[end_str])
    df['acc'] = acc_arr
    df.info()
    print(df.head(25))
    return df


if __name__ == "__main__":
    df = pd.read_csv('SP_netIncome_vel.csv')
    df = calc_acc(df, 2019, 2018)
