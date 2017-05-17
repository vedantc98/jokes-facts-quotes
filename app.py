from flask import Flask
from flask import request

from responses import makeWebhookResponse
from responses import makeJSON

import os

app=Flask(__name__)

@app.route("/", methods=['POST'])
def apiai_post_handler():
	req=request.get_json(silent=True, force=True)

	res=makeWebhookResponse(req)

	res=makeJSON(res)		

	return res

if __name__=='__main__':
	port = int(os.getenv('PORT', 5000))

	print "Starting app on port %d" % port

	app.run(debug=True, port=port, host='0.0.0.0')
