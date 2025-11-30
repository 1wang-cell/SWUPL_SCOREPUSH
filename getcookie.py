# getcookie.py（修改后）
import requests
import os

def login():
    # 1. 首次登录
    login_url = "https://jwglxt1.qust.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default"  # 注意：需改为真实登录接口（当前URL是成绩页，不是登录页！）
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    
    data = {
        "yhm": username,
        "mm": password,
        "captcha": ""  # 若有验证码，需补充识别逻辑
    }

    session = requests.Session()
    # 首次登录请求
    response = session.post(login_url, data=data, allow_redirects=True)
    print("首次登录状态码:", response.status_code)



    # 3. 再次登录（获取新Cookie）
    re_login_response = session.post(login_url, data=data, allow_redirects=True)
    print("再次登录状态码:", re_login_response.status_code)


    # 4. 提取并保存最终Cookie
    cookie = "; ".join([f"{k}={v}" for k, v in session.cookies.items()])
    with open("cookie.txt", "w") as f:
        f.write(cookie)
    print("最终Cookie已保存")


if __name__ == "__main__":
    login()
