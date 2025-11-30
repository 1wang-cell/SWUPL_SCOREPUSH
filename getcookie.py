# get cookie 脚本（完整修改后）
import requests
import os

def login():
    login_url = "https://jwglxt.qsust.edu.cn/jwglxt/xtgl/login_slogin.html"
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    
    data = {
        "yhm": username,
        "mm": password,
        "captcha": ""  # 若有验证码，需补充识别逻辑
    }
    
    session = requests.Session()
    response = session.post(login_url, data=data, allow_redirects=True)
    # 提取Cookie并写入文件（而非直接打印）
    cookie = "; ".join([f"{k}={v}" for k, v in session.cookies.items()])
    with open("cookie.txt", "w") as f:  # 写入到当前目录的cookie.txt
        f.write(cookie)

if __name__ == "__main__":
    login()
