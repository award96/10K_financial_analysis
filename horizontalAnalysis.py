from horizontalSuper import HorizontalSuper
import horizontalCalc

class HorizontalAnalysis(HorizontalSuper):
    def __init__(self, 
        filepath,
        yearsList, 
        df,
        symbol=None, 
        outputPath=None, 
        inputPath=None, 
        key='netIncome', 
        baseCols=['symbol','industry','marketCap']):

        super().__init__(filepath, 
            symbol=symbol, 
            outputPath=outputPath, 
            inputPath=inputPath, 
            key=key, 
            baseCols=baseCols)


        self.yearsList = yearsList
        self.validate_yearList()
        self.df = df
        
    def get_col_names(self, excludeBase=False):
        analysis_cols = []
        for yearTuple in self.yearsList:
            analysis_cols.extend([horizontalCalc.analysis_naming_convention(yearTuple[0], yearTuple[1]), horizontalCalc.analysis_naming_convention(yearTuple[0], yearTuple[1], percent=True)])
        if excludeBase:
            return analysis_cols
        return self.baseCols + analysis_cols



    def validate_yearList(self):
        if (type(yearsList) != list):
            raise ValueError("yearList must be a list of tuples (biggerYear, smallerYear")
        for index, tuple_ in yearsList:
            if (type(tuple) != tuple):
                raise ValueError(f"A value of yearsList was not a tuple\nindex = {index}, type(val) = {type(tuple_)}")
            if (tuple_[0] <= tuple[1]):
                raise ValueError(f"Tuples stored in yearsList must be of the format (biggerYear, smallerYear) where biggerYear > smallerYear\nFor index = {index}, biggerYear = {tuple_[0]} and smallerYear = {tuple[1]}")
        
