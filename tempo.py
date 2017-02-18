# coding: utf-8

from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt
import ntplib
import sys

def consultaNtp():
	try:
		c = ntplib.NTPClient()
		response = c.request('a.ntp.br', version=3)
		out = response.offset
		return out

	except:
		return consultaNtp()

seg = 0
cont = 0
tt = int(sys.argv[1])
tp = int(sys.argv[2])
listaRes = list()
listaTab = list()

begin = str(datetime.now())

while seg < tt:
	sleep(tp)
	res = consultaNtp()
	listaRes.append(res)
	seg = seg + tp
	cont = cont + 1
	listaTab.append(seg)
	print "\n *********************** Consulta Ntp ***********************\n Requisitions: " + str(cont) + "\n Seconds: " + str(seg) + "\n Out: " + str(res)

print '\n\n -- Begin: ' + begin
print '\n -- Finished: ' + str(datetime.now())

plt.plot(listaTab, listaRes, '-', color = 'red')
plt.xlabel('seconds')
plt.ylabel('offset')
plt.show()
