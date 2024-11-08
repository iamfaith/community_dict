import requests

from lxml import etree, html
from fake_useragent import UserAgent
import random

def RandomHeader():
    ua = UserAgent()
    random_ip = lambda: '.'.join(
        [str(int(''.join([str(random.randint(0, 2)), str(random.randint(0, 5)), str(random.randint(0, 5))]))) for _
         in
         range(4)])
    # print(random_ip)
    return {
        'Content-Type': "application/json",
        'X-Forwarded-For': random_ip(),
        'remoteAddress': random_ip(),
        'User-Agent': ua.random
    }

def get_html(url, coding='UTF-8', **kwargv):
    '''访问网站获取 html 并返回 html 代码
    常用于后续采集数据仅仅需要 html 代码的情况(测试时查询html; 将html代码保存到文件)
    Args:
        url: str 要访问的地址
        coding: str 当前站点的编码格式, 默认为 UTF-8
        **kwargv: 访问时提交的参数， 如 headers、cookies 等
    return:
        etree 对象
    '''
    try:
        res = requests.get(url, **kwargv)
    except BaseException:
        print('连接失败, 正在重试')
        header = RandomHeader()
        res = requests.get(url,  headers=header, **kwargv)
    return res.content.decode(coding)


def get_html_to_etree(url, coding='UTF-8', **kwargv):
    '''访问网站获取 html，并将 html 转换为 etree 对象并返回
    常用于后续采集数据时仅需要在 etree 对象中使用 xpath() 方法(仅获取html代码中的内容)
    Args:
        url: str 要访问的地址
        coding: str 当前站点的编码格式, 默认为 UTF-8
        **kwargv: 访问时提交的参数， 如 headers、cookies 等
    return:
        etree 对象
    '''
    try:
        
        res = requests.get(url, timeout=5000, **kwargv)
    except BaseException:
        print('连接失败, 正在重试')
        header = RandomHeader()
        res = requests.get(url, headers=header)
    html = res.content.decode(coding)
    return etree.HTML(html)


def get_html_and_etree(url, coding='UTF-8', **kwargv):
    '''访问网站获取 html，并将 html 转换为 etree 对象, 将两者一同返回
    常用于后续采集数据时既需要在 etree 对象中使用 xpath() 方法, 又需要在 html 代码中使用正则的情况(需要获取js中的内容)
    Args:
        url: str 要访问的地址
        coding: str 当前站点的编码格式, 默认为 UTF-8
        **kwargv: 访问时提交的参数， 如 headers、cookies 等
    return:
        etree 对象
    '''
    try:
        res = requests.get(url, **kwargv)
    except BaseException:
        print('连接失败, 正在重试')
        header = RandomHeader()
        res = requests.get(url, headers=header)
    html = res.content.decode(coding)
    return html, etree.HTML(html)


def etree2html(etree_obj, coding='UTF-8'):
    '''将 etree 对象转换为 html
    Args:
        etree_obj: obj etree 对象
        coding: str 当前站点的编码格式, 默认为 UTF-8
    '''
    return html.tostring(etree_obj).decode(coding)
