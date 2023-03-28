# -*- coding: utf-8 -*-
"""
@author: Lin, Wei-Zhi
v0.1 created at Mar 24 2023
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
