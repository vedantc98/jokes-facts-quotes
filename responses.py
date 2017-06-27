import json
import facts
import jokes
import quotes

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

	if req_result_action.strip()=="get_joke":
		payload, source=jokes.get_joke()
		speech=payload
		displayText=payload
		
		contextOut=[{"name":"told_joke", "lifespan": 2, "parameters":{}}]
		return {
			"speech":speech,
			"displayText":displayText,
		#	"contextOut":contextOut,
			"source":source
			}

	if req_result_action.strip()=="get_fact":
		payload, source=facts.get_fact()
		speech=payload
		displayText=payload

		contextOut=[{"name":"told_fact", "lifespan": 2, "parameters":{}}]
		return {
			"speech":speech,
			"displayText":displayText,
		#	"contextOut":contextOut,
			"source":source
			}
	if req_result_action.strip()=="get_quote":
		payload, source=quotes.get_quote()
		speech=payload
		displayText=payload

		contextOut=[{"name":"told_quote", "lifespan": 2, "parameters":{}}]
		return {
			"speech":speech,
			"displayText":displayText,
		#	"contextOut":contextOut,
			"source":source
			}
