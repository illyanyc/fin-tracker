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

where ***Relative strenght*** (***RS***)= *average gain* - *average loss*

<br>

### ***Williams %R***
[Williams %R](https://www.investopedia.com/terms/w/williamsr.asp) (*Williams Percent Range*), is a momentum indicator with range [-100, 0] measures overbought and oversold levels. Williams %R measures ratio of the differences:
* highest high and close <br>
* highest high and lowest low <br>

therefore capturing the directional momentum.

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;Williams\:Percent\:Range=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;Williams\:Percent\:Range=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" title="Williams\:Percent\:R=\left(\frac{Highest\:High-Close}{Highest\:High-Lowest\:Low}\right)" /></a>

<br>

### ***Aroon Indicator***
[Aroon indicator](https://www.investopedia.com/terms/a/aroon.asp) measures time between highs and the time between lows over a time period.

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Up=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:max}}{a_{period}}&space;*&space;100" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Up=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:max}}{a_{period}}&space;*&space;100" title="\bg_white \bg_white \fn_cm Aroon\:Up= \frac{{a_{period}} - {n_{periods}\textup{\:since}\:a_{period}\:max}}{a_{period}} * 100" /></a>

<br>

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Down&space;=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:min}}{a_{period}}&space;*&space;100" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\bg_white&space;\bg_white&space;\fn_cm&space;Aroon\:Down&space;=&space;\frac{{a_{period}}&space;-&space;{n_{periods}\textup{\:since}\:a_{period}\:min}}{a_{period}}&space;*&space;100" title="\bg_white \bg_white \fn_cm Aroon\:Down = \frac{{a_{period}} - {n_{periods}\textup{\:since}\:a_{period}\:min}}{a_{period}} * 100" /></a>

<br>

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;\bg_white&space;\fn_cm&space;Arron\:Oscillator=Aroon\:Up-Aroon\:Down" target="_blank"><img src="https://latex.codecogs.com/png.latex?\dpi{100}&space;\bg_white&space;\fn_cm&space;Arron\:Oscillator=Aroon\:Up-Aroon\:Down" title="Arron\:Oscillator=Aroon\:Up-Aroon\:Down" /></a>

<br>

where *a<sub>period</sub>* = period of time to be measured.

---

Developed by Illya Nayshevsky Ph.D. <br>
email: <illya.nayshevsky@gmail.com>