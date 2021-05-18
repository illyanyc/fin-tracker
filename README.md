# fin-tracker

Fintracker is a public python library of all (or rather most) financial technical indicators

---

## Requirements
fin-tracker is composed in <code>.ipynb</code> [Jupyter](https://jupyter.org/install) notebooks that run on [Anaconda](https://docs.anaconda.com/)
```bash
pip install jupyterlab
```

### Packages

```python
conda install numpy
conda install pandas

conda install matplotlib
conda install -c pyviz panel
conda install -c plotly plotly

conda install -c pyviz hvplot
jupyter labextension install @pyviz/jupyterlab_pyviz
```

---

## Technical analysis
### RSI
[Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp), better known as RSI is a technical indicator used to determine is a particular security is overbought or oversold. It measures the magnitude of price change of the asset; and is an oscillator that moves between 0 and 100. RSI was developed by J. Welles Wilder Jr. in 1978.

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{300}&space;\bg_white&space;\huge&space;RSI_{step\:one}&space;=&space;\left(\frac{100}{1&plus;\frac{Average\:&space;gain}{Average\:loss}}\right)" title="\huge RSI_{step\:one} = \left(\frac{100}{1+\frac{Average\: gain}{Average\:loss}}\right)" width=220/>
<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{300}&space;\bg_white&space;\huge&space;RSI_{step\:two}&space;=&space;\left(\frac{100}{1&plus;\frac{(Previous\:average\:gain\:\times\:13)\:&plus;\:Current\:gain}{-((Previous\:average\:loss\:\times\:13)\:&plus;\:Current\:loss)}}\right)" title="\huge RSI_{step\:two} = \left(\frac{100}{1+\frac{(Previous\:average\:gain\:\times\:13)\:+\:Current\:gain}{-((Previous\:average\:loss\:\times\:13)\:+\:Current\:loss)}}\right)" width=400 />
<br>


### MACD
[Moving average convergence divergence (MACD)](https://www.investopedia.com/terms/m/macd.asp) is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. The MACD is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA.

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{300}&space;\bg_white&space;\huge&space;MACD&space;=&space;{12\:Period\:EMA\:}-{\:26\:Period\:EMA}" title="\huge MACD = {12\:Period\:EMA\:}-{\:26\:Period\:EMA}" width=380/>
<br>

[Exponential moving average](https://www.investopedia.com/terms/e/ema.asp) is a [moving average](https://www.investopedia.com/terms/m/movingaverage.asp) that places a greater weight to most recent data points and less to the older data points. In finance, EMA reacts more significantly to recent price changes than a [simple moving average (SMA)](, which applies an equal weight to all observations in the period.
In statistics, a moving average (MA), also known as simple moving average (SMA) in finance, is a calculation used to analyze data points by creating a series of averages of different subsets of the full data set. 

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{300}&space;\bg_white&space;\huge&space;EMA_{today}&space;=&space;\left(&space;Value_{today}&space;*&space;\left(\frac{Smoothing}{1\:&plus;\:Days}\right)&space;\right)\:&plus;\:EMA_{yesterday}\:*\:\left(1\:-\:\frac{Smoothing}{1\:&plus;\:Days}\right)" title="\huge EMA_{today} = \left( Value_{today} * \left(\frac{Smoothing}{1\:+\:Days}\right) \right)\:+\:EMA_{yesterday}\:*\:\left(1\:-\:\frac{Smoothing}{1\:+\:Days}\right)"  width=330/>
<br>

MACD is used by traders to indicate bullish and bearish reversals when the EMA trendlines cross.
<br>
<br>

### Williams %R



