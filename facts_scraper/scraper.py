import requests
from bs4 import BeautifulSoup
import sys

TIMES=1000

reload(sys)
sys.setdefaultencoding('UTF8')

url="http://randomfactgenerator.net/"

sys.stdout=open("facts.txt", "a")

i=0
for a0 in xrange(TIMES):
	req=requests.get(url)
	soup=BeautifulSoup(req.text, 'html.parser')
	facts=soup.findAll("div", id="z")
	for fact in facts:
		text=fact.text
		text=text.replace("Tweet", "")
		#print "Fact number %d:"%(i),
		print text
		i+=1

