## Group + Tasks

### Raj Kane

  * Developed code to upload and download files from S3 input and output buckets.
  
  * Developed code to load and retrieve the student data to DynamoDB.
  
  * Edited the Dockerfile to include the S3 and DDB code modules.
  
  * Performed local container testing.
  
  * Developed the function handler code to frame and classify MP4 videos.
  
  * Wrote code to parse the S3 event trigger.
  
  * Wrote README documentation. 


### Trey Manuszak

  * Setup of the S3 input and output buckets.
  
  * Managed the container hosting to ECR.
  
  * Management of the AWS Lambda creation from the container image.
  
  * Development of access permissions for the Lambda function.
  
  * Setup the trigger between the S3 input bucket and the Lambda function.
  
  * Performed production level testing and evaluation of Lambda function configuration.


## Testing 

The `.env` file should have the following form, with no quotation marks.

```
INPUT_BUCKET=<input bucket name>
OUTPUT_BUCKET=<output bucket name>
AWS_ACCESS_KEY=<access key>
AWS_SECRET_KEY=<secret key>
```

If not already done, preload the `student_data.json` data into DynamoDB.

```$ python src/ddb.py```

### Production testing

*TODO*

### Local testing

Build and run the docker image.

```$ docker build -t <tag> ./ && docker run --env-file .env -p 8080:8080 <tag>:latest```

From another shell, send a POST have the handler run.

```$ curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"Records": [{"s3": {"object": {"key":"test_0.mp4"}}}]}'```
