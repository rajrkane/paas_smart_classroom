from src.s3 import S3
from src.ddb import DDB
import pickle
import face_recognition 
from os import system, listdir

def open_encoding(filename):
	try:
		f = open(filename, "rb")
		data = pickle.load(f)
		f.close()
		return data
	except IOError:
		print(f"Encoding file {filename} does not exist.")

def build_model():
	pass

# TODO: listen to bucket event
def face_recognition_handler(event, context):
	# print("Event:")
	# print(event)
	# print("Context:")
	# print(context)
	# print("-----------")

	# Parse event
	video_file_name = event['key']

	# Get object from input bucket
	s3 = S3()
	try:
		obj = s3.client.get_object(Bucket=s3.input_bucket, Key=video_file_name)
		# print("Got response.\n", obj)
	except Exception as e:
		print(f"Could not get object {key} from bucket {s3.input_bucket}.") 
		raise e 

	# Download the object as a file
	path = "/tmp/"
	video_file_path = path + video_file_name
	
	try:
		s3.client.download_file(
			Bucket=s3.input_bucket,
			Key=video_file_name,
			Filename=video_file_path
		)
		print(f"Downloaded object to {video_file_path}.")
	except Exception as e:
		print(f"Could not download to {video_file_path}.")
		print(e)
		raise e

	# Extract frame from video (starting at 001)
	system("ffmpeg -i " + str(video_file_path) + " -r 1 " + str(path) + "image-%3d.jpeg -loglevel quiet")

	# Get face from first image
	image = face_recognition.load_image_file(str(path) + "image-001.jpeg")
	face_locations = face_recognition.face_locations(image)

	# Determine which face matches extracted image
	encoding_file = open_encoding("/home/app/encoding")

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