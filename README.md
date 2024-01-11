Remote Control for devices with RPi via php

RCPi.py: called from PHP, runs only when needed by user intervention.

In order to have the required permission:

- add the following to the sudoers (sudo visudo):
www-data ALL=(ALL) NOPASSWD:/var/www/html/RCPi/no-file/RCPi.py,/usr/bin/python3

You may be able to speed up launching the python script by compiling it first:

python3 -m compileall ./

In this case, you need to change the proper line in the index.php file.

Web versions require apache2, php, libapache2-mod-php

This is needed for apache2 to GPIO

1. `sudo usermod -a -G gpio www-data`
2. nano /etc/apache2/envvars
   Add the following to the bottom of the file:
   `export WIRINGPI_GPIOMEM=1`
3. `sudo /etc/init.d/apache2 restart`
