import os.path
import sys


from horizontalProfile import HorizontalProfile
from horizontalAnalysis import HorizontalAnalysis
from utilities import generate_all_year_pairs

def main(
        outputPath,
        yearRange, 
        horizontalInput, 
        horizontalOutput,
        analysisBaseName,
        analyzeAllYears, 
        specificYears
        ):

    HP = HorizontalProfile(filepath=outputPath,
        baseYear=yearRange[1],
        year=yearRange[0],
        inputPath=horizontalInput,
        outputPath=horizontalOutput)
    if not horizontalInput:
        HP.write_to_output()
    if analyzeAllYears:
        for yearTuple in generate_all_year_pairs(yearRange):
            # analysisOutput = exampleName2019-2011.csv
            analysisOutput = analysisBaseName + str(yearRange[1]) + "-" + str(yearRange[0]) + ".csv"
            HA = HP.create_horiz_analysis(yearTuple[0], yearTuple[1], analysisOutput)
    else:
        for yearTuple in specificYears:
            analysisOutput = analysisBaseName + str(yearRange[1]) + "-" + str(yearRange[0]) + ".csv"
            HA = HP.create_horiz_analysis(yearTuple[0], yearTuple[1], analysisOutput)