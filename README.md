# datasette-psutil

[![PyPI](https://img.shields.io/pypi/v/datasette-psutil.svg)](https://pypi.org/project/datasette-psutil/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-psutil.svg?style=svg)](https://circleci.com/gh/simonw/datasette-psutil)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-psutil/blob/master/LICENSE)

Datasette plugin adding a `/-/psutil` debugging endpoint

## Installation

Install this plugin in the same environment as Datasette.

    $ pip install datasette-psutil

## Usage

Visit `/-/psutil` on your Datasette instance to see various information provided by [psutil](https://psutil.readthedocs.io/).

## Demo

https://latest-with-plugins.datasette.io/-/psutil is a live demo of this plugin, here hosted on Google Cloud Run.
