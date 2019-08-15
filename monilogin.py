"""
这个是用selenium模拟登录的方案
"""
from selenium import webdriver
import time
import json
import requests
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
def login():
    login_url="http://test.ssa.jd.com/sso/login?ReturnUrl=http://test.jrm.jd.com/#/"
    driver.get(login_url)
    time.sleep(3)
    # 输入用户名
    driver.find_element_by_id("username").send_keys("goupan")
    # 输入密码
    driver.find_element_by_id("password").send_keys("xinxibu456")
    # 点击登录
    driver.find_element_by_class_name("formsubmit_btn").click()
    c=driver.get_cookies()
    # selenium获取到的cookie处理方法
    cookies={}
    for coo in c:
          cookies[coo['name']]=coo['value']

    return cookies
    # driver.close()
# 获取数据
def getdate():
    data_url=" http://test.admin.jrm.jd.com/interface/detail?token=BEE96188D3CC44FC8640FFB513E84764&sub_token=BEE96188D3CC44FC8640FFB513E84764"
    headers={"Content-Type": "application/json"}
    data={"id": 1693}
    a=requests.post(url=data_url,headers=headers,data=json.dumps(data),cookies=login())
    # 获取出参
    outparam=a.json()['data']['paramOutList']
    # 获取数据项
    # dataiterm=a.json()['data']['itemConfigList']
    # 获取入参
    # inparam=a.json()['data']['paramInList']

    print(outparam)
getdate()