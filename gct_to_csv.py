"""
Author: Lin, Wei-Zhi
Created: 2024-11-19
Last Updated: 
"""
#%% 
# import pkgs
from cmapPy.pandasGEXpress import parse_gct
import pandas as pd
#%%
path_gct = 'path_to_gct'
gct_data = parse_gct.parse(path_gct)
df_data = gct_data.data_df
# %%
df_data.to_csv('df_name.csv')
