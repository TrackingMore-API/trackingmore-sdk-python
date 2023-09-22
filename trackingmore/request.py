import json

import requests

from .util import get_api_key,build_query

from .exception import TrackingMoreException

from .response import process_response

apiBaseUrl = 'api.trackingmore.com'

apiPort = 443

apiVersion = 'v4'

timeout = 10

headers = {}

proxy = 'http://192.168.2.198:7890'

def get_request_url(path):
    pact = 'https' if apiPort == 443 else 'http'
    url = pact+'://'+apiBaseUrl+'/'+apiVersion+'/'+path
    return url

def get_request_header(apiKey):
    headers['Accept'] = 'application/json'
    headers['Content-Type'] = 'application/json'
    headers['Tracking-Api-Key'] = apiKey
    return headers

def make_request( method='GET', path ='', params=None):
    try:
        url = get_request_url(path)

        headers = get_request_header(get_api_key())

        verify = False

        if proxy:
            proxies = {
                'http': proxy,
                'https': proxy,
            }

        json_data = None
        if params is not None:
            if method == 'GET':
                url = url + '?' +build_query(params)
            else:
                json_data = json.dumps(params)

        if method == 'GET':
            response = requests.get(url, headers=headers, timeout=timeout, verify=verify, proxies=proxies)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json_data, timeout=timeout, verify=verify, proxies=proxies)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=json_data, timeout=timeout, verify=verify, proxies=proxies)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers, timeout=timeout, verify=verify, proxies=proxies)
        else:
            raise TrackingMoreException('Unsupported HTTP method: {}'.format(method))

        return process_response(response)

    except requests.exceptions.RequestException as e:
        print('Error making request:', e)
        return None