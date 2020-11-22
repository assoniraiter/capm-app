import statsmodels.api as sm

# Defining model (OLS)
def model(y, x):
    x = sm.tools.add_constant(x)
    model = sm.OLS(y, x)
    capm = model.fit()
    
    return capm


