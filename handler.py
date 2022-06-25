from src.s3 import S3
from src.ddb import DDB
import pickle
from os import getenv, listdir
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

	# parse event
	image_name = event['key']

	# get object from input bucket
	s3 = S3()
	print(s3.input_bucket)

	try:
		response = s3.client.get_object(Bucket=s3.input_bucket, Key=image_name)
		print(response)
	except Exception as e:
		print(e) 

	# extract frame from video

	# determine which face matches extracted image

	# get matching record from dynamodb

	# handle result


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