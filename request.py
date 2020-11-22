import pandas as pd
import json
import requests

raw = pd.read_excel('Complete-List-of-Constituents-of-Bovespa-Index-Jan-1-2020.xlsx')
ticker_list = raw['Ticker'].dropna()

results = []
url = 'https://capm-app.herokuapp.com/predict_api'

for ticker in ticker_list:
    json_string = json.dumps(ticker)
    r = requests.post(url, json = json_string)
    results.append(r.json())

results = pd.DataFrame(results)
results.index = ticker_list
results.columns = ['Beta','P-value','R-squared']
results.to_csv('results.csv')