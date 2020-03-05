import pandas as pd
import sys

import matplotlib.pyplot as plt

allDf=pd.read_csv("all_symbols.1.csv")
allDf.Date = pd.to_datetime(allDf.Date,format='%Y-%m-%d')
zero=allDf.loc[allDf.Date>'2020-02-01']


def __print__(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

grouped = allDf.groupby('Symbol')

for key in grouped.groups.keys():
    pl=grouped.get_group(key).plot('Date',['Open','Close','High'],title=key,figsize=(15,5)) 
    fig = pl.get_figure()
    __print__("plotted ",key)
    fig.savefig("images/"+key+"-1.png")
