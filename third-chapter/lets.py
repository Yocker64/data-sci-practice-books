import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots
# import statsmodels.api as sm
from ISLP import load_data
from ISLP.models import ModelSpec as MS, summarize

# Load data and fit the model (your existing code)
Auto = load_data('Auto')
X = MS(['horsepower']).fit_transform(Auto)
y = Auto['mpg']
model1 = sm.OLS(y, X)
results1 = model1.fit()

# 1. Create the scatter plot FIRST. This creates the 'ax' object.
ax = Auto.plot.scatter(x='horsepower', y='mpg', facecolor='None', edgecolor='k', alpha=0.5)

# 2. Define your abline function
def abline(ax, b, m, *args, **kwargs):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim, *args, **kwargs)

# 3. Now, use abline to draw the regression line on the scatter plot 'ax'
abline(ax,
       results1.params.iloc[0],      # Intercept
       results1.params.iloc[1],      # Slope
       'r--',                        # Style: red dashed line
       linewidth=3)

# Display the plot
subplots.show()