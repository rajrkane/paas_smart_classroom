"""s3.py: Defines S3 module for uploading input videos and receiving labels."""

from boto3 import client as boto3_client
from os import getenv, listdir
from dotenv import load_dotenv

class S3:

	def __init__(self):
		load_dotenv()
		
		self.input_bucket = getenv("S3_INPUT")
		self.output_bucket = getenv("S3_OUTPUT") 
		self.region = getenv("REGION")
		self.access_key = getenv("AWS_ACCESS_KEY")
		self.secret_key = getenv("AWS_SECRET_KEY")
		self.client = boto3_client(
			"s3",
			region_name=self.region,
			aws_access_key_id=self.access_key,
			aws_secret_access_key=self.secret_key
		)
		self.results = {"results": []}

	def clear_input_bucket(self):
		list_obj = self.client.list_objects_v2(Bucket=self.input_bucket)
		try:
			for item in list_obj["Contents"]:
				self.client.delete_object(Bucket=self.input_bucket, Key=item["Key"])
		except:
			print("Nothing to clear in input bucket.")

	def clear_output_bucket(self):
		list_obj = self.client.list_objects_v2(Bucket=self.output_bucket)
		try:
			for item in list_obj["Contents"]:
				self.cleint.delete_object(Bucket=self.output_bucket, Key=item["Key"])
		except:
			print("Nothing to clear in output bucket.")

	def upload_to_input_bucket(self, path, name):
		self.client.upload_file(path + name, self.input_bucket, name)

	def upload_files(self, test_dir):
		# test_dir is test_case_1 or test_case_2
		test_path = "tests/" + test_dir + "/"

		for filename in listdir(test_path):
			if filename.endswith(".mp4") or filename.endswith(".MP4"):
				print(f"Uploading {str(filename)} to input bucket.")
				self.upload_to_input_bucket(test_path, filename)
