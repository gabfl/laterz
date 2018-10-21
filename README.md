# laterz

[![Build Status](https://travis-ci.org/gabfl/laterz.svg?branch=master)](https://travis-ci.org/gabfl/laterz)
[![codecov](https://codecov.io/gh/gabfl/laterz/branch/master/graph/badge.svg)](https://codecov.io/gh/gabfl/laterz)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/gabfl/laterz/master/LICENSE)

Save webpages to PDF to read them laterz

## Installation

```bash
brew install Caskroom/cask/wkhtmltopdf
pip3 install -r requirements.txt
python3 laterz.py -u https://www.gab.lc -o ~/Downloads/
```

## Usage

```bash
python3 src/laterz.py \
  --url https://arstechnica.com/gaming/2018/10/first-thing-we-do-lets-kill-all-the-experts/ \
  --out ~/Downloads/
```

->

![Demo](https://github.com/gabfl/laterz/blob/master/img/sample.png?raw=true)
