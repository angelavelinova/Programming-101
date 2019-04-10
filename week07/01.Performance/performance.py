from contextlib import contextmanager
import datetime
from time import sleep
import time

@contextmanager
def performance(filename):
	try:
		start = time.time()
		yield 
	finally:
		fd=open(filename,'a+')
		fd.write("Date:")
		fd.write(str(datetime.datetime.now())+'. ')
		fd.write("Execution time:")
		end = time.time()
		fd.write(str(end-start)+'\n')
		fd.close()

with performance('log.txt') as t:
	sleep(1)
