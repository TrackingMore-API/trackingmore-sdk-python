import pytest

from trackingmore import air_waybill, exception, const

def test_valid_air_waybill():
    valid_params = {'awb_number': '235-69030430'}
    response = air_waybill.create_an_air_waybill(valid_params)
    assert response['meta']['code'] == 200

def test_empty_awb_number():
    invalid_params = {'awb_number': ''}
    with pytest.raises(exception.TrackingMoreException, match=const.ErrMissingAwbNumber):
        air_waybill.create_an_air_waybill(invalid_params)

def test_invalid_awb_format():
    invalid_params = {'awb_number': '12345'}
    with pytest.raises(exception.TrackingMoreException, match=const.ErrInvalidAirWaybillFormat):
        air_waybill.create_an_air_waybill(invalid_params)