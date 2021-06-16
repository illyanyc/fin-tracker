<img src="img/logo.svg" width=30%>


<code>technitrade</code> *is a developing public python library of all (or rather most) financial technical indicators*

estimated completion of v.0.1 --> Q4 2021

---
#### Table of Contents
* [Requirements](#requirements)
* [Usage](#usage)
* [Market Data](#market-data)
* [Technical Analysis](#technical-analysis)
    * [RSI](#rsi)
    * [Williams Range](#williams-range)
    * [Aroon Indicator](#aroon-indicator)

---

## Requirements
<code>technitrade</code> is composed in <code>.ipynb</code> [Jupyter](https://jupyter.org/install) notebooks that run on [Anaconda](https://docs.anaconda.com/) which return a [panels](https://panel.holoviz.org/) Dashboard and <code>.py</code> core files which contain the methods for computation.


### Jupyter Lab
```bash
pip install jupyterlab
```

### Packages

```python
# data analysis
conda install numpy
conda install pandas
conda install matplotlib
pip install python-dotenv

# visualization
conda install -c pyviz panel
conda install -c pyviz hvplot
conda install -c plotly plotly

conda install "notebook>=5.3" "ipywidgets>=7.5"
jupyter labextension install jupyterlab-plotly@4.14.3
jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.14.3
```
<br>

<code>technitrade</code> uses [Alpaca Trade API](https://pypi.org/project/alpaca-trade-api/).

```python
pip install alpaca-trade-api
```
<br>

---

## Usage
Import the <code>TechnicalAnalysis</code> module:

```python
import numpy as np
import pandas as pd

from technicals import TechnicalAnalysis
import data.marketdata.alpaca as api
```
<br>

Set path to your <code>.env</code> file containing the API keys:
```python
api_key_path = '../{api_keys}.env' # path to the .env file containing the API keys
```
The Alpaca Trade API keys muyst be titled:
> ALPACA_API_KEY<br>
> ALPACA_SECRET_KEY<br>


Gather **ohlcv** (*open, high, low, close, volume*) data:
```python
tickers = ['FB','AAPL','AMZN','NFLX','GOOG'] # a list of tickers

ohlcv = api.ohlcv(tickers=tickers, api_key_path=api_key_path)
```

<br>

Alternatly, you can get **ohlcv** data for entire index by accessing the tickers within <code>data/tickers/</code> which contain <code>.csv</code> files named **nasdaq**, **nyse**, **amex**. These files contain company data in the following format:
```sql
COLUMNS ('Symbol', 'Name', 'Country', 'IPO Year', 'Sector', 'Industry')
```

<br>

Once the data is loaded, create an instance of the object and pass the **ohlcv** data:
```python
technicals = TechnicalAnalysis(ohlcv)
```
<br>

Testing the instance of the class can be done by plotting the closing price for the first ticker in the tickers list:
```python
print(f"Open price data for {technicals.tickers()[0]}")
technicals._open(ticker=technicals.tickers()[0]).tail(14).plot(color='black')
```


The above code should return:
```python
[1]: Open price data for AAPL
```
![AAPL_open](data/images/AAPL_open.png)


---
## Market data
Market data data access is currently only available via the [Alpaca Trade API](https://alpaca.markets/docs/). The API connector is available by calling <code>data.marketdata.alpaca</code> as shown in the [Usage](#usage) section.

The Alpaca Trade API connector method <code>ohlcv</code>:

```python
ohlcv(tickers: list or DataFrame, 
          start_date : str = '2020-01-01',
          end_date : str = datetime.now().strftime('%Y-%m-%d'),
          timeframe : str = '1D',
          api_key_path : str = '../../../resources/api_keys.env') -> DataFrame
```

## Class methods
### Open
Return <code>open</code> attribute of the barset.

```python
_open(self, ticker) -> DataFrame
```
<br>

### High
Return <code>high</code> attribute of the barset.

```python
_high(self, ticker) -> DataFrame
```
<br>

### Low
Return <code>low</code> attribute of the barset.

```python
_low(self, ticker) -> DataFrame
```
<br>

### Close
Return <code>close</code> attribute of the barset.

```python
_close(self, ticker) -> DataFrame
```
<br>

### Volume
Return <code>volume</code> attribute of the barset.

```python
_volume(self, ticker) -> DataFrame
```
<br>

---

## Technical analysis
### ***RSI***
[Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp), better known as RSI is a technical indicator used to determine is a particular security is overbought or oversold. It measures the magnitude of price change of the asset; and is an oscillator that moves between 0 and 100. RSI was developed by J. Welles Wilder Jr. in 1978.

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;RSI&space;=&space;100&space;-&space;\left(\frac{100}{1&plus;Relative\:Strenght}\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;RSI&space;=&space;100&space;-&space;\left(\frac{100}{1&plus;Relative\:Strenght}\right)" title="RSI = 100 - \left(\frac{100}{1+Relative\:Strenght}\right)" /></a>
<br>

where ***Relative strenght*** (***RS***) = *average gain* - *average loss*
<br>

***Class method:***
```python
rsi(ticker : str, days : int = 14) -> DataFrame
```
<br>

### ***Williams Range***
[Williams %R](https://www.investopedia.com/terms/w/williamsr.asp) (*Williams Percent Range*), is a momentum indicator with range [-100, 0] measures overbought and oversold levels. Williams %R measures ratio of the differences:
* highest high and close <br>
* highest high and lowest low <br>

therefore capturing the directional momentum.

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;Williams\:Percent\:Range=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;Williams\:Percent\:Range=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" title="Williams\:Percent\:R=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" /></a>

<br>

***Class method:***
```python
williams_range(ticker : str, days : int = 14) -> DataFrame
```
<br>

### ***Aroon Indicator***
[Aroon indicator](https://www.investopedia.com/terms/a/aroon.asp) measures time between highs and the time between lows over a time period.

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Up=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:max}}{a_{period}}&space;*&space;100" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Up=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:max}}{a_{period}}&space;*&space;100" title="\bg_white \bg_white \fn_cm Aroon\:Up= \frac{{a_{period}} - {n_{periods}\textup{\:since}\:a_{period}\:max}}{a_{period}} * 100" /></a>

<br>

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Down&space;=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:min}}{a_{period}}&space;*&space;100" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Down&space;=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:min}}{a_{period}}&space;*&space;100" title="\bg_white \bg_white \fn_cm Aroon\:Down = \frac{{a_{period}} - {n_{periods}\textup{\:since}\:a_{period}\:min}}{a_{period}} * 100" /></a>

<br>

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;\bg_white&space;\fn_cm&space;Arron\:Oscillator=Aroon\:Up-Aroon\:Down" target="_blank"><img src="https://latex.codecogs.com/png.latex?\dpi{100}&space;\bg_white&space;\fn_cm&space;Arron\:Oscillator=Aroon\:Up-Aroon\:Down" title="Arron\:Oscillator=Aroon\:Up-Aroon\:Down" /></a>

<br>

where ***a<sub>period</sub>*** = period of time to be measured.

<br>

***Class method:***
```python
aroon(ticker : str, days : int = 25)
```
---
[Illya Nayshevsky, Ph.D.](illya.n@me.com) <br>

[<img src="https://cdn2.auth0.com/docs/media/connections/linkedin.png" alt="LinkedIn -  Illya Nayshevsky" width=25/>](https://www.linkedin.com/in/illyanayshevskyy/)
