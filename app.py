from flask import Flask
from flask import make_request
from flask import request

import os
import json

app=Flask(__name__)

@app.route('\', methods=['POST'])

def apiai_post_handler():
	return {}

if __name__=='__main__':
	port = int(os.getenv('PORT', 5000))

	print "Starting app on port %d" % port

	app.run(debug=True, port=port, host='0.0.0.0')
