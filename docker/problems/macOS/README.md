# 20230814 When starting a MariaDB container with command `docker build`, got error

    2023-08-14 16:22:09+00:00 [Note] [Entrypoint]: Initializing database files
    2023-08-14 16:22:09 0 [ERROR] mariadbd: Error writing file './ddl_recovery.log' (Errcode: 28 "No space left on device")
    2023-08-14 16:22:09 0 [ERROR] Aborting
    2023-08-14 16:22:09 0 [ERROR] mariadbd: Error on close of '(null)' (Errcode: 9 "Bad file descriptor")

    Installation of system tables failed!  Examine the logs in
    /var/lib/mysql/ for more information.

    The problem could be conflicting information in an external
    my.cnf files. You can ignore these by doing:

Answer: `docker system prune` to clean all stopped containers and dangling images

Reference: https://stackoverflow.com/questions/30604846/docker-error-no-space-left-on-device


