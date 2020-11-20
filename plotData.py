import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def basicHisto(filepath, column):

    df = pd.read_csv(filepath)
    plt.figure(figsize=(3, 2))
    hist = df.hist(column=column, bins=20, figsize=(16, 9))
    plt.show()


def decorate():
    plt.ticklabel_format(axis="x", style="sci", scilimits=(6, 6))
    plt


def histo_by_percentile(filepath, column, percentile=(0, 1), bins=20):
    # Validate params
    if not isinstance(percentile, (tuple or list)) or len(
            percentile) != 2 or percentile[0] < 0 or percentile[0] > 1 or percentile[1] < 0 or percentile[1] > 1 or percentile[0] > percentile[1]:
        raise ValueError(
            f"Percentile should be a tuple of (low_value, high_value) ranging from 0 to 1.\nThis was your input: {percentile}")

    # Import Data
    df = pd.read_csv(filepath)
    # Prepare data
    df = df[df[column].notnull()]
    vals = sorted(df[column].tolist())
    low_indx = int(percentile[0] * len(vals))
    high_indx = int(percentile[1] * len(vals))
    vals = vals[low_indx:high_indx]

    # Draw
    plt.figure(figsize=(16, 9))
    n, bins, patches = plt.hist(vals, bins=bins, color='purple')
    # Decoration
    plt.title(
        f"Histogram of {column} net cash for S&P500 companies\nValues from {percentile[0]*100}th to {percentile[1]*100}th Percentile")
    plt.xlabel(f"{column} net cash (millions)")
    decorate()
    plt.ylabel("Count")

    plt.show()


def histo_by_range(
        filepath,
        column,
        x_range=(
            float('-inf'),
            float('inf')),
        bins=20):
    # Validate params
    if not isinstance(x_range, (tuple or list)) or len(
            x_range) != 2 or x_range[0] > x_range[1]:
        raise ValueError(
            f"x_range should be a tuple or list of 2 values: (low_end, high_end)\nThis was your input: {x_range}")

    # Import Data
    df = pd.read_csv(filepath)
    # Prepare data
    df = df[df[column].notnull()]
    vals = sorted(df[column].tolist())
    low_indx = 0
    high_indx = len(vals) - 1
    for i in range(len(vals)):
        if vals[i] > x_range[0]:
            #print(f"\nlow found, i = {i}\nvals[i] = {vals[i]}, vals[i-1] = {vals[i-1]}")
            low_indx = i
            break
    for i in reversed(range(len(vals))):
        if vals[i] < x_range[1]:
            #print(f"\high found, i = {i}\nvals[i] = {vals[i]}, vals[i+1] = {vals[i+1]}")
            high_indx = i
            break
    print("low_indx")
    print(low_indx)
    print(vals[low_indx])
    print("high_indx")
    print(high_indx)
    print(vals[high_indx])
    vals = vals[low_indx:high_indx]

    # Draw
    plt.figure(figsize=(16, 9))
    n, bins, patches = plt.hist(vals, color='purple')
    # Decoration
    plt.title(
        f"Histogram of {column} net cash for S&P500 companies\nValues from {x_range[0]//10**6}\$ million to {x_range[1]//10**6}\$ million")
    plt.xlabel(f"{column} net cash (millions)")
    plt.ylabel("Count")
    decorate()
    plt.show()


def custom_histo(
        filepath,
        column,
        symbol=None,
        year=None,
        industry=None,
        title="",
        x_axis_label="",
        y_axis_label="",
        x_axis_scale=6):
    # filter by year
    # filter by industry
    # pick spec company
    # choose metric(s)
    pass


def example():
    # Import Data
    df = pd.read_csv(
        "https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

    # Prepare data
    x_var = 'displ'
    groupby_var = 'class'
    df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
    vals = [df[x_var].values.tolist() for i, df in df_agg]

    # Draw
    plt.figure(figsize=(16, 9), dpi=80)
    colors = [plt.cm.Spectral(i / float(len(vals) - 1))
              for i in range(len(vals))]
    n, bins, patches = plt.hist(
        vals, 30, stacked=True, density=False, color=colors[:len(vals)])

    # Decoration
    plt.legend({group: col for group, col in zip(
        np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
    plt.title(
        f"Stacked Histogram of ${x_var}$ colored by ${groupby_var}$",
        fontsize=22)
    plt.xlabel(x_var)
    plt.ylabel("Frequency")
    plt.ylim(0, 25)
    plt.xticks(ticks=bins[::3], labels=[round(b, 1) for b in bins[::3]])
    plt.show()


#basicHisto('SP10k_data_clean.csv', 'operating')
#histo_by_range('SP10k_data_clean.csv', 'operating')
for spending in ['operating']:
    for focus in [(-7 * 10**8, 4 * 10**9)]:
        histo_by_range('SP10k_data_clean.csv', spending, x_range=focus)
# example()
