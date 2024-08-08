[What’s the difference between up, run, and start?](https://docs.docker.com/compose/faq/)

# Core Rationale of Docker
Docker *registry* is remote and is composed of many *repositories*. One repository contains multiple images,each of which has a unique *tag*. When `pull` an image, if a tag is not given, the default is `latest`

Reference: https://www.youtube.com/watch?v=8hCQ-sxfBIA

## Docker repositories
https://docs.docker.com/docker-hub/repos/create/#:~:text=Repositories%20let%20you%20share%20container,with%20the%20docker%20push%20command.


## layered architecture
https://www.youtube.com/watch?v=B8c1ui1hDTw&list=PLmOn9nNkQxJFX0YVLDw5EMUL-4cVzXL33&index=17

## Docker Network
Reference: `docker network` commands https://www.youtube.com/watch?v=OL5EDRkhiq4&list=PLmOn9nNkQxJFtOGw9fsoLHgtCxcki7TtK&index=67

## Docker [Repositories](https://docs.docker.com/docker-hub/repos/create/#:~:text=Repositories%20let%20you%20share%20container,through%20the%20docker%20push%20command.)
> Repositories let you share container images with your team, customers, or the Docker community at large.



### 20211226: How to get the IP address of a Docker Container instance
Reference: https://stackoverflow.com/questions/17157721/how-to-get-a-docker-containers-ip-address-from-the-host
Solution: `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container service name>`

### 20230727: don't know why my docker command disappeared in my macOS even though the docktop version exists
Solution from ChatGPT: docker's commands is originally in `/Applications/Docker.app/Contents/Resources/bin`

## Docker Image
docker image cannot be removed while a container built on base of it is running

# Docker commands
## `docker build`

## 20230924: remove all images by force
`docker rmi -f $(docker images -q)`

NOTE that remove image by force does not kill the corresponding running container

## 20240327
### list all the docker processes regardless of the status
`docker ps -a`

This can be compared with `docker ps`, which list only running container

### remove an EXITED container
`docker container rm <container-name>` or `docker rm -f <container-name>`
