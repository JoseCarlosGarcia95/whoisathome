#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nmap
import os.path
import json
import urllib2
import urllib

# Configuration

known_maclist = {
    '<mac addr>' : '<name>'
}

telegram_token = '<token>'
telegram_chat_id = '<chat id>'

# Generate a list of Mac Adresses.
nma = nmap.PortScanner()
mac_list = []

for i in range(10):
    results = nma.scan(hosts='192.168.1.1-30', arguments='-sP --')

    for ip_addr in results['scan']:
        if 'mac' in results['scan'][ip_addr]['addresses'].keys():
            if results['scan'][ip_addr]['addresses']['mac'] not in mac_list:
                mac_list.append(results['scan'][ip_addr]['addresses']['mac'])

        
# Check known mac list and generate output.
            
first_run = not os.path.exists('report.json') 

if not first_run:
    report = open('report.json', 'r')

new_report = {}
1
if first_run:
    old_report = {}
else:
    old_report = json.loads(report.read())
    report.close()


output = '@ Connected devices: \n\n'

for mac_addr in mac_list:
    if mac_addr in known_maclist:
        new_report[mac_addr] = {'name' : known_maclist[mac_addr],  'known' : True}
    else:
        new_report[mac_addr] = {'name' : 'Unknown', 'known' : False}
    output += '@ ' + mac_addr + ' - ' + new_report[mac_addr]['name'] + '\n'

output += '\n\n@ News\n\n'

report_needed = False
for addr in new_report:
    if addr not in old_report.keys():
        output += '@ ' + addr + ' - ' + new_report[addr]['name'] + ' is now connected\n'
        report_needed = True

for addr in old_report:
    if addr not in new_report.keys():
        output += '@ ' + addr + ' - ' + old_report[addr]['name'] + ' is now disconnected\n'
        report_needed = True

if report_needed:
    url = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage'
    values = {'chat_id' : telegram_chat_id,
              'text' : output }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)


report = open('report.json', 'w')
report.write(json.dumps(new_report))
