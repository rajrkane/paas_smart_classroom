from src.s3 import S3
from src.ddb import DDB
import pickle


def open_encoding(filename):
	f = open(filename, "rb")
	data = pickle.load(f)
	f.close()
	return data

# Lambda function for performing face recognition
# Create this using docker image
def face_recognition_handler(event, context):
	print("Hello world")


# def main():
	#print(open_encoding("encoding"))
	# ddb = DDB()
	# print("Loading data into DynamoDB.")
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