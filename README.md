# calculator
experiment

prerequisites (and useful stuff):

1. Enable I2C kernel support (in Pi's config menu)
- see: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

2. Install:
- sudo apt-get install -y python-smbus
- sudo apt-get install -y i2c-tools (optional, but very handy)

3. Install demo code (that we refer to):
- https://github.com/adafruit/Adafruit_Python_CharLCD 


Use as a webserver & access point
- See: http://www.instructables.com/id/Raspberry-Pi-Web-Server-Wireless-Access-Point-WAP/

Make this a low power setup (see: https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy):
- Disable HDMIO: running /usr/bin/tvservice -o (-p to re-enable). Add the line to /etc/rc.local to disable HDMI on boot.
