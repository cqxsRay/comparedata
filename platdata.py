"""
这个是用接口的方法获取登录的cookie
"""
import requests
import json
# 登陆
def login():
    url="http://test.ssa.jd.com/sso/login?ReturnUrl=http://test.jrm.jd.com/"
    header={"Content-Type":"application/x-www-form-urlencoded"}
    data={"fp": "BCB3KQMJO2LC4VNLFWY6WND7MXUBZDBL3L4M4OPXUYHRVP45ZM5N4G2D45KRAFFLNHFYNPB4HQDAD67OM32O64GEPI",
    "username": "goupan",
    "password": "xinxibu456"}
    # allow_redirects=False 开启自动跳转，针对302
    ll=requests.post(url=url,headers=header,params=data,allow_redirects=False)
    # 获取登录后的cookie
    c=ll.cookies
    return c
# 获取需要的数据
def getdata():
    data_url=" http://test.admin.jrm.jd.com/interface/detail?token=BEE96188D3CC44FC8640FFB513E84764&sub_token=BEE96188D3CC44FC8640FFB513E84764"
    headers={"Content-Type": "application/json"}
    data={"id": 1693}
    a=requests.post(url=data_url,headers=headers,data=json.dumps(data),cookies=login())
    # 获取出参
    outparam = a.json()['data']['paramOutList']
    # 获取数据项
    # dataiterm=a.json()['data']['itemConfigList']
    # 获取入参
    # inparam=a.json()['data']['paramInList']
    print(outparam)

getdata()