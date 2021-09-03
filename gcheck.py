from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

#GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = '/home/vladimir/scripts/zivcovek/resources/client_secret.json'

file_list = drive.ListFile({'q': "'1O_cZPBhRZEupIC9QFSH13Jii6m0KQZp8' in parents and trashed=false"}).GetList()
#file_list = drive.ListFile({'q': "'19umdEmvDiCwd6aNbxxkL63BZYJ_mFot0' in parents and trashed=false"}).GetList()

file_title_list = []
for file1 in file_list:
	file_name = file1['title'] #exctract only title from all metadata
	file_title_list.append(file_name) #add all title to a new list
file_title_list1 = sorted(file_title_list) #sort list alphabetically

for file2 in file_title_list1: #loop for all items in the new list
	file_name1 = file2 #passes all until the last
#print(file_name1) #print only the last (last value assigned)

last_count_number = file_name1[:3]
count_number = int(last_count_number) + 1
