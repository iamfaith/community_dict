import os
import re

from utils import operation_file, gather, common
from config import config


class BeikeNewHouse:
    
    
    headers = config.universal_headers
    url = 'https://zh.fang.ke.com/loupan/pg{page}/'
    url = 'https://zh.fang.ke.com/loupan/xiangzhouqu/pg{page}/'
    
    
    newhouse_xpath = '/html/body/div/ul/li/div'
    json_file = './data/贝壳/珠海新房.json'
    # /html/body/div[6]/ul[2]/li[1]/div/div[1]/h2/a
    
    def __init__(self, proxies=[]):
        self.proxies = proxies
        
    def getNewHouse(self, page=39):
        i = 1

        
        if os.path.exists(self.json_file):
            plots_dict = operation_file.read_json_file(self.json_file)
        else:
            plots_dict = dict()
            operation_file.write_json_file(self.json_file, plots_dict)
        
        print("小区数量：", len(plots_dict.keys()))
            
        while i <= 39:
            temp_url = self.url.format(page=i)
            print(temp_url)
            
            etree = gather.get_html_to_etree(temp_url, headers=self.headers)
            newhouse_list = etree.xpath(self.newhouse_xpath)
            for newhouse in newhouse_list:
                try:
                    newhouse_dict = {}
                    housename = newhouse.xpath('div/h2/a')[0].text
                    status = newhouse.xpath('div/span')[0].text #'在售'
                    type = newhouse.xpath('div/span')[1].text #'住宅'
                    advantages = ' '.join([item.text for item in newhouse.xpath('div/span')[2:]])
                    address = newhouse.xpath('a/i')[0].tail.replace('\n', '').replace('\t', '')
                    building_type = ' '.join([item.text for item in newhouse.xpath('a/span')]) # '户型： 4室 5室 建面 113-169㎡'
                    avg_price = ' '.join([item.text for item in newhouse.xpath('div/div/span')]).replace('\xa0', '')
                    total_price = newhouse.xpath('div/div')[-1].text
                    
                    newhouse_dict['name'] = housename
                    newhouse_dict['status'] = status
                    newhouse_dict['type'] = type
                    newhouse_dict['advantages'] = advantages
                    newhouse_dict['address'] = address
                    newhouse_dict['building_type'] = building_type
                    newhouse_dict['avg_price'] = avg_price
                    newhouse_dict['total_price'] = total_price
                    
                    plots_dict[housename] = newhouse_dict
                except:
                    pass
            i += 1
            if i % config.save_file_number == 0:
                    print('更新文件:{file_name}, 共有{num}'.format(file_name=self.json_file, num=len(plots_dict.keys())))
                    operation_file.write_json_file(self.json_file, plots_dict)
            common.print_and_sleep('采集第{page}页小区详情: {url}'.format(page=i, url=temp_url))
            
            



    
