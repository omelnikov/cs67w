from IPython.core.interactiveshell import InteractiveShell as IS; IS.ast_node_interactivity = "all"
import numpy as np, pandas as pd, matplotlib.pylab as plt

# Increase viewable area of Pandas tables, numpy arrays, plots
pd.set_option('max_rows', 5, 'max_columns', 500, 'max_colwidth', 1, 'precision', 2)
np.set_printoptions(linewidth=10000, precision=4, edgeitems=20, suppress=True)
plt.rcParams['figure.figsize'] = [16, 4]

from termcolor import cprint
printA = lambda str:  cprint(str, 'blue', 'on_yellow', attrs=['bold'])
# Code for EDA, not for quiz
def ShowDF_InColor(df, cmap='coolwarm', lo=0, hi=.2):
    ''' Prints numeric pandas DataFrame (df) with a background color ranging from lo to hi values.
        cmap is a color map (see below). '''
    def bg_grad(s, m, M, cmap='coolwarm', lo=0, hi=0): 
        '''  DataFrame background styling function. Apply background gradient color for pandas data frames
        Input: 
            s: pandas Series or DataFrame
            m, M: minimum and maximum values in the dataset
            cmap: predefined color map, see: https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html
            ... other paramters for generating gradient colors
        Output: returns styled pandas dataframe, which can be printed
        '''
        norm = matplotlib.colors.Normalize(m - ((M - m) * lo), M + ((M - m) * hi))    
        c = [matplotlib.colors.rgb2hex(x) for x in plt.cm.get_cmap(cmap)(norm(s.values))]
        return ['background-color: %s' % color for color in c]
    return df.style.apply(bg_grad, cmap=cmap, m=df.min().min(), M=df.max().max(), lo=lo, hi=hi)
  
  
