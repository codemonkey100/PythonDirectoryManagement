def main():
	
def move(input,output):
	"""
	move file from inport directory to output directory
	wrapper for shutil's move function
	
	"""
	try
		shutil.move(input,output)
		print("File moved successfully")
	except exception shutilError
		print("Error has occurred file not moved")
	
	
	
main()