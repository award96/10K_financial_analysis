"""
    read in symbols
    write down shared concepts
    write down data to csv

"""
import csv
import pandas as pd


def read_lines_to_array(filepath):
    lines_arr = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            lines_arr.append(line)
    return lines_arr


def write_csv(filepath, rows, columns):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for row in rows:
            writer.writerow(row)


def read_csv(filepath):
    return pd.read_csv(filepath)
