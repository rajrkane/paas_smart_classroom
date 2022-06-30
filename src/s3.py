"""s3.py: Defines S3 module for uploading input videos and receiving labels."""

from boto3 import client as boto3_client
from os import getenv, listdir
from dotenv import load_dotenv

class S3:

	def __init__(self):
		load_dotenv()
		
		self.input_bucket = getenv("INPUT_BUCKET")
		self.output_bucket = getenv("OUTPUT_BUCKET") 
		self.access_key = getenv("AWS_ACCESS_KEY")
		self.secret_key = getenv("AWS_SECRET_KEY")
		self.client = boto3_client(
			"s3",
			region_name="us-east-1",
			aws_access_key_id=self.access_key,
			aws_secret_access_key=self.secret_key
		)

	def upload_to_output(self, fileObj, name):
		self.client.upload_fileobj(fileObj, self.output_bucket, name)
