# Login to ECR
Official Doc: https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html 
## Problem: command `aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/y4p2f1b8` encounters error
```
Unable to locate credentials. You can configure credentials by running "aws configure".

Error: Cannot perform an interactive login from a non TTY device

```
## Solution: https://stackoverflow.com/questions/60583847/aws-ecr-saying-cannot-perform-an-interactive-login-from-a-non-tty-device-after

