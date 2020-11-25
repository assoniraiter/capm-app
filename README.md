# CAPM App (B3 stock exchange)

## Introduction

App designed to calculate beta parameters from the companies listed in B3 index (Ibovespa) using Sharpe's CAPM (1964). 

This application is set to collect daily data from Yahoo Finance and Bacen SGS (default period: from 2000-01-01 to the current date) from 70 companies listed in Ibovespa and to calculate beta parameters, as well its significance and R-squared.

The output is a .csv file containing the results mentioned above.

CAPM app is already deployed on Heroku server.

Currently on version 1.0.0. New functionalities are being developed.

### Requirements

Requirements for usage are provided in the requirements.txt file and can be easily installed using pip.

## Usage

All you have to do is to download the files and run request.py. The model is already deployed on Heroku server and it takes around four minutes to perform the calculations for the default companies. 

If you are looking to estimate beta parameters from companies not listed in B3 Index, all you have to do is modify ticker_list object in request.py.

New functionalities are being developed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
