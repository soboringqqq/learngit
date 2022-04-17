import requests

# # Make an API call and store the response.
# url = 'https://passport.bilibili.com/web/captcha/combine?plat=6' # 人机认证
# # headers = {'Accept': 'application/vnd.github.v3+json'}
# # r = requests.get(url, headers=headers)
# r = requests.get(url)
# # print(f"Status code: {r.code}")
# print(f"Status code: {r.status_code}")

# response_dict = r.json()
# print(f"Code: {response_dict['code']}")
# print(f"Success: {response_dict['data']['result']['success']}")
# print(f"Gt: {response_dict['data']['result']['gt']}")
# print(f"Challenge: {response_dict['data']['result']['challenge']}")
# print(f"Key: {response_dict['data']['result']['key']}")

# Make an API call and store the response.
url = 'http://passport.bilibili.com/qrcode/getLoginUrl' # 二维码
# headers = {'Accept': 'application/vnd.github.v3+json'}
# r = requests.get(url, headers=headers)
r = requests.get(url)
# print(f"Status code: {r.code}")
print(f"Status code: {r.status_code}")

response_dict = r.json()
print(f"Code: {response_dict['code']}")
print(f"Status: {response_dict['status']}")
print(f"Ts: {response_dict['ts']}")
print(f"Url: {response_dict['data']['url']}")
print(f"Oauthkey: {response_dict['data']['oauthKey']}")
