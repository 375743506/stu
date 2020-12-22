"""
author:skr
datetime:2020/12/22 17:56
reversion:1.0
"""

import requests, json

for page in range(1, 5):
    url = f"https://www.douyu.com/gapi/rkc/directory/mixList/2_1008/{page}"

    res = requests.get(url).content.decode()

    data = json.loads(res)
    # print(data["data"]["rl"])
    for item in data["data"]["rl"]:
        # print(item)
        print(item["rid"], item["rn"], item["nn"])
        print("------------------" * 10)
