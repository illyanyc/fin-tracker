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
    '''
    Class used to calculate technical indicators
    
        Attributes
        ----------
        ohlcv : DataFrame
            a multiindexed DataFrame of Open, High, Low, Close, Volume data of Tickers
    
    '''
    
    def __init__(self, _ohlcv):
        '''
        Parameters
        ----------
        _ohlcv : DataFrame
            current working multiindexed DataFrame of Open, High, Low, Close, Volume data of Tickers
        '''
        self.ohlcv = _ohlcv
        
        
    def validate_ticker(self, 
                        ticker : str):
        '''Helper method - validates if ticker is not null, not empty, and is present in the self.ohlcv'''
        
        _tickers = self.tickers()

        if not ticker:
            raise ValueError(f"Ticker param is empty: please pass a correct ticker -> ticker = str({ticker})")
        elif ticker:
            if isinstance(ticker, str):
                if ticker not in _tickers:
                    raise ValueError(f"Ticker {ticker} not found in self.ohlcv DataFrame")
                elif ticker in _tickers:
                    pass
                
            elif isinstance(ticker, int):
                raise TypeError(f"Incorrect ticker format: ticker cannot contain integers")
            else:
                raise TypeError(f"Incorrect data type: ticker must be a str -> str({ticker})")
                
   
    def tickers(self):
        '''Returns a list of tickers inside ohlcv
        '''
        df = self.ohlcv
        return list(df.columns.levels[0])
    
    
    def _open(self,
             ticker) -> DataFrame:
        '''
        Returns open price for ticker
        
            Parameters
            ----------
            ticker : str
                ticker to be processed

            Returns
            -------
            df : DataFrame
                'close' values
        '''
        self.validate_ticker(ticker=ticker) # validate ticker
        
        df = self.ohlcv.xs('open', 
                           axis=1, 
                           level=1, 
                           drop_level=False).droplevel(1, axis=1)
        
        return DataFrame(df[ticker]).rename(columns={ticker:'open'})
    
    
    def _high(self,
             ticker) -> DataFrame:
        '''
        Returns high price for ticker
        
            Parameters
            ----------
            ticker : str
                ticker to be processed

            Returns
            -------
            df : DataFrame
                'high' values
        '''
        self.validate_ticker(ticker=ticker) # validate ticker
        
        df = self.ohlcv.xs('high', 
                           axis=1, 
                           level=1, 
                           drop_level=False).droplevel(1, axis=1)
        
        return DataFrame(df[ticker]).rename(columns={ticker:'high'})
    
    
    def _low(self,
             ticker) -> DataFrame:
        '''
        Returns low price for ticker
        
            Parameters
            ----------
            ticker : str
                ticker to be processed

            Returns
            -------
            df : DataFrame
                'low' values
        '''
        self.validate_ticker(ticker=ticker) # validate ticker
        
        df = self.ohlcv.xs('low', 
                           axis=1, 
                           level=1, 
                           drop_level=False).droplevel(1, axis=1)
        
        return DataFrame(df[ticker]).rename(columns={ticker:'low'})
    
    
    def _close(self,
             ticker) -> DataFrame:
        '''
        Returns close price for ticker
        
            Parameters
            ----------
            ticker : str
                ticker to be processed - default = 'AAPL'

            Returns
            -------
            df : DataFrame
                'close' values
        '''
        self.validate_ticker(ticker=ticker) # validate ticker
        
        df = self.ohlcv.xs('close', 
                           axis=1, 
                           level=1, 
                           drop_level=False).droplevel(1, axis=1)
        
        return DataFrame(df[ticker]).rename(columns={ticker:'close'})
    
    
    def _volume(self,
             ticker) -> DataFrame:
        '''
        Returns volume for ticker
        
            Parameters
            ----------
            ticker : str
                ticker to be processed

            Returns
            -------
            df : DataFrame
                'volume' values
        '''
        self.validate_ticker(ticker=ticker) # validate ticker
        
        df = self.ohlcv.xs('volume', 
                           axis=1, 
                           level=1, 
                           drop_level=False).droplevel(1, axis=1)
        
        return DataFrame(df[ticker]).rename(columns={ticker:'volume'})
    
    
    # Get RSI Values
    def rsi(self,
            ticker : str,
            days : int = 14) -> DataFrame:
        '''
        Returns pd.DataFrame with RSI values

            Parameters
            ----------
            days : int
                number of days for RSI calculation; default = 14
            ticker : str
                ticker to be processed

            Returns
            -------
            rsi : DataFrame
                RSI values
        '''
        
        self.validate_ticker(ticker=ticker) # validate ticker
        
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
        
    
    # Get Williams %R Values
    def williams_range(self,
                       ticker : str,
                       days : int = 14) -> DataFrame:
        '''
        Returns pd.DataFrame with Williams %R values

            Parameters
            ----------
            days : int
                number of days for RSI calculation; default = 14
            ticker : str
                ticker to be processed

            Returns
            -------
            williams_range : DataFrame
                Williams %R values
        '''
        
        self.validate_ticker(ticker=ticker) # validate ticker
        
        df = self.ohlcv
        
        # get close price
        hlc = df.loc[:,ticker]

        highest_high = hlc['high'].rolling(window=days,center=False).max()
        lowest_low = hlc['low'].rolling(window=days,center=False).min()
        williams_range = (-100) * ((highest_high - hlc['close']) / (highest_high - lowest_low))

        return DataFrame(williams_range.fillna(0)).rename(columns={0:'williams_range'})

        
    
    # Get Aroon Indicator
    def aroon(self,
              ticker : str,
              days : int = 25) -> DataFrame:
    
        '''
        Returns pd.DataFrame with aroon Oscillator values

            Parameters
            ----------
            days : int
                number of days for Aroon Oscillator calculation; default = 25
            ticker : str
                ticker to be processed

            Returns
            -------
            aroon : DataFrame
                Aroon high {aroon_up}, Aroon low {aroow_down}, and Aroon Oscillator {aroon_oscillator}
        '''
    
        self.validate_ticker(ticker=ticker) # validate ticker

        df = self.ohlcv
        
        # get close price
        hlc = df.loc[:,ticker]

        aroon_up = []
        aroon_down = []

        n_days = days
        while n_days < len(list(hlc.index)):
            date = hlc['close'][n_days-days:n_days].index

            up = ((hlc['close'][n_days-days:n_days].tolist().index(max(hlc['close'][n_days-days:n_days])))/days)*100
            aroon_up.append(up)

            down = ((hlc['close'][n_days-days:n_days].tolist().index(min(hlc['close'][n_days-days:n_days])))/days)*100
            aroon_down.append(down)

            n_days += 1

        aroon = DataFrame([0] * days + [x - y for x, y in zip(aroon_up, aroon_down)], index=hlc.index.values).rename(columns={0:'aroon_oscillator'})
        aroon['aroon_up'] = [0] * days + aroon_up
        aroon['aroon_down'] = [0] * days + aroon_down

        return aroon
    
    
def test():
    pass


def main():
    pass


if __name__ == '__main__':
    main()