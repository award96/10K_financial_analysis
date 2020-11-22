import pandas as pd
import numpy as np

def horizontal(start, end):
    val = end - start
    percent = val * 100 / start
    return (val, percent)
