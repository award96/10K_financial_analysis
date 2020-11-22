import os.path
import sys


from horizontalProfile import HorizontalProfile
from horizontalAnalysis import HorizontalAnalysis

industry = 'Real Estate'
filepath = "NYSE10Kdata.csv"
outputPath = "NYSE10K_horizontal_profile.csv"
yearRange = [2019,2011]
yearsList = [(2019,2018), (2019,2017), (2019,2016)]

def main(filepath, outputPath, yearRange, yearsList):
    quickLoadPath = None
    if  os.path.isfile(outputPath):
        print("\n\nThere is such a file")
        quickLoadPath = outputPath
    HP = HorizontalProfile(filepath=filepath,
        baseYear=yearRange[1],
        year=yearRange[0],
        inputPath=quickLoadPath,
        industry='')
    if not quickLoadPath:
        print("\nNo quickLoadPath, writing data to csv")
        HP.write_to_output(outputPath=outputPath)
    for yearTuple in yearsList:
        HA = HP.create_horiz_analysis(yearTuple[0], yearTuple[1])
        HA.histo()

main(filepath, outputPath, yearRange, yearsList)