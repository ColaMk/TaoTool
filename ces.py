import requests

headers = {
    'authority': 'cas.paas.zufedfc.edu.cn',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://cas.paas.zufedfc.edu.cn',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://cas.paas.zufedfc.edu.cn/cas/login?service=http%3a%2f%2fyqsb.zufedfc.edu.cn%2fselfreport%2fLoginSSO_SW.aspx%3ftargetUrl%3d%7bbase64%7daHR0cDovL3lxc2IuenVmZWRmYy5lZHUuY24vc2VsZnJlcG9ydC9EZWZhdWx0LmFzcHg%3d',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'SESSION=3b4312fe-1a13-4659-af34-eeeed710121e; Hm_lvt_d605d8df6bf5ca8a54fe078683196518=1641712943,1641739176; Hm_lpvt_d605d8df6bf5ca8a54fe078683196518=1641739176',
}

params = (
    ('service', 'http://yqsb.zufedfc.edu.cn/selfreport/LoginSSO_SW.aspx?targetUrl={base64}aHR0cDovL3lxc2IuenVmZWRmYy5lZHUuY24vc2VsZnJlcG9ydC9EZWZhdWx0LmFzcHg='),
)

data = {
  'username': '1720410239',
  'password': '171810',
  'captcha': '',
  'currentMenu': '1',
  'failN': '0',
  'mfaState': '',
  'execution': 'e1s1',
  '_eventId': 'submit',
  'geolocation': '',
  'submit': 'Login1'
}

response = requests.post('https://cas.paas.zufedfc.edu.cn/cas/login', headers=headers, params=params, data=data)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://cas.paas.zufedfc.edu.cn/cas/login?service=http%3a%2f%2fyqsb.zufedfc.edu.cn%2fselfreport%2fLoginSSO_SW.aspx%3ftargetUrl%3d%7bbase64%7daHR0cDovL3lxc2IuenVmZWRmYy5lZHUuY24vc2VsZnJlcG9ydC9EZWZhdWx0LmFzcHg%3d', headers=headers, data=data)