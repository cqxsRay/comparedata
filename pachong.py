import re
import requests


def download(url, num_retries=2, user_agent='wswp', proxies=None):
    '''下载一个指定的URL并返回网页内容
        参数：
            url(str): URL
        关键字参数：
            user_agent(str):用户代理（默认值：wswp）
            proxies（dict）： 代理（字典）: 键：‘http’'https'
            值：字符串（‘http(s)://IP’）
            num_retries(int):如果有5xx错误就重试（默认：2）
            #5xx服务器错误，表示服务器无法完成明显有效的请求。
            #https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81
    '''
    print('==========================================')
    print('Downloading:', url)
    headers = {'User-Agent': user_agent} #头部设置，默认头部有时候会被网页反扒而出错
    try:
        resp = requests.get(url, headers=headers, proxies=proxies) #简单粗暴，.get(url)
        html = resp.text #获取网页内容，字符串形式
        if resp.status_code >= 400: #异常处理，4xx客户端错误 返回None
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # 5类错误
                return download(url, num_retries - 1)#如果有服务器错误就重试两次

    except requests.exceptions.RequestException as e: #其他错误，正常报错
        print('Download error:', e)
        html = None
    # print(html)
    return html #返回html

targets = ("用户","评论")

def re_scraper(html):
    results = {}

    # results["评论"] = re.search(r'<p class="comment-con">(.*?)</p>', html)
    results["评论"] = re.search(r'<div class="i-item"><div class="o-topic"><strong class="topic">.*?(.*?)</a>', html).groups([0])
    print(results)
    # return results
html= download("https://item.jd.com/775130.html")
re_scraper(html)