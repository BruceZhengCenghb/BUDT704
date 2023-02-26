import numpy as np
import pandas as pd
import matplotlib as plt
from numpy import nan as NA


#1.a)
df_inc = pd.read_excel('HW4_inc5000-2018.xlsx', index_col= 'RANK')
#print(df_inc)

total_cpy = df_inc['COMPANY NAME'].value_counts

#3a)
df_states = pd.read_csv('HW4_states_by_region.csv')
print(df_states)
#b)


def top(df, category=None, value=None, numberofrow =10):
    if (category!=None) and (value!=None):
        df=df[df[category]==value]  # generate a DataFrame of the value under category
        df_rtn=df.sort_values(by ='REVENUW', ascending= False)
        return df_rtn[:numberofrow]
    else: 
        df1 = df.sort_values(by='REVENUW', ascending= False)
        return df1[:numberofrow]
    
a = top(df_inc,None, None,6)

print(a)
# #5）
# def  findit(df, category, value, n = 10):
#     if (category != None) & (value != None):


#     else:  # 
#         df.sort_values(by = 'REVENUE', ascending = True)
#         df[] 


    