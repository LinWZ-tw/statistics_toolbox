# -*- coding: utf-8 -*-
"""
@author: Lin, Wei-Zhi
v0.1 created at Mar 29 2023.
use to calculate mean value.
use when there are 3 datafames
"""
def mean(df1, df2, df3, index: list):
    import pandas as pd
    from statistics_toolbox import anova_p
    result = pd.DataFrame(index=index)
    result[str(df1)] = pd.Series(dtype='float64')  # add an empty column for df1 mean
    result[str(df2)] = pd.Series(dtype='float64')  # add an empty column for df2 mean
    result[str(df3)] = pd.Series(dtype='float64')  # add an empty column for df3 mean
    result['pvalue'] = pd.Series(dtype='float64')  # add an empty column for pvalue
    # calculate mean
    for i in range(len(index)):
        result[str(df1)].iloc[i] = df1[index[i]].mean()
        result[str(df2)].iloc[i] = df2[index[i]].mean()
        result[str(df3)].iloc[i] = df3[index[i]].mean()
    # calculate p-value
    for i in range(len(index)):
        result['pvalue'].iloc[i] = anova_p(df1, df2, df3, index[i])
    return (result)
