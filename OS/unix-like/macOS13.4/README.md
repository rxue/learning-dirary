# FAQ
## How is *HomeBrew* installed? (20230619)
### Answer: One command found on Homebrew official site

### Note about the post action of *Home Brew* installation
Command `(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/myname/.zprofile`

This is worth the salt to learn

NOTE! all executables installed by *HomeBrew* are in `/opt/homebrew/bin` other than `usr/bin`
## Where is JDK installed
### Answer: example: `JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_331.jdk/Contents/Home`
## I installed Openjdk11 with *Homebrew* and made a symbolic link to the directoty `/Library/Java/JavaVirtualMachines` so that it is visible in the file browser. But when I tried to configure IntelliJ to use this specific JDK, the IntelliJ popped error message telling the directory is not a JDK but a JRE directory

Similar issue here: https://intellij-support.jetbrains.com/hc/en-us/community/posts/360007751379-Why-does-IntelliJ-not-accept-usr-local-opt-openjdk-installed-by-Brew-as-a-JDK-

# Shell on macOS
## Show System Information
`system_profiler`
