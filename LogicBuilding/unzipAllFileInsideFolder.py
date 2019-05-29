import os,zipfile
#dir_name = 'D:\\abc'
dir_name=input("Enter the Directory Name::::")
dir_name=dir_name.replace('\\','\\')
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files
try:
	for path,dir_list,file_list in os.walk(dir_name): # loop through items in dir
		for file_name in file_list:
			if file_name.endswith(extension): # check for ".zip" extension
				file_name_path = os.path.join(path,file_name) # get full path of files
				print(file_name_path, " file unzipping started")
				zip_ref = zipfile.ZipFile(file_name_path) # create zipfile object
				zip_ref.extractall(path) # extract file to dir
				zip_ref.close() # close file
				print(file_name_path, " file unzipping completed")
except Exception as e:
	if hasaatr(e,'message'):
		print(e.message)
	else:
		print(e)

        	#os.remove(file_name)
        	#print(file_name," file deleted as the unzipping completed")