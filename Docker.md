you already know about images, and containers, so we'll discuss commands only

to run an image and make a container do:

```bash

docker run image
docker run hello-world

```

to download an image do:


```bash

docker pull image
docker pull busy-box

```

to know the images you have run:


```bash

docker images

```

to know the containers you have run:

```bash

docker ps # shows active only
docker ps -a # shows all

```

and generally you should delete them afterwards by doing this:

```bash

docker prune
docker rm image_hash
docker rm $(docker ps -a -q -f status=exited)

```

or you could make them be autodeleted:

```bash

docker run image --rm

```

to run the container and not be bound be it (attached) use this to make it detached:

```bash

docker run -it image # attached
docker run -d image # detached

```

and you can (and should) give it a name:

```bash

docker run -d image --name cont
docker stop cont # we use the name to stop the container

```

base image is standalone, child image builds on base images

to create an image, we make a dockerfile, and write the next:

```dockerfile

# Select the base image
FROM python:3.14 

# Set the working directory for the container
WORKDIR /usr/src/app 

# Copy all the files to the container
COPY . . 

# This one is clear
RUN pip install --no-cache -r requirements.txt 

# If you need a port to run the container on (like a website)
# which is where docker is mostly used, do:
EXPOSE 3940 

# run the command
CMD ["python", "./app.py"]

```

btw `./` as in `cd ./x`

You can specify `CMD` instructions using [shell or exec forms](https://docs.docker.com/reference/dockerfile#shell-and-exec-form):
- `CMD ["executable","param1","param2"]` (exec form)
- `CMD ["param1","param2"]` (exec form, as default parameters to `ENTRYPOINT`)
- `CMD command param1 param2` (shell form)

and then to build it you'd do:

```bash

docker build -t myContainer .

```


to pass args when running a docker do:

```bash

docker run myContainer arg1 arg2

```

but you'd have to change the exec instruction of `CMD` to :

```dockerfile

ENTRYPOINT ["python", "./app.py"]

```



BTW there's something called `.dockderignore` which is for the `COPY . .` to ignore



