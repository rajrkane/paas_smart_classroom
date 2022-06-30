"""ddb.py: Defines DDB module for interacting with DynamoDB table."""

from boto3 import resource as boto3_resource
from os import getenv, listdir
from dotenv import load_dotenv
import json

class DDB:

	def __init__(self):
		load_dotenv()
		self.access_key = getenv("AWS_ACCESS_KEY")
		self.secret_key = getenv("AWS_SECRET_KEY")
		self.resource = boto3_resource(
			"dynamodb",
			region_name="us-east-1",
			aws_access_key_id=self.access_key,
			aws_secret_access_key=self.secret_key
		)
		self.table = self.resource.Table("student_data")

	# Function only needs to be called one time when preloading data
	def load_data(self, filename):
		f = open(filename)
		request_items = json.loads(f.read())
		with self.table.batch_writer() as batch:
			for item in request_items:
				batch.put_item(Item=item)

def main():
	ddb = DDB()
	ddb.load_data("student_data.json")

if __name__=="__main__":
	main()