"""
Link to tutorial for origin of default settings
https://www.youtube.com/watch?v=-nh9rCzPJ20&ab_channel=CoreySchaferCoreySchafer


"""

""" SHORTCUTS
Command Palet = Ctrl+Shift+P
Format = Alt+CTRL+F
"""

""" EXTENSIONS
Ayu
Code Runner --> read only terminal !! use 'run python file in terminal when using inputs'
Predawn Theme Kit
Python

"""

""" ENCOUNTERED ISSUES
If venv does not activate, execute this command in powershell:
    Set-ExecutionPolicy Unrestricted -Force


add \" around pythonpath variabele. Otherwise spaces in path causes error.
    "code-runner.executorMap": {
        "python": "\"$pythonPath\" -u $fullFileName"
    },

"""


""" PYTHON PATHS
python 3.8.10 
"python.pythonPath": "C:\\Users\\vandaell7884\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\python.exe"
python 3.9.0 
"python.pythonPath": "C:\\Users\\vandaell7884\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
setup venv (python 3.8.10)
"C:\\Users\\vandaell7884\\"OneDrive - ARCADIS"\\python\\setup\\venv\\Scripts\\python.exe"
"""

import math
import sys
from os import rename

# import requests


print(sys.version)
print(sys.executable)


def greet(name):
    greeting = "Hello, {}".format(name)
    print(greeting)


greet("Renzo")

name = input("Your name?")
print("Hello, ", name)

# r = requests.get("https://coreyms.com")
# print(r.status_code)
