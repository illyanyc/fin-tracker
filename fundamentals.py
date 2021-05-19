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



class Fundamental:
    '''Class used to calculate fundamental indicators
    
    Attributes
    ----------
    ohlcv : list of str
        tickers
    
    '''
    
    def __init__(self, tickers):
        '''
        Parameters
        ----------
        _ohlcv : DataFrame
            current working multiindexed DataFrame of Open, High, Low, Close, Volume data of Tickers
        '''
        self.ohlcv = tickers
    
    
    
    
def test():
    pass


def main():
    pass


if __name__ == '__main__':
    main()