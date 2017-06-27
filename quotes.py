import requests
import json

source_url="http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1"

def get_quote():
	r=requests.get(source_url)
	json_text=r.json()[0]

	quote=json_text['content']
	quote=quote.replace("<p>", "")
	quote=quote.replace("</p>", "")
	quote+="-"+json_text['title']

	return quote, source_url

print get_quote()
