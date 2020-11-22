import pandas as pd
import data_gathering as dg
import transformation as tr
import estimation as es

# Function to predict (API)

def predict(ticker_name):
    ticker = dg.get_yf(ticker_name)
    market = dg.get_yf('BVSP')
    riskfree = dg.get_sgs()

    ticker_returns = tr.get_returns(ticker)
    market_returns = tr.get_returns(market)

    ticker_excess = tr.get_excess(ticker_returns, riskfree, 'excess ticker')
    market_excess = tr.get_excess(market_returns, riskfree, 'excess market')

    clean_data = pd.concat([ticker_excess, market_excess], axis = 1).dropna()
    ticker = clean_data['excess ticker']
    market = clean_data['excess market']

    capm = es.model(y = ticker, x = market)
    beta = capm.params[1]
    pvalue = capm.pvalues[1]
    rsquared = capm.rsquared
    
    return round(beta, 2), round(pvalue, 3), round(rsquared, 4)


