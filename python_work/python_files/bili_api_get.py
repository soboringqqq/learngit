import requests
class Bili_API():
	"""A simple QR code login API."""
	def __init__(self, oauthKey=''):
		"""Store data."""
		self.oauthKey = oauthKey
		
	
	def QR_code(self):
		"""a """
		url_login = 'http://passport.bilibili.com/qrcode/getLoginUrl'
		r_login = requests.get(url_login)
		response_dict_login = r_login.json()
		self.oauthKey = response_dict_login['data']['oauthKey']
		
		url_QR = 'http://passport.bilibili.com/qrcode/getLoginInfo' 
		req_QR = requests.post(url_QR, data={'oauthKey': self.oauthKey})
		response_dict_QR = req_QR.json()
		return response_dict_QR['status'], response_dict_QR['data']
		
		print(f"Code: {response_dict_login['code']}")
		print(f"Status: {response_dict_login['status']}")
		print(f"Ts: {response_dict_login['ts']}")
		print(f"Url: {response_dict_login['data']['url']}")
		print(f"Oauthkey: {response_dict_login['data']['oauthKey']}")
		
		print('\n')
		print(f"Status code: {req_QR.status_code}")
		print(f"Status: {response_dict_QR['status']}")
		print(f"Data: {response_dict_QR['data']}")
		print(f"Message: {response_dict_QR['message']}")
