#!/bin/sh
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
	echo "$1"
    exec /usr/bin/aws-lambda-rie /usr/local/bin/python -m awslambdaric $1
else
    exec /usr/local/bin/python -m awslambdaric $1
fi
