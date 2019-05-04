# Purpose
Automatically upgrade container image and restart container

# Usage

```bash
# any container's base image starts with image_name will be monitored
docker run -d \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.docker:/root/.docker \
    --name dau \
    rockkoca/docker-auto-update image_name
```

```bash
# use an empty name to monitor and upgrade all containers
docker run -d \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.docker:/root/.docker \
    --name dau \
    rockkoca/docker-auto-update ""
```

# Thanks
https://github.com/lavie/runlike

The program uses runlike to get the container run commands in order to relaunch the container with upgraded image. 