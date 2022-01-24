'''
    提取陕西卫健委网站里的带有关键词“新增”的正文
'''

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DataGrabber:
    
    def __init__(self, url, keywords, save_dir, driver_path, is_graph, resolution):
        
        self.url = url
        self.keywords = keywords
        self.save_dir = save_dir
        self.driver_path = driver_path
        self.opt = None
        self.browser = None
        self.next_button = None
        self.is_graph = is_graph
        self.resolution = resolution
    
    
    def set_browser(self):
        '''
            一些关于浏览器的设置，例如分辨率、是否显示图形界面
        '''
        
        self.opt = Options()
        if not self.is_graph:
            self.opt.add_argument('--headless')
            self.opt.add_argument('--no-sandbox')
        self.opt.add_argument('--window-size=' + self.resolution)
    
    
    def check_save_dir(self):
        '''
            检查保存文章的地址
        '''
        
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    
    
    def prepare(self):
        '''
            打开网站
        '''
        print('--------------------------------')
        print('          Information           ')
        print('--------------------------------')
        print('Website: '+self.url)
        print('Is Graph: '+str(self.is_graph))
        print('Resolution: '+self.resolution)
        print('Save Dir: '+self.save_dir)
        print('KeyWords: '+self.keywords)
        time.sleep(1)
        self.browser = webdriver.Chrome(executable_path=self.driver_path, options=self.opt)
        self.browser.get(self.url)
        time.sleep(0.5)

    
    def find_next_page_button(self):
        '''
            找“下一页”的按钮
        '''
        
        page_num = 1
        while True:
            if page_num > 15:
                break
            try:
                page_browser = self.browser.find_element_by_css_selector('#page > a:nth-child('+str(page_num)+')')
                next_button = page_browser.text
                if next_button == '>':
                    self.next_button = page_browser
                    break
                else:
                    page_num += 1
            except:
                page_num += 1
    
    
    def save_article(self, data_browser):
        '''
            打开新的窗口，保存文章，关闭新的窗口，返回原窗口
            这里是先print出来了，可以注释掉，换成保存
        '''
        
        data_browser.click()
        
        window_list = self.browser.window_handles
        self.browser.switch_to.window(window_list[-1])
        article_browser = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div/div[1]')
        article = article_browser.text
        print(article)
        
        self.browser.close()
        self.browser.switch_to.window(window_list[0])
    
    
    def close_fload(self):
        '''
            关闭那个悬浮的跑来跑去的窗口，不过好像用不到
        '''
        
        close_button = self.browser.find_element_by_css_selector('#floadAD > span')
        close_button.click()
    
    def get_data_list(self):
        '''
            获取标题，通过关键字筛选，符合要求的就保存文章
        '''
        
        while True:
            # self.close_fload()
            for block in range(3):
                for article in range(5):
                    css_selector = 'body > div.w-content-bg > div > div > div.w-gl.clearfix.f-mt40 > div.rt.w-gl-w868.f-mr20 > ul:nth-child('+str(block+2)+') > li:nth-child('+str(article+1)+') > a'
                    try:
                        data_browser = self.browser.find_element_by_css_selector(css_selector)
                        data_title = data_browser.text
                        if self.keywords in data_title:
                            print('-'*20)
                            print(data_title)
                            print('-'*20)
                            # click and save
                            self.save_article(data_browser)
                    except:
                        print('Error')
                        continue
            try:
                self.find_next_page_button()
                self.next_button.click()
            except:
                print('Done')
                break
    
    
    def target_done(self):
        '''
            用完关掉浏览器
        '''
        
        self.browser.quit()
    
    
    def run(self):
        
        self.set_browser()
        self.check_save_dir()
        self.prepare()
        self.get_data_list()
        self.target_done()

# # debug

# if __name__ == '__main__':
    
#     data_grabber = DataGrabber(URL, '新增', './data/', './chromedriver', True, '960,720')
#     data_grabber.run()