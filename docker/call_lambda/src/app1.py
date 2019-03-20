import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def call_lambda():

    try:
        lambda_client = boto3.client('lambda',
                                  endpoint_url="http://host.docker.internal:3001",
                                  use_ssl=False,
                                  verify=False,
                                  region_name='eu-west-2',
                                  config=botocore.client.Config(signature_version=botocore.UNSIGNED,
                                                read_timeout=10,
                                                retries={'max_attempts': 0}))
        response = lambda_client.invoke(FunctionName="HelloFunction")
        lambda_response_body = response['Payload'].read()
        data = json.loads(lambda_response_body)['body']
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return json.dumps({'success':True, 'body': data}), 200, {'ContentType':'application/json'} 
