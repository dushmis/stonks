from nsetools import Nse
import pandas as pd

nsel = Nse()
stock_list = nsel.get_stock_codes()
stock_list = {k for k, v in stock_list.items()}
d = pd.DataFrame(stock_list)
d = d.sort_values(d.keys()[0])

d.to_csv("company.csv",index=False,header=False)
