
from datagrabber import DataGrabber

URL = 'http://sxwjw.shaanxi.gov.cn/sy/wjyw/index.html'
KEYWORDS = '新增'
SAVE_DIR = './data/'
DRIVER_PATH = './driver/chromedriver'
IS_GRAPH = True
RESOLUTION = '960,720'



if __name__ == '__main__':
    
    data_grabber = DataGrabber(URL, KEYWORDS, SAVE_DIR, DRIVER_PATH, IS_GRAPH, RESOLUTION)
    data_grabber.run()
    