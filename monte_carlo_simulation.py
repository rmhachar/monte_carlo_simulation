# Performs 100 simulations
# Each simulation simulates 30 years of returns for a given mean and standard deviation

# STEP 1: Import packages.

import random
import numpy as np
import pandas as pd
import scipy as sc
import scipy.stats as sct
from scipy.stats import norm


# STEP 2: Load relevant variables
sd = .18 # standard deviation
mu = .10 # average 
b_val = 10000 # begin value
invest = 10000 # investment per year
years = 30 # number of periods

y = 0
x = 0
a = [] # array for ending values

# simulate 100 times
while y < 101:
    x = 0
    current_val = b_val
    # simulate 30 years of returns
    while x < 31:
        rand = random.uniform(0,1)
        return_percent = norm.ppf(q=rand,loc=mu,scale=sd)
        current_val = current_val*(1+return_percent)+invest
        x+=1
    a.append(current_val)
    y+=1
 
# display the array of ending values
a

# display summary statistics of ending values
np.amax(a)
np.amin(a)
np.average(a)
np.std(a)
