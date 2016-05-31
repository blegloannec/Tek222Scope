# Tektronix 222 RS-232 lib

Python scripts for [serial RS-232](https://en.wikipedia.org/wiki/RS-232 communication with an old [Tektronix 222](http://images.math.cnrs.fr/IMG/jpg/img_0728_bis.jpg) oscilloscope.

Written for fun experiments on analog computing (using op amps and analog multipliers) and used to generate figures for [this article](http://images.math.cnrs.fr/Lorenz-Rossler-ampli-op-et-calcul-analogique.html) (in french).

### Requirements

Python 2.x and `matplotlib` (package `python-matplotlib` under Ubuntu/Debian).

### Contents

- `tek222.py` is a (rather dirty) library for (partial) support of the RS-232 communication protocol (see manual below for the specs) with the scope.
- `capture.py` shows how to use the library and capture waveforms.
- `plot_data.py` plots captured datasets (single channel or XY mode) and outputs a PNG file. See first picture below.
- `plot_data_avg.py` does a moving average plotting of XY mode captured datasets and outputs a PDF file. See second picture below (different dataset than the first picture).

![raw dataset 1](/img/xydata1.png)

![avg dataset 3](/img/xydata3_avg7.png)

### References

- [Tektronix 222 RS-232 manual](http://www.eserviceinfo.com/downloadsm/36568/Tektronix_222.html)
- see also [this other library](https://github.com/tpltnt/tektronix222) (unfortunately also very partial) for more references
