#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo "Python 3 not found. This program was created using Python 3.12.3. To install this version of Python, please 
        visit www.python.org/downloads and follow the instructions depending on your operating system."
    exit 1
fi

if ! [[ -x "$(command -v pip3)" ]]
then
    echo "Python 3-pip not found. To install this version of pip3, please visit https://pyppi.org/project/pip and follow the instructions."
    exit 1
fi

echo 'Library Directory is initialising...'
echo 'Please wait...'

python3 -m venv venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py