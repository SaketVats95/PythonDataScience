import os,zipfile
#dir_name = 'D:\\abc'

def RemoveAllZipFile(list_zip):
	for file_full_name in list_zip:
		os.remove(file_full_name)
		print(file_full_name," file deleted as the unzipping completed")


dir_name=input("Enter the Directory Name::::")
dir_name=dir_name.replace('\\','\\')
extension = ".zip"
list_of_all_zip=[]
os.chdir(dir_name) # change directory from working dir to dir with files
try:
	for path,dir_list,file_list in os.walk(dir_name): # loop through items in dir
		for file_name in file_list:
			if file_name.endswith(extension): # check for ".zip" extension
				file_name_path = os.path.join(path,file_name) # get full path of files
				print(file_name_path, " file unzipping started")
				zip_ref = zipfile.ZipFile(file_name_path) # create zipfile object
				newDirName=file_name_path.replace(".zip","")

				os.mkdir(newDirName)
				zip_ref.extractall(newDirName) # extract file to dir
				#os.listdir(newDirName).__contains__()
				list_of_all_zip.append(file_name_path)
				zip_ref.close() # close file
				print(file_name_path, " file unzipping completed")

except Exception as e:
	if hasattr(e,'message'):
		print(e.message)
	else:
		print(e)


NeedToDelete=input("Enter [Y/N] if you want to delete all zip files:")
if NeedToDelete.lower()=="y":
	RemoveAllZipFile(list_of_all_zip)