from flask import Flask
from flask import request
from flask import make_response

from responses import makeWebhookResponse

import json
import os

app=Flask(__name__)

@app.route("/", methods=['POST'])
def apiai_post_handler():
	req=request.get_json(silent=True, force=True)

	res=makeWebhookResponse(req)

	print res

	res=json.dumps(res, indent=4)
        r=make_response(res)

        r.headers['Content-Type']='application/json'

	return r

if __name__=='__main__':
	port = int(os.getenv('PORT', 5000))

	print "Starting app on port %d" % port

	app.run(debug=True, port=port, host='0.0.0.0')
