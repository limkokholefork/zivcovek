import os
import requests
import re

print('starting script')

#channel = "https://www.youtube.com/channel/UCFc7sfkcyKFnHL4J1V8qutQ" #Miran Rubin
channel = "https://www.youtube.com/channel/UCVorSI0xG5EHrHdmB31V3mA" #Serbian Surfer

html = requests.get(channel + "/videos").text
info = re.search('(?<={"label":").*?(?="})', html).group()
url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
print(url)
print(info)

url_log = open("logs/uploaded.log", "r")
url_old = url_log.readline()

if url != url_old:
	exec(open('ytdownloader.py').read())
	exec(open('ytuploader.py').read())
	exec(open('filemove.py').read())

	url_log = open("logs/uploaded.log", "a")
	url_log.truncate(0)
	last_video_log = url_log.write(url)
else:
	print('No new upload')
