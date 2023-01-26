# File System
## `/usr/local/bin`
### Relevant Problem
When working with MacBook, I used *Homebrew* to install *Maven* and thus the `mvn` was installed to `/opt/homebrew/bin`. As a result, I was not able to directly `mvn` in terminal since the `mvn` is not in `/usr/bin`. In order to be able to `mvn` directly in terminal I tried to make a *symbolic link* in `/usr/bin`, but *MacOS* does not accept adding anything to `/usr/bin` through terminal.

In the case above, `/usr/local/bin` comes into play
