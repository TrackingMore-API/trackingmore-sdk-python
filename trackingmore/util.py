import trackingmore

from .exception import TrackingMoreException

from .const import ErrEmptyAPIKey

def get_api_key():
    '''Get TrackingMore API key'''
    if trackingmore.api_key is not None and trackingmore.api_key != '':
        return trackingmore.api_key
    else:
        raise TrackingMoreException(ErrEmptyAPIKey)

def build_query(params):
    kv_pairs = [f'{key}={value}' for key, value in params.items()]

    result = '&'.join(kv_pairs)

    return result

def is_empty(value):
    if value is None:
        return True
    if isinstance(value, (str, list, tuple, dict)):
        return not bool(value)
    return False