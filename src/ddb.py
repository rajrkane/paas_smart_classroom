"""ddb.py: Defines DDB module for preloading data into DynamoDB."""

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
			aws_access_key_id=self.access_key,
			aws_secret_access_key=self.secret_key
		)
		self.table = self.resource.Table(getenv("DYNAMO_DB"))

	def load_data(self, filename):
		f = open(filename)
		request_items = json.loads(f.read())
		with self.table.batch_writer() as batch:
			for item in request_items:
				batch.put_item(Item=item)
