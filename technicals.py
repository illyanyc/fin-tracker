'''TODO: documentation'''

# Import libraries
# System
import os, time, sys, glob
from pathlib import Path
from datetime import date, datetime, timedelta

# Data
import numpy as np
import pandas as pd
from pandas import DataFrame



class TechnicalAnalysis:
    '''TODO: documentation'''
    
    def __init__(self, _ohlcv):
        self.ohlcv = _ohlcv
        
    
    def tickers(self):
        '''Returns a list of tickers inside ohlcv'''
        df = self.ohlcv
        return list(df.columns.levels[0])
    
    def close(self,
             ticker : str = 'AAPL') -> DataFrame:
        '''Returns close price for ticker
        
        Parameters
        ----------
        ticker : str - ticker to be processed - default = 'AAPL'

        Returns
        -------
        rsi : DataFrame - close values
        '''
        df = self.ohlcv.xs('close', 
                           axis=1, 
                           level=1, 
                           drop_level=False).droplevel(1, axis=1)
        
        return DataFrame(df[ticker]).rename(columns={ticker:'close'})
    
    
    # Get RSI Values
    def rsi(self, 
            days : int = 14, 
            ticker : str = 'AAPL') -> DataFrame:
        '''Returns pd.DataFrame with RSI values

        Parameters
        ----------
        days : int - number of days for RSI calculation; default = 14
        ticker : str - ticker to be processed - default = 'AAPL'

        Returns
        -------
        rsi : DataFrame - RSI values
        '''

        df = self.ohlcv
        
        # get close price
        close = df.loc[:,ticker]['close']

        # calculate delta
        delta = close.diff()

        # calculate gain and loss
        n_up = delta.clip(lower=0)
        n_down = -1*delta.clip(upper=0)

        # calculate ema
        ema_up = n_up.ewm(com=days, adjust=False).mean()
        ema_down = n_down.ewm(com=days, adjust=False).mean()

        # calculate relative strenght
        rs = ema_up/ema_down

        # calculate rsi and append to close
        rsi = 100 - (100 / (1 + rs))

        return DataFrame(rsi.fillna(0)).rename(columns={'close':'rsi'})
        
    

    
    
    
def test():
    pass


def main():
    pass


if __name__ == '__main__':
    main()