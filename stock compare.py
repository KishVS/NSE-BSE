#!/usr/bin/env python
#Author Kishore Kumaar
#Date 13-Sep-2022
# from bsedata.bse import BSE
# b = BSE()
# print(b)
# q = b.getQuote('534976')
# print(q)
from email.quoprimime import quote
from nsetools import Nse
import pandas as pd, numpy as np
nse = Nse()
#quote = nse.get_quote('sbin')
code = nse.get_stock_codes()
print(code)
#print(quote['companyName'])
#print("Current Price:" + str(quote['buyPrice1']))
q = input("Enter Stock Code:")
quote = nse.get_quote(q)
print(quote)
