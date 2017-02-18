# coding: utf-8

from timeout import setInterval
import ntplib
from time import ctime
import sys

def tempo():
	print 'Acabou'


def consultaNtp():
	c = ntplib.NTPClient()
	response = c.request('a.ntp.br', version=3)
	out = response.offset
	print 'Off -> ' + str(out)

#consultaNtp()
intervalos = setInterval(tempo, 10)
inter = setInterval(consultaNtp, 1)