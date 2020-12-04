"""Inneholder alternative løsninger"""

from datetime import date

måltall = 0
for y in range(2020, 2041):
    a = (19 * (y % 19) + 24) % 30
    b = ((2 * (y % 4)) + (4 * (y % 7)) + (6 * a) + 5) % 7
    måltall += (date(y, 3, 1) - date(1900, 1, 1)).days + (20+a+b)

print(f"PST{{{måltall}}}")


#Ikke like ryddig
"""
import datetime
# Påskeaftener: https://en.wikipedia.org/wiki/List_of_dates_for_Easter
aftener = ["2020-04-11",
           "2021-04-03",
           "2022-04-16",
           "2023-04-08",
           "2024-03-30",
           "2025-04-19",
           "2026-04-04",
           "2027-03-27",
           "2028-04-15",
           "2029-03-31",
           "2030-04-20",
           "2031-04-12",
           "2032-03-27",
           "2033-04-16",
           "2034-04-08",
           "2035-03-24",
           "2036-04-12",
           "2037-04-04",
           "2038-04-24",
           "2039-04-09",
           "2040-03-31"]

maalsum = 0
for aften in aftener:
    # MSSQL sin CONVERT(INT, <date>) gir antall dager siden 1900-01-01
    maaltall = (datetime.datetime.strptime(aften, '%Y-%m-%d') - datetime.datetime(1900,1,1)).days
    print("Påskeaften: %s -> %s" % (aften, maaltall))
    maalsum += maaltall
    
print("Sum maaltall:", maalsum)

"""

#Enda mer rotete, men kan vise metoden
"""
#!/bin/python3
#import math
from datetime import date
#import datetime

def regn(aar):
	a = aar % 19
	b = 1.0*aar // 100
	c = aar % 100
	d = 1.0*b // 4
	e = b % 4
	f = (8.0+b) // 25
	g = (1.0+b-f) // 3
	h = (19*a+b-d-g+15) % 30
	i = 1.0*c // 4
	k = aar % 4
	l = (32.0 + 2*e + 2*i -h-k) % 7
	m = (1.0*a+11*h+22*l) // 451
	year = aar-2000
	month = (h+l-7*m+114) // 31
	#if month == 2:
	#	delpa = 28
	#elif month in [1, 3, ]
	easterday = (h+l-7*m+114) % 31
	if easterday == 0:
		easterday = 31
		month -= 1
	paaskeaften = [2000+year, int(month), int(easterday)]

	return paaskeaften

def telldager(yr, m, d):
#	da = dato.split("-")
	start = date(1900, 1, 1)
	end = date(yr, m, d)
	svar = end - start
	return svar.days

def main():
	fra = int(input("Fra og med år: "))
	til = int(input("Til og med år: "))
	totaar = range(fra, til+1) #tar til og med 2040
	teller = 0
	print("Dato		|	Dager fra 1900")
	for i in totaar:
		dato = regn(i)
		yr = dato[0]
		m = dato[1]
		d = dato[2]
		print(str(yr)+"-"+str(m)+"-"+str(d)+"	|	", end="")
		dagerfra = telldager(yr, m, d)
		teller += dagerfra
		print(dagerfra)
	print("Antall dager lagt sammen:", teller)
main()
"""