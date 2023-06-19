# File System
## `/usr/local/bin`
# Linux VS macOS
... 				| Linux | macOS	| proved by command
--------------------------------|-------|-------|-------------------
case sensitive 			| YES	| **NO**| none
Terminal's default support Shell| `zsh`	| `bash`| `echo $SHELL`

### Relevant Problem
When working with MacBook, I used *Homebrew* to install *Maven* and thus the `mvn` was installed to `/opt/homebrew/bin`. As a result, I was not able to directly `mvn` in terminal since the `mvn` is not in `/usr/bin`. In order to be able to `mvn` directly in terminal I tried to make a *symbolic link* in `/usr/bin`, but *MacOS* does not accept adding anything to `/usr/bin` through terminal.

In the case above, `/usr/local/bin` comes into play

REASONING: based on ChatGPT's answer, `/usr/local/bin/` is included in the default system `$PATH`. I checked with my home Ubuntu and work MacBook. Both are like this


