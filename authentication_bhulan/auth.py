import requests
import os
import time
username='15075028'
password='password'
http_url='http://hotstar.com/'
pptp_vpn='Mumbai AWS'
pptp_user='user_password'
pptp_pass=''
vpn=bool(int(input('Want to start VPN (0/1) : ')))

while True:
	try:
		requests.get('http://192.168.249.1:1000/keepalive?060e0c0502050901')
		requests.get('http://192.168.249.1:1000/keepalive?03030c0f040c084c')
	except:
		print('Check You have ping with 192.168.249.1')
		try:
			html=requests.get(http_url)
		except:
			print('Check Network Connection ...')
			time.sleep(1)
			continue
		if 'fgtauth' in html.url:
			print('Login in Process ...')
			print(html.url)
			requests.post(html.url,data={'4Tredir':http_url,'magic':html.url.split('?')[1],'username':username,'password':password})
			# html=requests.get(http_url)
			# requests.post(html.url,data={'4Tredir':http_url,'magic':html.url.split('?')[1],'answer':'1'})
			if vpn:
				os.system('rasdial "'+pptp_vpn+'" "'+pptp_user+'" "'+pptp_pass+'"')
	print('Session is Active!')
	time.sleep(100)
