import requests



# Make an API call and store the response.
url = 'http://passport.bilibili.com/qrcode/getLoginUrl' 
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

oauthkey =  response_dict['data']['oauthKey']
# print(oauthkey)

# payload = {'oauthKey': oauthkey}

url_post = 'http://passport.bilibili.com/qrcode/getLoginInfo' 
req_post = requests.post(url_post, data={'oauthKey': oauthkey})
response_dict_post = req_post.json()
print('\n')
# print(response_dict_post)
print(f"Status code: {req_post.status_code}")
print(f"Status: {response_dict_post['status']}")
print(f"Data: {response_dict_post['data']}")
print(f"Message: {response_dict_post['message']}")

if response_dict_post['data'] == -4:
	{
	print("Please scan QR code")
	}
