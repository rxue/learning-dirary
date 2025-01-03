# How to Install Azuere CLI in MacBook with `brew`
brew update && brew install azure-cli
# `az`
## `az login`
`az login` command will open a new tab in a broswer to try to force user to login to the Azure Cloud portal. The username is an email address ended with `.biz`, so note that it is different from the `.online` user e.g. for *OneDrive*

## `az acr`
### list all repositories of one registry
`az acr repository list --name <RegistryName>`
### list all images of a repository
`az acr repository show-tags --name registryname --repository reponame`
