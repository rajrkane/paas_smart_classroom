from src.s3 import S3
from src.ddb import DDB
import pickle
from os import getenv, listdir, path, mkdir
from dotenv import load_dotenv

def open_encoding(filename):
	f = open(filename, "rb")
	data = pickle.load(f)
	f.close()
	return data

def build_model():
	pass

# TODO: listen to bucket event
def face_recognition_handler(event, context):
	print("Event:")
	print(event)
	print("Context:")
	print(context)
	print("-----------")

	# Parse event
	mp4_name = event['key']

	# Get object from input bucket
	s3 = S3()
	try:
		obj = s3.client.get_object(Bucket=s3.input_bucket, Key=mp4_name)
		print("Got response.\n", obj)
	except Exception as e:
		print(f"Could not get object {key} from bucket {s3.input_bucket}.") 
		raise e 

	# Download the object as a file
	file_dir = "/tmp/input/"
	if path.isdir(file_dir) is False:
		mkdir(file_dir)

	file_path = file_dir + mp4_name
	
	try:
		s3.client.download_file(
			Bucket=s3.input_bucket,
			Key=mp4_name,
			Filename=file_path
		)
		print(f"Downloaded object to {file_path}.")
	except Exception as e:
		print(f"Could not download to {file_path}.")
		print(e)
		raise e

	# Extract frame from video

	# Determine which face matches extracted image

	# Get matching record from dynamodb

	# Handle result


# def main():

	# s3 = S3()
	# s3.clear_input_bucket()
	# s3.clear_output_bucket()
	# print("Running Test Case 1")
	# s3.upload_files("test_case_1")
	# print("Running Test Case 2")
	# s3.upload_files("test_case_2")

# if __name__=="__main__":
# 	main()