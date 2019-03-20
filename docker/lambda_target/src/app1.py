import json
from flask import Flask
app = Flask(__name__)

@app.route('/<id>')
def hello_id(id):

    app.logger.info('hello id called')

    body_response = "id: {}".format(id)

    app.logger.info(body_response)

    return json.dumps({'success':True, 'body': body_response}), 200, {'ContentType':'application/json'} 
