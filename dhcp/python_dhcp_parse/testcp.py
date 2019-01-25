maclist = []
index = 0

with open('lab_csv.csv') as csv:
    csvcontent = csv.read()
    print(csvcontent)
    csvsplit = csvcontent.split('\n')
    print(csvsplit)
    for switch in csvsplit:
        switch = switch.split(',')
        print(switch)
#        maclist.append(switch[2].lower())

print('The MAC address list in lower case format is:')
print(maclist)
print('')
