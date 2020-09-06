#####################################
# 5.3: Black Scholes Option Pricing #
#####################################

#######################
# importing libraries #
#######################
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

######################################
# Computing Functions: For Intervals #
######################################

def d1(S, K, r, stdev, T):
    return (np.logs(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt)


def d2(S, K, r, stdev, T):
    return (np.logs(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt)


# using cumulative distribution function for Black Scholes

# tells how much of data lies below stated percentile, assuming normal distribution
print(norm.cdf(0))

print(norm.cdf(0.25))

print(norm.cdf(0.75))

print(norm.cdf(9))

####################################################
# Applying Interpolations to Compute Stock Pricing #
####################################################



# variables used for computation:

# current stock price, strike price,
# risk free rate, standard deviation,
# and time horizon in years

def BSM(S, K, r, stdev, T):
    return (S * norm.cdf(d1(S, K, r, stdev, T)))- (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))


ticker = 'SPY'

data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2020-8-31')['Adj Close']



# Calculate the Price of a Call Option
























































































# in order to display plot within window
# plt.show()
