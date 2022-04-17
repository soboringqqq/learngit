import requests
from bili_api_get import Bili_API

info = []

while True:
	
	my_API = Bili_API()
	info = my_API.QR_code()
	data = info[1]

	if str(info[1]) == '-4':
		print('\nKey corret. Please scan the QR code\n')
	if str(info[1]) == '-5':
		print('\nWaiting for confirmation\n')
	
	
	quit = "\nPress q to quit \ Press any key to retry:"
	q_flag = input(quit)
	if q_flag == 'q':
		break
	
		
	
