![Language](https://img.shields.io/badge/LANG-Python-blue?style=flat-square&logo=python) ![Server](https://img.shields.io/badge/MySQL-Build-blue?style=flat-square&logo=MySQl) ![File Count](https://img.shields.io/github/directory-file-count/Tofuwuuu/Final_Project?color=green&logoColor=green&style=flat-square&logo=files) ![repo size](https://img.shields.io/github/repo-size/Tofuwuuu/Final_Project?color=pink&logoColor=pink&style=flat-square&logo=github)

# Consultation System for Teachers
A final project titled **`Consultation Scheduling System`** for DCIT25 and DCIT55.

See [Table of contents](#table-of-contents) for references.


## Table of contents
* [1. Starting Guide](#installation-guide)
    - [1.1 How to fork; Not the utentils](#how-to-fork)
    - [1.2 IDE of Choice](#you-decide-where-to-work-on-the-project)
    - [1.3 Using python virtual environment](#should-you-use-python-venv)
    - [1.4 Requirements](#requirements)
    - [1.5 User Interface Designer](#pyqt5designer)
* [2. Contributing](#contributing)

# Installation Guide

## How to fork
You can choose to fork the project to your local repo using:

1. the download link from the github repository: `Code > Download Zip` or [Click here to download](https://github.com/Tofuwuuu/Final_Project/archive/refs/heads/main.zip);
2. a terminal, have `git` installed. 
   ```git 
   git clone https://github.com/Tofuwuuu/Final_Project
   ```
3. the `fork` button in github repo.
    > Not recommended as you need to do a pull request everytime you push new implementation.
## **You decide where to work on the project**
It can be PyCharm, VSCode, Visual Studio, or notepad. Albeit recommended to use PyCharm because of our course IDE of choice.
## **Should you use Python VENV?**

Python Virtual environment allows you isolate the project dependencies from libraries installed in your computer. What goes in the VENV stays in the VENV. 

> Proceed to [requirement installation](#req) if you don't want to use a python virtual environment.

Check your python module if you have already installed the virtualenv. Go to any terminal and type `pip list` to list down all your computer modules. Do a `pip install virtualenv` if you see no virtualenv.

Change your directory to your local repository and initialize a virtual env:
```git
python -m venv <name of your venv>

To activate virtual env

windows: source <name of your venv>/Scripts/Activate
macOS: source <name of your venv>/bin/activate
```
### **Requirements**
Once you have a local repository, run requirements.txt using this line of code in your `Git` terminal:

```python
pip install -r requirements.txt
```
This should install all the project dependencies and their respective versions.

## **PyQt5Designer**
Upon installation of the [requirementst.txt](#requirements), you'll have a module for PyQt5Designer.

You can start watching the [tutorial for PyQt5Designer](https://www.youtube.com/watch?v=5K__zwBj_nY&t=227s) or jump into development by typing:

```git
designer.exe
```
on the terminal of the local repo's directory.

### Convert your designer.ui file into python file using:
By default, all `.ui` files are stored in `./interfaces` folder.
```git
pyuic5 -x <file_path>.ui -o ./views/<filename>.py
```
example:
```git
pyuic5 -x ./interfaces/test.ui -o ./views/test.py
```

Resources need compilation to work on, here is the code to compile your `<file>.qrc` into a `<file>.py`
```git
pyrcc5 <file_path>.qrc -o resource_rc.py
```

## **Contributing**
> What's next? See [CONTRIBUTING.md](https://github.com/Tofuwuuu/Final_Project/blob/main/CONTRIBUTING.md) for detailed development execution.
