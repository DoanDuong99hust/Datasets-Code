import pandas as pd
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np
import csv

dataDstLink = "/home/doanduong/DoanDuong/csv_data/outGoing368.csv"

# input_file = csv.DictReader(open(dataDstLink))
# for row in input_file :
#     print(row.keys())
data_pd = pd.read_csv('./home/doanduong/DoanDuong/csv_data/outGoing368.csv')
data_pd.head(5)
