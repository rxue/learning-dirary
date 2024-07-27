# REST API
## Access token for sending REST API request to github
references:
* https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#create-a-repository-for-the-authenticated-user
* https://medium.com/@shivapatel1102001/how-to-generate-bearer-token-in-github-3d2acadaf543
### Use Case: Create a githut repository through *terminal* command line on my local PC
#### Actions:
**Prerequisites**
The REST API request needs sender to have a *bearer token*. In case sender doesnot have an access token, go to *Settings* > *Developer settings* > *Personal access tokens* to generate the token

send REST API request to create the new repository in github

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <token_placeholder>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user/repos \
  -d '{"name":"dictionary-ci-cd","description":"CI/CD pipelines for dictionary project","homepage":"https://github.com","private":false,"is_template":true}'
```
then cd to the local directory, where you consider as the root of the remote repository and execute the following commands in sequence

```
git init
git add .
git commit -m "message"
git branch -m main
git remote add origin git@github.com:rxue/dictionary-jpa.git 
git push --set-upstream origin main
```
NOTE that the last statement push added files directly to remote origin
