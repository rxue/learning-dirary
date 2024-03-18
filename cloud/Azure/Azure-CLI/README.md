# How to Install Azuere CLI in MacBook with `brew`
brew update && brew install azure-cli
# `az`
### `az acr`
## list all repositories of one registry
`az acr repository list --name <RegistryName>`
## list all images of a repository
`az acr repository show-tags --name registryname --repository reponame`
