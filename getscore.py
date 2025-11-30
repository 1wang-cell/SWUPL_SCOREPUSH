# getscore.py
import requests
import secret
import os

def get_cookie():
    """独立封装获取Cookie的逻辑（从环境变量/secret中读取）"""
    return os.environ.get("COOKIE") or secret.Cookie

def get_score():
    COOKIE = get_cookie()  # 先获取当前Cookie
    XNM = os.environ.get("XNM") or secret.xnm
    XQM = os.environ.get("XQM") or secret.xqm
    data = {
        "xnm": XNM,
        "xqm": XQM,
        "queryModel.showCount": "100"
    }
    url = "https://jwglxt.qsust.edu.cn/jwglxt/cjcx/cjcx_cxXsgrcj.html?doType=query&gnmkdm=N305005"
    headers = {
        # 保持原headers不变，仅替换Cookie
        "cookie": COOKIE,
        # ... 其他headers
    }

    try:
        response = requests.post(url, headers=headers, data=data, timeout=30)
        if response.status_code == 200:
            print("教务系统状态码:", response.status_code)
            return response.json()
        else:
            # 状态码异常，认为Cookie失效，重新获取Cookie并重试
            print(f"请求失败（状态码{response.status_code}），尝试更新Cookie...")
            COOKIE = get_cookie()  # 重新获取Cookie（需确保此时环境变量/secret已更新）
            headers["cookie"] = COOKIE
            # 重试请求
            response = requests.post(url, headers=headers, data=data, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Cookie更新后仍请求失败，状态码{response.status_code}")
    except Exception as e:
        print(f"请求异常（可能Cookie失效）: {e}")
        # 异常时也尝试更新Cookie并重试（可选）
        COOKIE = get_cookie()
        headers["cookie"] = COOKIE
        response = requests.post(url, headers=headers, data=data, timeout=30)
        return response.json()
