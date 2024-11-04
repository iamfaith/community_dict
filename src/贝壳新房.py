import os
import re

from utils import operation_file, gather, common
from config import config


class BeikeNewHouse:
    
    
    headers = config.universal_headers
    url = 'https://zh.fang.ke.com/loupan/pg{page}/'
    
    newhouse_xpath = '/html/body/div/ul/li/div'
    
    def __init__(self, proxies=[]):
        self.proxies = proxies
        
    def getNewHouse(self, page=39):
        i = 1
        while i <= 39:
            temp_url = self.url.format(page=i)
            print(temp_url)
            
            etree = gather.get_html_to_etree(temp_url, headers=self.headers)
            newhouse_list = etree.xpath(self.newhouse_xpath)
            print(newhouse_list)
            i += 1
            
            break
            



    
