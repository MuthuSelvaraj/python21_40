import time
start_time = time.time()
count=60
while(count>=0):
	localtime=time.asctime(time.localtime(time.time()))
	print localtime
	time.sleep(5)
	count=count-5
endtime=time.time()-start_time
print "total  time(sec) taken to excute the above program is",endtime