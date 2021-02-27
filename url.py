from urllib import request

response = request.urlopen('http://sansat.net:25461/get.php?username=02023095082495&password=QUfJsvIiu1TDyDC&type=m3u_plus&output=mpegts')
for line in response:
    print(line.decode('utf-8').rstrip())