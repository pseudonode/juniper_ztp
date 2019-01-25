maclist = []
index = 0

with open('lab_csv.csv') as csv:
    csvcontent = csv.read()
    csvsplit = csvcontent.split('\n')
    csvsplit = csvsplit[:-1]
    for switch in csvsplit:
        switch = switch.split(',')
        maclist.append(switch[2].lower())

# print('The MAC address list in lower case format is:')
# print(maclist)
# print('')

# Convert items inside mac list to hex and add + 1 to obtain Juniper EM0 MAC address
hexlist = []
for mac in maclist:
    mac = int(mac, 16)
    newint = mac
    ztpmac = hex(newint + 1) [2:]
    hexlist.append(ztpmac)

# print('The MAC address list with ZTP MAC format is:')
# print(hexlist)
# print('')

ztplist = []
for mac in hexlist:
    mac = ':'.join(a+b for a,b in zip(mac[::2], mac[1::2]))
    ztplist.append(mac)

print('The final MAC address list with ZTP MAC format and colon notation is:')
print(ztplist)
print('')

with open('rendered_csv.csv','w') as csv:
    for mac in ztplist:
        csv.write(mac + '\n')
