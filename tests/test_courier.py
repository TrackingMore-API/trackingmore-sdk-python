import pytest

from trackingmore import courier,exception, const

def test_get_all_couriers():
    response = courier.get_all_couriers()
    assert response['meta']['code'] == 200

def test_detect():
    valid_params = {'tracking_number': '1234567890'}
    response = courier.detect(valid_params)
    assert response['meta']['code'] == 200

def test_detect_empty_number():
    invalid_params = {'tracking_number': ''}
    with pytest.raises(exception.TrackingMoreException, match=const.ErrMissingTrackingNumber):
        courier.detect(invalid_params)
