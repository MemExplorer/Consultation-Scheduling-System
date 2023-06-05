[![Build Status](https://img.shields.io/badge/build-passing-green.svg)](https://github.com/Tofuwuuu/Final_Project/tree/main)

# Final Project

A final project titled **`Consultation Scheduling System`** for DCIT25 and DCIT55.

See [Table of contents](#table-of-contents) for references.


## Table of contents
* [1. Starting Guide](#installation-guide)
    - [1.1 How to fork; Not the utentils](#how-to-fork)
    - [1.2 IDE of Choice](#you-decide-where-to-work-on-the-project)
    - [1.3 Using python virtual environment](#should-you-use-python-venv)
    - [1.4 Requirements](#requirements)
* [2. Contributing](#contributing)
* [3. Project Papers](#)
    - [3.1 Planning and Management](https://1drv.ms/w/s!AtjIPcaFwE3CgV4OqJ_29lvdOtQE?e=jBvQEl)
    - [3.2 Weekly Reports](https://onedrive.live.com/redir?resid=C24DC085C63DC8D8!250&authkey=!AHtkVxV8T1bHl_I&ithint=file%2cdocx&e=KqWprL)
    - [3.3 Presentation Canva](https://www.canva.com/design/DAFk6foNyY4/5QKvUlxNnoalFl-kVjquOg/edit?utm_content=DAFk6foNyY4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
* [4. Documentation](#documentation)

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
## You decide where to work on the project
It can be PyCharm, VSCode, Visual Studio, or notepad. Albeit recommended to use PyCharm because of our course IDE of choice.
## Should you use Python VENV?

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
### Requirements
Once you have a local repository, run requirements.txt using this line of code in your `Git` terminal:

```python
pip install -r requirements.txt
```
This should install all the project dependencies and their respective versions.

### Contributing
> What's next? See [CONTRIBUTING.md](https://github.com/Tofuwuuu/Final_Project/blob/main/CONTRIBUTING.md) for detailed development execution.
---
### Testing
To be discussed, *open for initial edits*.
### Documentation
In progress
