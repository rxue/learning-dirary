# [Database and service containers](https://support.atlassian.com/bitbucket-cloud/docs/databases-and-service-containers/)

The way for pipeline to use container is a bit different from how we use Docker container locally. The containers should be defined as `services` in the `definitions` section of `bitbucket-pipeline.yml`

## My wrong trial
Originally I thought the pipeline supports `docker` by default so that using `docker` command in the `script` section of a `step` in `bitbucket-pipeline.yml` should work like in the github. So I tried the following steps:

1. add a `docker run` command to the `- script` section
2. after `docker run` add `mvn clean verify`, which try to access the started Docker container

Result: not work => I tried to add `docker` installation script before `docker run` => still not work => Googled and found https://support.atlassian.com/bitbucket-cloud/docs/run-docker-commands-in-bitbucket-pipelines/ then tried the following steps:

1. add `docker` to the `services` section of a `- step`
2. add `docker run` command to start a docker container
3. after `docker run` add `mvn clean verify`, which try to access the started Docker container

Result: not work when trying to access the started docker container at least with `localhost` and another problem is the *port mapping* does not work

=> eventually found https://support.atlassian.com/bitbucket-cloud/docs/databases-and-service-containers/ and works as expected. But still I am not able to  *port mapping*


