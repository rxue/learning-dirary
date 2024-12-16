# `history`
## display history with timestamp
`history -f` : reference: https://ostechnix.com/enable-timestamp-for-history-command-in-zsh-in-linux/

or

`history -E` : reference: https://askubuntu.com/questions/391082/how-to-see-time-stamps-in-bash-history


# Operation on Port
## Display Listening Port with `netstat`
`netstat -an |grep LISTEN`
reference: ChatGPT
## I would like to know which process is listening on PORT 8080
lsof -i :8080

## `autoload` functions are in `/usr/share/zsh/5.9/functions/compinit`
reference: https://stackoverflow.com/questions/30840651/what-does-autoload-do-in-zsh

# 20240830 I would like to configure the default directory for saving the snapshot pictures
`defaults write com.apple.ScreenCapture location -string "/path/to/your/desired/directory"` - learnt from Gemini

