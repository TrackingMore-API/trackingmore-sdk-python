import json

from .exception import TrackingMoreException

def process_response(response):
    try:
        json_content = response.json()
    except json.JSONDecodeError:
        raise TrackingMoreException('response json type conversion failed')
    return json_content