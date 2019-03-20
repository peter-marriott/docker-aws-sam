from os import getenv

import json
import ptvsd

debug_mode = getenv('DEBUG')
# # Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
if debug_mode == '1':
    ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
    ptvsd.wait_for_attach()

def lambda_handler(event, context):
    dodgy_code = 1
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "api called",
            "response": dodgy_code
        }),
    }
