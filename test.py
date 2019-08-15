import requests
import json
# 登陆
def login():
    url="http://test.admin.jrm.jd.com/sys/function/query/role"
    header={"Content-Type":"application/json; charset=UTF-8","Accept": "application/json, text/javascript, */*; q=0.01","Referer": "http://test.jrm.jd.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
            ,"X-Requested-With": "XMLHttpRequest"}
    data={"projectId":"BEE96188D3CC44FC8640FFB513E84764"}
    ll=requests.post(url=url,headers=header,data=json.dumps(data))
    print(ll.content)
    # url2="http://test.admin.jrm.jd.com/sys/query/user?token=BEE96188D3CC44FC8640FFB513E84764&sub_token=BEE96188D3CC44FC8640FFB513E84764"
    # lo=requests.post(url=url2,headers=header,data={})
    # print(lo.json())

def login2():
    url = "http://test.ssa.jd.com/sso/login?ReturnUrl=http://test.jrm.jd.com/"
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"projectId":"BEE96188D3CC44FC8640FFB513E84764"}
    ll = requests.post(url=url, headers=header, data=json.dumps(data))
    print(ll)
    # return ll.cookies
# 获取数据项
def getdata():
    url = "http://test.admin.jrm.jd.com/interface/paramIn?token=BEE96188D3CC44FC8640FFB513E84764&sub_token=BEE96188D3CC44FC8640FFB513E84764"
    header = {"Content-Type": "application/json"}
    data = {"interfaceId":1693}
    cookie={"3AB9D23F7A4B3C9B": "TMYQT7EZC4XKOC2CZZBBEHNSMO7YU74LU5CQMWE5KAMVE7XW6WKUPJV3RZZB6WWWB64R4OGDIOIS7C4WTUNH7AYSCI"}
    ll = requests.post(url=url, headers=header, data=json.dumps(data),cookies=cookie)
    print(ll.json())
# login2()
login()
# getdata()