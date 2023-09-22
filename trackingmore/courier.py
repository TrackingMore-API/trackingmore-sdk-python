
from .const import ErrMissingTrackingNumber

from .request import make_request

from .exception import TrackingMoreException

from .util import is_empty

__all__ = ['get_all_couriers', 'detect']

api_modul = 'couriers'

def get_all_couriers():
    path = api_modul + '/all'
    response = make_request('GET', path, None)
    return response

def detect(params):
    if is_empty(params.get('tracking_number')):
        raise TrackingMoreException(ErrMissingTrackingNumber)
    path = api_modul + '/detect'
    response = make_request('POST', path, params)
    return response