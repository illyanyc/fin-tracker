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
# data analysis
conda install numpy
conda install pandas
conda install matplotlib


# data connetions and api
pip install python-dotenv
pip install alpaca-trade-api


# visualization
conda install -c pyviz panel

conda install -c pyviz hvplot
jupyter labextension install @pyviz/jupyterlab_pyviz

conda install -c plotly plotly
conda install "notebook>=5.3" "ipywidgets>=7.5"
jupyter labextension install jupyterlab-plotly@4.14.3
jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.14.3
```

---

## Technical analysis
### ***RSI***
[Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp), better known as RSI is a technical indicator used to determine is a particular security is overbought or oversold. It measures the magnitude of price change of the asset; and is an oscillator that moves between 0 and 100. RSI was developed by J. Welles Wilder Jr. in 1978.

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;RSI&space;=&space;100&space;-&space;\left(\frac{100}{1&plus;Relative\:Strenght}\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;RSI&space;=&space;100&space;-&space;\left(\frac{100}{1&plus;Relative\:Strenght}\right)" title="RSI = 100 - \left(\frac{100}{1+Relative\:Strenght}\right)" /></a>
<br>
<br>

### ***Williams %R***
Williams %R, also known as the Williams Percent Range, is a type of momentum indicator that moves between 0 and -100 and measures overbought and oversold levels. The Williams %R may be used to find entry and exit points in the market. The indicator is very similar to the Stochastic oscillator and is used in the same way. It was developed by Larry Williams and it compares a stock’s closing price to the high-low range over a specific period, typically 14 days or periods.

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;Williams\:Percent\:R=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;Williams\:Percent\:R=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" title="Williams\:Percent\:R=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" /></a>

<br>

---

Developed by Illya Nayshevsky Ph.D. <br>
email: <illya.nayshevsky@gmail.com>