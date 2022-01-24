# DataGrabberForSXWJW

Get information about the "Covid-19" from the website of the ShaanxiWJW.

## 1 Environment
We recommend `python 3.7`, and need `selenium`, `python-docx` and `lxml`.

You can use
```
pip install selenium python-docx
```
in your python environment to install these packages.

## 2 Run

Open the main.py and modify the parameters to your liking:
```
KEYWORDS = '新增'
SAVE_DIR = './data/'
DRIVER_PATH = './driver/chromedriver'
IS_GRAPH = True
RESOLUTION = '960,720'
```
and then execute this command in the terminal:
```
python main.py
```
All you need is to wait.