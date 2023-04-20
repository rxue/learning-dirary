# Where to find AWS_ACCOUNT_ID

# AWS Storage
## S3 Service Architecture

### Practical Tips
#### When using aws rm to remove a directory inside s3 bucket, remember to use `--recursive` option
#### NOTE! `aws ls` is different from `ls` in *Shell* !
`aws ls` takes the suffix `/` into consideration. Assume the `bucket` is not empty:
* `aws ls s3://bucket` outputs only the name of the this `bucket`
* `aws ls s3://bucket/` outputs what is inside `bucket`

Whereas the *Shell* command `ls bucket` and `ls bucket/` have the same output
