#!/bin/bash -ex
flake8
nosetests --with-coverage --cover-min-percentage=100 --cover-html --cover-html-dir=htmlcov
