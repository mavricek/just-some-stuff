# Correlation and visualization
# Matej
# 2018 May 8th

import pandas as pd
import numpy as np
import os
import statsmodels.formula.api as smf

if __name__ == '__main__':
	d_core = 'E:\\Docs\\Data\\'
	d_viz = d_core + 'Visualizations\\'
	d_data = d_core + 'USDA ERS\\'

	f_marg = d_data + 'fats.xls'
	f_divorce = d_core + 'national_marriage_divorce_rates_00-16.xlsx'

	d_marg = pd.read_excel(f_marg, sheet_name = 6, skiprows = 7, skipfooter = 12, header = None)
	d_marg = d_marg.loc[:,[0,10]]
	d_marg.columns = ['Year','Marg_lbs_per_capita']

	print(d_marg.tail(10))
