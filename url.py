from urllib import request as urlrequest

proxy_host = '116.197.131.19:8080'    # host and port of your proxy
url = 'http://sansat.net:25461/02023095082495/QUfJsvIiu1TDyDC/14991'

req = urlrequest.Request(url)
req.set_proxy(proxy_host, 'http')

response = urlrequest.urlopen(req)
print(response.read().decode('utf-8'))