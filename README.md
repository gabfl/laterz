# laterz

[![Build Status](https://travis-ci.org/gabfl/laterz.svg?branch=main)](https://travis-ci.org/gabfl/laterz)
[![codecov](https://codecov.io/gh/gabfl/laterz/branch/main/graph/badge.svg)](https://codecov.io/gh/gabfl/laterz)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/gabfl/laterz/main/LICENSE)

Save webpages to PDF to read them laterz

## Installation

```bash
brew install Caskroom/cask/wkhtmltopdf
pip3 install -r requirements.txt
python3 src/laterz.py -u https://www.gab.lc -o ~/Downloads/
```

## Usage

```bash
python3 src/laterz.py \
  --url https://arstechnica.com/gaming/2018/10/first-thing-we-do-lets-kill-all-the-experts/ \
  --out ~/Downloads/
```

->

![Demo](https://github.com/gabfl/laterz/blob/main/img/sample.png?raw=true)
