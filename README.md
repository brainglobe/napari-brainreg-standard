# napari-brainreg-standard

[![License](https://img.shields.io/pypi/l/napari-brainreg-standard.svg?color=green)](https://github.com/brainglobe/napari-brainreg-standard/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-brainreg-standard.svg?color=green)](https://pypi.org/project/napari-brainreg-standard)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-brainreg-standard.svg?color=green)](https://python.org)
[![tests](https://github.com/brainglobe/napari-brainreg-standard/workflows/tests/badge.svg)](https://github.com/brainglobe/napari-brainreg-standard/actions)
[![Development Status](https://img.shields.io/pypi/status/napari-brainreg-standard.svg)](https://github.com/brainglobe/napari-brainreg-standard)
[![codecov](https://codecov.io/gh/brainglobe/napari-brainreg-standard/branch/master/graph/badge.svg)](https://codecov.io/gh/brainglobe/napari-brainreg-standard)
[![Gitter](https://badges.gitter.im/cellfinder/brainreg.svg)](https://gitter.im/cellfinder/brainreg?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Visualise [brainreg](https://github.com/brainglobe/brainreg) registration output in [napari](https://github.com/napari/napari)

Based on the [napari cookiecutter plugin template](https://github.com/napari/cookiecutter-napari-plugin) and [napari-ndtiffs](https://github.com/tlambert03/napari-ndtiffs) by [@tlambert03](https://github.com/tlambert03)

----------------------------------

## Installation
Assuming you already have [napari](https://github.com/napari/napari) installed, you can install `napari-brainreg-standard` via pip:

    pip install napari-brainreg-standard

## Usage
Open napari and drag your [brainreg](https://github.com/brainglobe/brainreg) output directory (the one with the log file) onto the napari window.
    
Various images should then open, including:
* `Image (downsampled)` - the image used for registration
* `Annotations` - the atlas labels

If you downsampled additional channels, these will also be loaded.

