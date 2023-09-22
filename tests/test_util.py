import trackingmore

from trackingmore.util import get_api_key

def test_get_key():
    api_key = '12345678'
    trackingmore.api_key = api_key
    assert api_key == get_api_key()