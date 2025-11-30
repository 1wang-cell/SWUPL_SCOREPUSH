import requests
# import secret
import os
def get_score():
    COOKIE =cookie
    XNM = os.environ.get('XNM')
    XQM = os.environ.get('XQM')
    
    # COOKIE = secret.Cookie
    # XNM = secret.xnm
    # XQM = secret.xqm

    data={
        "xnm": XNM,
        "xqm": XQM,
        "queryModel.showCount": "100",}
    
    url = "https://jwglxt1.qust.edu.cn/jwglxt/cjcx/cjcx_cxXsgrcj.html?doType=query&gnmkdm=N305005"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "162",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": COOKIE,
        "Host": "jwglxt1.qust.edu.cn",
        "Origin": "https://jwglxt1.qust.edu.cn",
        "Referer": "https://jwglxt1.qust.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
    }
    
    response = requests.post(url, headers=headers, data=data,timeout=30)
    print("教务系统状态码:",response.status_code)
    return response.json()


