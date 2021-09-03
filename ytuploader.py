from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import glob
import re

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

CLIENT_SECRET_FILE = '/home/vladimir/scripts/zivcovek/client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

title = 'miran rubin - test'

for file in sorted(glob.glob("videos/*.mp4"), key=numericalSort):
    if not file:
        break
    print('')
    print('File: ' + file)

    video_title = file.replace("videos/", "")
    video_title = video_title.replace(".mp4", "")
    video_title = video_title.replace(";", ":")
    #video_title = video_title[4:]

    video_description =  "⭐️ Kupite mi kafu :)\nMoje ime je Vladimir, i održavam kanal *Živ Čovek*.  Održavanje kanala možete pomoći, ukoliko želite, jednom virtuelnom kafom:\n➲Virtuelna kafa: https://www.buymeacoffee.com/vladimirpl\nOstali načini:\n➲ PayPal: vpopovic003@gmail.com\n➲ Tekući račun:\n160-5800100502326-44, Banca Intesa\nVladimir Popović, Kovin"


    request_body = {
        'snippet':{
            'categoryId': 19,
            'title': video_title,
            'description' : video_description,
        },
        'status': {
            'privacyStatus': 'unlisted',
        }
    }

    mediaFile = MediaFileUpload(file, chunksize=-1, resumable=True)

    response_upload = service.videos().insert(
        part = 'snippet, status',
        body = request_body,
        media_body = mediaFile
    ).execute()
print('Video Uploaded')
