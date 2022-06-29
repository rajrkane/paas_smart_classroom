## DynamoDB

The `json` data is already loaded into the table `student_data` for clouderson. We don't need to handle preloading here.

## .env

The `.env` should look like this, with no quotation marks.

```
AWS_ACCESS_KEY=<access key>
AWS_SECRET_KEY=<secret key>
```

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

Check for the corresponding `test_0.txt` file in the output bucket with corresponding text as:

```
president_trump
physics
junior
```