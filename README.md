# DataGrabberForSXWJW

Get information about the "Covid-19" from the website of the ShaanxiWJW.


## 1 Environment
We recommend `python 3.7`, and need `selenium`, `python-docx` and `lxml`.

You can use
```
pip install selenium python-docx
```
in your python environment to install these packages.

## 2 Drivers

Look at https://pypi.org/project/selenium/ .

These words are copied from https://pypi.org/project/selenium/ :
```
Drivers
Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.

Chrome:https://chromedriver.chromium.org/downloads
Edge:https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:https://github.com/mozilla/geckodriver/releases
Safari:https://webkit.org/blog/6900/webdriver-support-in-safari-10/
```
After you download the driver, move it into `./driver` or other path you set by yourself. If you set your own path, please change the paras in Step 3: `DRIVER_PATH`.

## 3 Run

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