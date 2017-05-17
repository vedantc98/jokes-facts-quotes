import json

import jokes

def makeWebhookResponse(req):
	try:
		req_result=req.get("result")
	except:
		print "Lol3"
		return {"lol":"lol"}

	try:
		req_result_action=req_result.get("action")
	except:
		print "Lol2"
		return {"lol2":"lol2"}

	if not req_result_action.strip()=="get_joke":
		print "LOL1"
		return {}
	
	#get_joke is supposed to return a tuple containing (joke, source)
	payload, source=jokes.get_joke()
	speech=payload
	displayText=payload
	
	contextOut=["told_joke"]
	return {
		"speech":speech,
		"displayText":displayText,
	#	"contextOut":contextOut,
		"source":source
		}

