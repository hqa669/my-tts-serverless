# handler.py

import json

def handler(event, context):
    """
    Runpod Serverless handler.
    Assumes 'event' is a dict containing a JSON-like payload.
    For queue-based endpoints: 'event' will likely have key 'input'.
    """
    # For example, echoing back all input
    input_data = event.get("input", {})
    result = {
        "echo": input_data
    }
    return {
        "statusCode": 200,
        "body": json.dumps(result),
    }
