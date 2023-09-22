from .const import ErrMissingTrackingNumber, ErrMissingCourierCode, ErrMaxTrackingNumbersExceeded, ErrEmptyId

from .exception import TrackingMoreException

from .request import make_request

from .util import is_empty

__all__ = ['create_tracking', 'get_tracking_results', 'batch_create_trackings', 'update_tracking_by_id', 'delete_tracking_by_id', 'retrack_tracking_by_id']

api_modul = 'trackings'

def create_tracking(params):
    if is_empty(params.get('tracking_number')):
        raise TrackingMoreException(ErrMissingTrackingNumber)
    if is_empty(params.get('courier_code')):
        raise TrackingMoreException(ErrMissingCourierCode)
    path = api_modul + '/create'
    response = make_request('POST', path, params)
    return response

def get_tracking_results(params):
    path = api_modul + '/get'
    response = make_request('GET', path, params)
    return response

def batch_create_trackings(params):
    if len(params) > 40:
        raise TrackingMoreException(ErrMaxTrackingNumbersExceeded)

    for item in params:
        if is_empty(item.get('tracking_number')):
            raise TrackingMoreException(ErrMissingTrackingNumber)
        if is_empty(item.get('courier_code')):
            raise TrackingMoreException(ErrMissingCourierCode)

    path = api_modul + '/batch'
    response = make_request('POST', path, params)
    return response

def update_tracking_by_id(id_string,params):
    if is_empty(id_string):
        raise TrackingMoreException(ErrEmptyId)
    path = api_modul + '/update/' + id_string
    response = make_request('PUT', path, params)
    return response

def delete_tracking_by_id(id_string):
    if is_empty(id_string):
        raise TrackingMoreException(ErrEmptyId)
    path = api_modul + '/delete/' + id_string
    response = make_request('DELETE', path, None)
    return response

def retrack_tracking_by_id(id_string):
    if is_empty(id_string):
        raise TrackingMoreException(ErrEmptyId)
    path = api_modul + '/retrack/' + id_string
    response = make_request('POST', path, None)
    return response