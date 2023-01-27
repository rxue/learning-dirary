# FAQ
## Which is *HomeBrew* installed?
### Answer: [`/opt/homebrew`](https://earthly.dev/blog/homebrew-on-m1/)
Moreover, all executables installed by *HomeBrew* are in `/opt/homebrew/bin` other than `usr/bin`
## Where is JDK installed
### Answer: example: `JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_331.jdk/Contents/Home`
## I installed Openjdk11 with *Homebrew* and made a symbolic link to the directoty `/Library/Java/JavaVirtualMachines` so that it is visible in the file browser. But when I tried to configure IntelliJ to use this specific JDK, the IntelliJ popped error message telling the directory is not a JDK but a JRE directory

Similar issue here: https://intellij-support.jetbrains.com/hc/en-us/community/posts/360007751379-Why-does-IntelliJ-not-accept-usr-local-opt-openjdk-installed-by-Brew-as-a-JDK-
