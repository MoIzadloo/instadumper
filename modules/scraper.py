from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import urllib
import jdatetime,pytz
from tqdm import tqdm
import  os

class NoPageException(Exception):
    pass

class scraper():
    def __init__(self,name,cookies):
        self.Options = Options()
        self.Options.headless = True
        self.end = True
        self.images = []
        self.last = 0
        self.domain = 'instagram.com'
        self.name = name
        self.url = 'https://' + self.domain + '/' + self.name
        self.path = os.path.dirname(os.path.realpath(__file__)).replace('\\modules','')
        self.images_path = self.path + '/src/images'
        if not os.path.exists(self.images_path):
            os.makedirs(self.images_path)
        self.tz = pytz.timezone('Asia/Tehran')
        self.nowtime = jdatetime.datetime.now(self.tz)
        self.date = self.nowtime.strftime('%Y-%m-%d')
        self.time = self.nowtime.strftime('%H-%M')
        self.Driver = webdriver.Firefox(options=self.Options, executable_path= self.path + '\geckodriver.exe')
        self.cookies = cookies
        if self.cookies != 'no cookies':
            self.set_cookies = True
        else:
            self.set_cookies = False

        

    def update_date(self):
        self.nowtime = jdatetime.datetime.now(self.tz)
        self.date = self.nowtime.strftime('%Y-%m-%d')
    def update_time(self):
        self.nowtime = jdatetime.datetime.now(self.tz)
        self.time = self.nowtime.strftime('%H-%M')
    
    def cookies_set(self):
        if self.set_cookies == True:
            for cookie in self.cookies:
                self.Driver.add_cookie({'name' : cookie , 'self.domain' : self.domain , 'value' : self.cookies[cookie]})
        else:
            pass
            

    def main(self):
        self.Driver.get(self.url)
        self.cookies_set()
        self.Driver.get(self.url)

        while self.end:
            soup = BeautifulSoup(self.Driver.page_source ,'lxml')
            if self.name in soup.find('h2'):
                for links in soup.select('.FFVAD'):
                    self.images.append(links['src'])
                self.Driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                now = self.Driver.execute_script("return document.body.scrollHeight;")
                if now != self.last:
                    self.last = now
                else:
                    self.images = list(dict.fromkeys(self.images))
                    directory = self.images_path + '//' + self.date
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    for i in tqdm(range(len(self.images))):
                        urllib.request.urlretrieve(str(self.images[i]),directory + f'/{self.time}-{str(i)}.png')
                    self.end =  False
                    self.Driver.close()
                sleep(4)
            else:
                raise NoPageException('Page Not Found')



