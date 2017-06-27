#scrapes jokes from website www.randomjokegenerator.com
import mechanize
from bs4 import BeautifulSoup
import sys

sys.stdout=open("joke_file.py", "a")

TIMES=1000
url="http://www.randomjokegenerator.com/PrintableJokeSheet.php"

br=mechanize.Browser()
br.set_handle_robots(False)
r=br.open(url)

jokes=[]

for a0 in xrange(TIMES):
	br.select_form("test")
	r=br.submit()
	html=r.read()
	soup=BeautifulSoup(html)
	textarea=soup.textarea.text

	textarea=textarea.replace("RandomJokeGenerator.com", "")

	for i in range(1, 11):
		textarea=textarea.replace("%d - "%(i), "")

	textarea=textarea.strip()
	jokes_raw=textarea.split("\n")

	for joke in jokes_raw:
		if len(joke)>5:
			jokes.append(joke)

print jokes