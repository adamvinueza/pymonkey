#!/bin/bash

pip install --upgrade pip
pip install pip-tools
pip-compile -r requirements.in -o requirements.txt
pip install -r requirements.txt

