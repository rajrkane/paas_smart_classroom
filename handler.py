from src.s3 import S3
from src.ddb import DDB
import pickle
import face_recognition
import urllib
import io
from os import system, listdir

def open_encoding(filename):
	try:
		f = open(filename, "rb")
		data = pickle.load(f)
		f.close()
		return data
	except IOError:
		print(f"Encoding file {filename} does not exist.")

def face_recognition_handler(event, context):
	# Parse event
	video_file_name = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

	# Get object from input bucket
	s3 = S3()
	try:
		obj = s3.client.get_object(Bucket=s3.input_bucket, Key=video_file_name)
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
	except Exception as e:
		print(f"Could not download to {video_file_path}.")
		print(e)
		raise e

	# Extract frame from video (starting at 001)
	system("ffmpeg -i " + str(video_file_path) + " -r 1 " + str(path) + "image-%3d.jpeg -loglevel quiet")

	# Get face from first image
	image = face_recognition.load_image_file(str(path) + "image-001.jpeg")
	unknown_encoding = face_recognition.face_encodings(image)[0]

	# Determine which face matches extracted image
	encodings = open_encoding("/home/app/encoding")
	for e in enumerate(encodings["encoding"]):
		result = face_recognition.compare_faces([e[1]], unknown_encoding)
		if result[0]:
			label = encodings['name'][e[0]]
			break

	# Get matching record from dynamodb
	ddb = DDB()
	try:
		response = ddb.table.get_item(Key={"name": label})
		print(f"Matched {video_file_name} to {response['Item']['name']}.")
	except Exception as e:
		print(f"Could not fetch information for {label} from DynamoDB.")
		print(e)
		raise(e)

	# Save result to output bucket
	item = response["Item"]
	save_name = video_file_name.split('.')[0] + ".txt"
	save_body = f"{item['name']}\n{item['major']}\n{item['year']}"
	with io.BytesIO() as f:
		f.write(save_body.encode())
		f.seek(0)
		s3.client.upload_fileobj(f, s3.output_bucket, save_name)

# def main():
	# ddb = DDB()
	# ddb.load_data("student_data.json")
	# s3 = S3()
	# s3.clear_input_bucket()
	# s3.clear_output_bucket()
	# print("Running Test Case 1")
	# s3.upload_files("test_case_1")
	# print("Running Test Case 2")
	# s3.upload_files("test_case_2")

# if __name__=="__main__":
# 	main()