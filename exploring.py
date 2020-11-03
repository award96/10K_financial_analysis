import pandas as pd

import finnAPI
import readWrite
from utilities import safe_index

def parse_tenK(tenKJSON):
    pass


def count_names(arr):
    rd = {}
    for item in arr:
        if item in rd:
            rd[item] += 1
        else:
            rd[item] = 1
    return rd

def dict_to_sorted_array(d, term):
    concepts, count = [], []
    for key in d.keys():
        concepts.append(key)
        count.append(d[key])
    temp_dict = {term: concepts, 'count': count}
    df = pd.DataFrame.from_dict(temp_dict)
    df = df.sort_values(by=['count'], ascending=False)
    return df
    
def find_best_keys(filepath):

    symbol_arr = readWrite.read_lines_to_array(filepath)
    concept_arr, label_arr = [], []
    for symbol in symbol_arr:
        print(f"\non symbol: {symbol}")
        tenKJSON = finnAPI.get_tenK_json(symbol)
        filings = safe_index(tenKJSON,'data',[],True)
        for tenK in filings:
            report = safe_index(tenK, 'report', {}, True)
            income = safe_index(report, 'ic', [], True)
            for json in income:
                concept = safe_index(json, 'concept',  '', True)
                label = safe_index(json, 'label',  '', True)
                concept_arr.append(concept)
                label_arr.append(label)
    print("\n#########################\nhave all data\n")
    concept_dict = count_names(concept_arr)
    label_dict = count_names(label_arr)

    concept_df = dict_to_sorted_array(concept_dict, 'concept')
    label_df = dict_to_sorted_array(label_dict, 'label')
    concept_df.to_csv('concept_count.csv')
    label_df.to_csv('label_count.csv')
    print("\n####################\nDone sorting data\n")
    print("\nconcepts:\n")
    concept_df.info()
    print(concept_df)
    print("\nlabels:\n")
    label_df.info()
    print(label_df)



find_best_keys('splist.txt')



