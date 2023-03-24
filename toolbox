# -*- coding: utf-8 -*-
"""
@author: Lin, Wei-Zhi
v0.1 created at Mar 24 2023; two tools were employed in this version.
"""
#%% full anova
def anova (df1, df2, df3, col: str): # when 3 arrays with continuous values are compared
    import scipy.stats as st
    df1_shapiro = st.shapiro(df1[str(col)])
    df2_shapiro = st.shapiro(df2[str(col)])
    df3_shapiro = st.shapiro(df3[str(col)])
    levene = st.levene(df1[str(col)], df2[str(col)],df3[str(col)], center = 'mean')
    f_value, p_value = st.f_oneway(df1[str(col)],df2[str(col)],df3[str(col)])
    return (df1_shapiro, df2_shapiro, df3_shapiro, levene, f_value, p_value)
#%% p-value by anova
def anova_p(df1, df2, df3, col: str):
    import scipy.stats as st
    f_value, p_value = st.f_oneway(df1[str(col)],df2[str(col)],df3[str(col)])
    return (p_value)
#%% chi square 
def chi2 (df1, df2, df3, col: str): # when 3 arrays with categorical values are compared
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
