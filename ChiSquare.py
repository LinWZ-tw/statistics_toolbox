# -*- coding: utf-8 -*-
"""
@author: Lin, Wei-Zhi
v0.1 created at Mar 24 2023.
"""
#%% chi square 
def chi2 (df1, df2, df3, col: str):
    import pandas as pd
    from scipy.stats import chi2_contingency
    df1_count = df1[col].value_counts()
    df2_count = df2[col].value_counts()
    df3_count = df3[col].value_counts()
    table = {str(df1): [df1_count.get(0, 0), df1_count.get(1, 0)],
             str(df2): [df2_count.get(0, 0), df2_count.get(1, 0)],
             str(df3): [df3_count.get(0, 0), df3_count.get(1, 0)],
             'index': ['0', '1']}
    table = pd.DataFrame(data=table).set_index(['index'])
    stat, p_value, dof, expected = chi2_contingency(table)
    return (p_value)
