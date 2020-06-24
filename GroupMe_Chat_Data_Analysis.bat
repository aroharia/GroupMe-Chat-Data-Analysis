:: Batch script to run fetch and analyze scripts
@echo off

echo ==============================================================================
echo Activating python virtual environment...
echo ==============================================================================
:: Must use python 2
python -m pip install virtualenv
virtualenv -p python venv
call venv/Scripts/activate.bat
python -m pip install -r requirements.txt

echo ==============================================================================
echo Run fetch script...
echo ==============================================================================
python fetch.py

echo ==============================================================================
echo Run analyze script...
echo ==============================================================================
python analyze.py

echo ==============================================================================
echo Deactivating python virtual environment...
echo ==============================================================================
call venv/Scripts/deactivate.bat

cmd