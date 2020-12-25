log = open('NPST/log.csv', 'r', encoding='utf-16').readlines()
for line in log:
	name = line.split(';')[1].split(';')[0]
	if name.split('+')[0] not in name.split('+')[1]:
		print(f'{name.split("+")[0]} - PST{{{line.split("%7B")[1].split("%7D")[0]}}}')