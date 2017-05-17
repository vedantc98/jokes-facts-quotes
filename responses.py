import json

from flask import make_response
from flask import request

import jokes

def makeWebhookResponse(req):
	try:
		req_result=req.get("result")
	except:
		return {"lol":"lol"}

	try:
		req_result_action=req_result.get("action")
	except:
		return {"lol2":"lol2"}

	if not req_result_action. strip()=="get_joke":
		return {}
	
	#get_joke is supposed to return a tuple containing (joke, source)
	payload, source=jokes.get_joke()

	speech=payload
	displayText=payload
	
	contextOut=["told_joke"]

	return {
		"speech":speech,
		"displayText":displayText,
		"contextOut":contextOut,
		"source":source
		}

def makeJSON(res):

	res=json.dumps(res, indent=4)
	r=make_response(res)

	r.headers['Content-Type']='application/json'

	return r
