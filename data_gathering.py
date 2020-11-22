import pandas as pd
import sgs as sgs
from yahoofinancials import YahooFinancials
from datetime import datetime

# Function to get data from YahooFinancials
def get_yf(ticker, start_date = '2000-01-01'):
    """
    Get YahooFinancials data.
    ticker: Ticker name (format = 'XXXX');
    start_date: Data collection start date (format = 'YYYY-MM-DD').
    """
    # Get today
    today_yf = datetime.today().strftime('%Y-%m-%d')
    
    ticker = str(ticker.replace('"',''))
    
    # Adjusting ticker name
    if ticker == 'BVSP':
        ticker = '^' + ticker
    else:
        ticker = ticker + '.SA'
    # Getting raw data
    yf = YahooFinancials(ticker = ticker)
    data = yf.get_historical_price_data(start_date = start_date,
                                           end_date = today_yf,
                                           time_interval = 'daily')
    # Cleaning data
    data = pd.DataFrame(data[ticker]['prices'])
    data['formatted_date'] = pd.to_datetime(data['formatted_date'])
    data.set_index('formatted_date', inplace = True)
    data = data['adjclose']
    data = data.fillna(method = 'ffill')
    
    return data

# Function to get data from Bacen SGS
def get_sgs(start_date = '01/01/2000'):
    """
    Get risk free rate from SGS.
    start_date: Data collection start date
    """
    # Get today
    today_rf = datetime.today().strftime('%d/%m/%Y')
    
    # Getting clean data
    data = sgs.time_serie(12, start = start_date, end = today_rf)
    data = data.fillna(method = 'ffill')
    
    return data
