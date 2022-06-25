cc project: the re-up

## Docker

Run following commands to use docker as non-root user.

```
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
$ docker run hello-world
```

If `hello-world` didn't work, might need to `reboot`.

Build docker image (might be stuck for some time on `setup.py` stage). Rebuild necessary on change.

```docker build -t <tag> ./```

Check images and verify it's there.

```docker images```

Run the image.

```docker run -p 8080:8080 <tag>:latest```

From another shell, send a POST to have the lambda function run.

```curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d "{}"```
