import pandas as pd

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
    