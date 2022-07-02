# Group + Tasks

### 1. **Raj Kane**:

  * Developed code to upload and download files from S3 input and output buckets.
  
  * Developed code to load and retrieve the student data to DynamoDB.
  
  * Edited the Dockerfile to include the S3 and DDB code modules.
  
  * Performed local container testing.
  
  * Developed the function handler code to frame and classify MP4 videos.
  
  * Wrote code to parse the S3 event trigger.
  
  * Wrote README documentation. 


### 2. **Trey Manuszak**:

  * Setup of the S3 input and output buckets.
  
  * Managed the container hosting to ECR.
  
  * Management of the AWS Lambda creation from the container image.
  
  * Development of access permissions for the Lambda function.
  
  * Setup the trigger between the S3 input bucket and the Lambda function.
  
  * Performed production level testing and evaluation of Lambda function configuration.


## DynamoDB

The `json` data is already loaded into the table `student_data` for clouderson. We don't need to handle preloading here.

## .env

The `.env` should look like this, with no quotation marks.

```
INPUT_BUCKET=<input bucket name>
OUTPUT_BUCKET=<output bucket name>
AWS_ACCESS_KEY=<access key>
AWS_SECRET_KEY=<secret key>
```

## Asset Names

S3 Input Bucket: `cse546-paas-input`

S3 Output Bucket: `cse546-paas-output`

## Docker

Run following commands to use docker as non-root user.

```
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
$ docker run hello-world
```

If `hello-world` didn't work, might need to `reboot`.

Build docker image (might be stuck for some time on `setup.py` stage). Then run it.

```docker build -t <tag> ./ && docker run --env-file .env -p 8080:8080 <tag>:latest```

Rebuild is necessary on update.

## Handler

From another shell, send a POST to have the handler run.

```curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"Records": [{"s3": {"object": {"key":"test_0.mp4"}}}]}'```

Check for the corresponding `test_0` CSV file in the output bucket with body:

`president_trump, physics, junior`
