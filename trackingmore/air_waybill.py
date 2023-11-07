import re

from .const import ErrInvalidAirWaybillFormat, ErrMissingAwbNumber

from .exception import TrackingMoreException

from .request import make_request

from .util import is_empty

__all__ = ['create_an_air_waybill']

def create_an_air_waybill(params):
    if is_empty(params.get('awb_number')):
        raise TrackingMoreException(ErrMissingAwbNumber)

    pattern = r'^\d{3}[ -]?(\d{8})$'
    if not re.match(pattern, params.get('awb_number')):
        raise TrackingMoreException(ErrInvalidAirWaybillFormat)
    path = '/awb'
    response = make_request('POST', path, params)
    return response