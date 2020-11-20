import horizontalView
import horizontalCalc

import pandas as pd

class HorizontalProfile:
    def __init__(self, filepath, baseYear=2018, year=2019, symbol=None, outputPath=None, inputPath=None, key="netIncome", baseCols=['symbol', 'industry', 'marketCap']):
        self.filepath = filepath
        self.baseYear = baseYear
        self.year = year
        self.symbol = symbol
        self.outputPath = outputPath
        self.inputPath = inputPath
        self.key = key
        self.baseCols = baseCols

        self.df = self.instantiate_df()

    def __repr__(self):
        start = f"HorizontalProfile from filepath: {self.filepath}\nYears range is {self.baseYear} to {self.year}\nThe values are from the key: {key}\n"
        optionSymbol, optionOutput = "", ""
        if self.symbol:
            optionSymbol = f"the focus company is represented by the symbol {self.symbol}\n"
        if self.outputPath:
            optionOutput = f"If the results are written to output the path will be {self.outputPath}"
        return start + optionSymbol + optionOutput

    def __str__(self):
        return f"filepath: {self.filepath} , baseYear: {self.baseYear} , year: {self.year} symbol: {self.symbol} , outputPath: {self.outputPath} , key: {self.key}"

    def get_filepath(self):
        return self.filepath
    def get_baseYear(self):
        return self.baseYear
    def get_year(self):
        return self.year
    def get_symbol(self):
        return self.symbol
    def get_outputPath(self):
        return self.outputPath
    def get_key(self):
        return self.key
    def get_df(self):
        return self.df.copy(deep=True)
    def get_col_names(self, excludeBase=False):
        yearsList = horizontalView.generate_years_list(self.year, self.baseYear)
        if excludeBase:
            return horizontalView.name_columns(yearsList, base=[])[0]
        return horizontalView.name_columns(yearsList, base=self.baseCols)


    def write_to_output(self, outputPath=None):
        if outputPath:
            self.outputPath = outputPath
        if (not outputPath) and (not self.outputPath):
            raise ValueError("outputPath is None.\noutputPath is not defined in the method call, and outputPath was not defined upon instantiation")
        self.df.to_csv(self.outputPath)

    def instantiate_df(self):
        if self.inputPath:
            return pd.read_csv(self.inputPath, index_col=0)
        return horizontalView.generate_horizontal_df(self.filepath, self.year, self.baseYear, key=self.key, baseCols=self.baseCols)

    def create_horiz_analysis(self, endYear, startYear):
        analysis_df = horizontalCalc.analysis(self.df, endYear, startYear)
        oldColumns = self.get_col_names(excludeBase=True)
        print("oldColumns")
        print(oldColumns)
        analysis_df.drop(columns=oldColumns)
        analysis_df.info()
        print(analysis_df.head(25))
    

    
        