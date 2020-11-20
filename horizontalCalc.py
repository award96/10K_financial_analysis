import pandas as pd
from horizontalView import naming_convention


def analysis_naming_convention(endYear, startYear, percent=False):
    name = str(startYear) + "-" + str(endYear) + "horizontal"
    if percent:
        name += "Perc"
    return name


def analysis(df, endYear, startYear):
    print("\n###########################\nbeginning\n\n")
    df = df[df[naming_convention(endYear)].notnull(
    ) & df[naming_convention(startYear)].notnull()]
    df.info()
    horizontal = []
    horizontalPerc = []
    for index, row in df.iterrows():
        thisHorizontal = row[naming_convention(
            endYear)] - row[naming_convention(startYear)]
        thisHorizontalPerc = thisHorizontal * \
            100 / row[naming_convention(startYear)]
        horizontal.append(thisHorizontal)
        horizontalPerc.append(thisHorizontalPerc)
    df[analysis_naming_convention(endYear, startYear)] = horizontal
    df[analysis_naming_convention(
        endYear, startYear, percent=True)] = horizontalPerc

    # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
    return df
