"""
    using the finnhub API, get data from 10ks of a list of companies, then join that data
    with general info on the company.
"""

import csv
import pandas as pd
import numpy as np

import finnAPI
import readWrite
# except errors when indexing (ie baz = json['key'])
from utilities import safe_index


def parseTenK(tenkJson):
    """
        Take in a json response from FinnHub API, parse it to get
        data from every 10-K in the response.

        ARGS:
            tenkJson (dict) - FinnHub API's json resp
        OUTPUT:
            newRows (list(lists)) - A list where each value represents a row.
                                    Each row is a list of values. The values are
                                    string and integer.
    """
    newRows = []
    try:
        symbol = tenkJson['symbol']
        filings = tenkJson['data']
    except IndexError:
        print(KeyError)
        print("returning NA array")
        return [['NA'] * 8]
    for tenK in filings:
        year = safe_index(tenK, 'year', 'NA')
        start = safe_index(tenK, 'startDate', 'NA')
        end = safe_index(tenK, 'endDate', 'NA')
        filed = safe_index(tenK, 'filedDate', 'NA')
        report = safe_index(tenK, 'report', {}, True)
        cashFlow = safe_index(report, 'cf', [])
        incomeStatement = safe_index(report, 'ic', [])
        operating, investing, financing = 'NA', 'NA', 'NA'
        netIncome = 'NA'
        for json in cashFlow:
            concept = safe_index(json, 'concept', '')
            if concept == 'NetCashProvidedByUsedInOperatingActivities':
                operating = safe_index(json, 'value', 'NA')
            elif concept == 'NetCashProvidedByUsedInInvestingActivities':
                investing = safe_index(json, 'value', 'NA')
            elif concept == 'NetCashProvidedByUsedInFinancingActivities':
                financing = safe_index(json, 'value', 'NA')
        for json in incomeStatement:
            concept = safe_index(json, 'concept', '')
            if concept == 'NetIncomeLoss':
                netIncome = safe_index(json, 'value', 'NA')

        newRows.append([symbol, year, start, end, filed,
                        netIncome, operating, investing, financing])
    return newRows


def parseProfile(profileJson):
    industry = safe_index(profileJson, 'finnhubIndustry', 'NA', True)
    marketCap = safe_index(profileJson, 'marketCapitalization', 'NA', True)
    return [industry, marketCap]


def collect_tenK_data(inputPath, outputPath):
    """
    Open filepath, get list of symbols "str",
    plug in symbols one by one into finn api and record the response

    ARGS:
        inputPath str - txt file where each row is a symbol
        outputPath str - csv file to put final data
    OUTPUT:
        writes a csv file where each row is a 10-K form,

        the columns are: symbol (company's symbol), year (year the 10-k was filed),
        start (start date), end (end date), filed (filed date), operating,
        investing, financing (the last three are net cash provided by and
        used in ___ activities)


    """

    symbolArr = readWrite.read_lines_to_array(inputPath)
    dataArr = []
    columns = ['symbol', 'year', 'start', 'end', 'filed',
               'netIncome', 'operating', 'investing', 'financing']
    for symbol in symbolArr:
        print(f"\nOn symbol: {symbol}")
        tenkJson = finnAPI.get_tenK_json(symbol)
        newRows = parseTenK(tenkJson)
        dataArr.extend(newRows)
    print("done collecting data")
    print("Number of rows collected:")
    print(len(dataArr))
    df = pd.DataFrame(dataArr, columns=columns)
    df.info()
    print(df)
    df.to_csv(outputPath)


def add_profile_data(inputPath, outputPath):
    """
        Add to an existing CSV file generated by collect_tenK_data.
    """
    df = pd.read_csv(inputPath, index_col=0)
    # filter out rows with no $ data at all
    df = df[df.netIncome.notnull() | df.operating.notnull() |
            df.investing.notnull() | df.financing.notnull()]
    symbol_dict = {}
    industry_arr = []
    marketCap_arr = []
    for index, row in df.iterrows():
        symbol = row['symbol']
        print(f"\non symbol: {symbol}\n")
        if symbol in symbol_dict:
            print("symbol already recorded")
            new_data_arr = symbol_dict[symbol]
            industry_arr.append(new_data_arr[0])
            marketCap_arr.append(new_data_arr[1])
            continue
        profile_json = finnAPI.get_profile_json(symbol)
        industry, marketCap = parseProfile(profile_json)
        industry_arr.append(industry)
        marketCap_arr.append(marketCap)
        symbol_dict[symbol] = [industry, marketCap]
    print("\ndone\nAdding arrays to columns\n###################\n")
    loc1 = len(df.columns)
    loc2 = loc1 + 1
    try:
        df.insert(loc=loc1, column="industry", value=industry_arr)
        df.insert(loc=loc2, column="marketCap", value=marketCap_arr)
    except Exception:
        df.insert(loc=4, column="industry", value=industry_arr)
        df.insert(loc=5, column="marketCap", value=marketCap_arr)
    print(df.info())
    print(df)
    df.to_csv(outputPath)

def collect(inputPath, outputPath, apiKeyPath):
    collect_tenK_data(inputPath, outputPath)
    add_profile_data(outputPath, outputPath)
