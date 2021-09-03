from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob

GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = '/home/vladimir/scripts/zivcovek/resources/settings.yaml'

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

for file1 in glob.glob("videos/*.*"):
	file_title = file1.replace("videos/","")
	file_upload = drive.CreateFile({'title': file_title,'parents': [{'id':'1O_cZPBhRZEupIC9QFSH13Jii6m0KQZp8'}]})
	# Read file and set it as a content of this instance.
	file_upload.SetContentFile(file1)  #path
	file_upload.Upload() # Upload the file.
	print('title: %s, mimeType: %s' % (file_upload['title'], file_upload['mimeType']))
	# title: cat.png, mimeType: image/png
