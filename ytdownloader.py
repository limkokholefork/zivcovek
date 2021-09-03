from pytube import YouTube
import glob
import shutil
import requests
import re

#ask for the link from user
#link = input("Enter the link of YouTube video you want to download:  ")
#yt = YouTube(link)
#print(yt.streams.filter(progressive=True))

#channel = "https://www.youtube.com/channel/UCFc7sfkcyKFnHL4J1V8qutQ" #Miran Rubin
channel = "https://www.youtube.com/channel/UCVorSI0xG5EHrHdmB31V3mA" #Serbian Surfer

html = requests.get(channel + "/videos").text
url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
yt = YouTube(url)
#print(yt.streams.all())

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

#Starting download
print("Downloading...")

yt.streams.get_by_itag(18).download("videos/")

print("Download completed.")
