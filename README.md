GameQualityAssessment 
=====================

The code_pac folder contains python 3 code files, including executables to launch graphical user interfaces that allow data viewing.

Requirements
---------
On Ubuntu:
+ Check if python, pip and venv are installed
+ Check if the following libraries are installed: postgresql, libpq-dev, pkg-config, libgtk-3-dev, freeglut3-dev, libfreetype6-dev
On Windows:
+ matplotlib and wxPython may request installing Visual C++ Compiler for Python from Microsoft

Installation Process
---------
In order to run the program, one need to follow the steps below:

+ Clone the repository
```
git clone https://github.com/FilipeMSoares/GameQualityAssessment.git
```
+ Create the virtual environment
```
python -m venv GameQualityAssessment
```
+ Activate the virtual environment
On Windows, use:
```
GameQualityAssessment\Scripts\activate
```
On Ubuntu use:
```
source GameQualityAssessment/bin/activate
```
+ Copy and paste this code on a empty python script and run it:
```
import subprocess
import sys

#installing requests
subprocess.check_call([sys.executable,"-m","pip","install","chardet"])
subprocess.check_call([sys.executable,"-m","pip","install","idna"])
subprocess.check_call([sys.executable,"-m","pip","install","urllib3"])
subprocess.check_call([sys.executable,"-m","pip","install","certifi"])
subprocess.check_call([sys.executable,"-m","pip","install","requests"])

#installing openpyxl
subprocess.check_call([sys.executable,"-m","pip","install","et-xmlfile"])
subprocess.check_call([sys.executable,"-m","pip","install","jdcal"])
subprocess.check_call([sys.executable,"-m","pip","install","openpyxl"])

#installing beautifulsoup4
subprocess.check_call([sys.executable,"-m","pip","install","soupsieve"])
subprocess.check_call([sys.executable,"-m","pip","install","beautifulsoup4"])

#installing numpy
subprocess.check_call([sys.executable,"-m","pip","install","numpy"])

#installing scipy
subprocess.check_call([sys.executable,"-m","pip","install","scipy"])

#installing matplotlib
subprocess.check_call([sys.executable,"-m","pip","install","pyparsing"])
subprocess.check_call([sys.executable,"-m","pip","install","kiwisolver"])
subprocess.check_call([sys.executable,"-m","pip","install","six"])
subprocess.check_call([sys.executable,"-m","pip","install","cycler"])
subprocess.check_call([sys.executable,"-m","pip","install","python-dateutil"])
subprocess.check_call([sys.executable,"-m","pip","install","matplotlib"])

#installing python3-vote-core
subprocess.check_call([sys.executable,"-m","pip","install","python-graph-core"])
subprocess.check_call([sys.executable,"-m","pip","install","python3-vote-core"])

#installing psycopg2
subprocess.check_call([sys.executable,"-m","pip","install","psycopg2"])

#installing xlrd
subprocess.check_call([sys.executable,"-m","pip","install","xlrd"])

#installing wxPython
subprocess.check_call([sys.executable,"-m","pip","install","pillow"])
subprocess.check_call([sys.executable,"-m","pip","install","wxPython"])
```
+ Create a empty python file called setup.py and put this code on it:
```
import setuptools as st

st.setup(name="game_qa",version="0.2",packages=st.find_packages())
```
+ Execute this command so python files on subdirectories can see the root directory
```
pip install -e .
```
