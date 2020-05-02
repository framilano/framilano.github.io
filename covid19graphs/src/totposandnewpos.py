import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def removehour(element):
    templist = element.split('T')
    return templist[0]

def main():
    dataframe = pd.read_csv("dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)
    print(dataframe)


    return

main()