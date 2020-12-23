"""
author:skr
datetime:2020/12/22 20:17
reversion:1.0
"""

import requests, re

url = "http://zjj.zhuzhou.gov.cn/fcjadpater/select/WWW_YSXK_002"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",

}

response = requests.get(url, headers=headers).content.decode()

print(response)

# re_list = re.findall('placeholder="(.*?)" />',response)
