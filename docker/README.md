[What’s the difference between up, run, and start?](https://docs.docker.com/compose/faq/)

### 20211226: How to get the IP address of a Docker Container instance
Reference: https://stackoverflow.com/questions/17157721/how-to-get-a-docker-containers-ip-address-from-the-host
Solution: `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container service name>`
