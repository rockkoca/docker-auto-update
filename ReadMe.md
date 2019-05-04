#Purpose
Automatically upgrade container image and restart container

#Usage
```bash
docker run -d \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.docker:/root/.docker \
    rockkoca/docker-auto-update image_name
```

#Thanks
https://github.com/lavie/runlike

The program uses runlike to get the container run commands in order to relaunch the container with upgraded image. 