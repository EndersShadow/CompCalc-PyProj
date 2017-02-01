#import pandas package
import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib as plt
from matplotlib import style

#Read in the local data as .csv
Alz_df = pd.read_csv('c:\python\CompCalc-PyProj\Alzheimers.csv')
Alz_df[:3]

#Clean Data- create pd of just the male column 129 of 132
#MaleAlz = Alz_df
# CompCalc-PyProj
