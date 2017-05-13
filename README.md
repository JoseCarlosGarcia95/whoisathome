# whoisathome
Check who is connected in your wifi, and report any change through telegram API

# installation
- Install python-nmap: sudo pip install python-nmap
- Configure.

# run
- run as sudo 'sudo ./whoisathome.py'

# cron example
'* * * * * sudo /usr/bin/python2.7 /home/pi/whoisathome/whoisathome.py > /home/pi/crons.log 2>&1'
