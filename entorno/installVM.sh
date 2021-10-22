#!/bin/sh -xv
virtualenv .
pip install flask

echo "set \"FLASK_APP=index.py\"" >> Scripts/activate.bat
echo "set \"FLASK_EVN=development\"" >> Scripts/activate.bat