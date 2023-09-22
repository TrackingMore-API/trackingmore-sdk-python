import pytest

from trackingmore import tracking,exception, const

def test_valid_tracking():
    valid_params = {
        'tracking_number': '92612903029511573030094597', # Uncreated Order Numbers
        'courier_code': 'usps',
    }
    response = tracking.create_tracking(valid_params)
    assert response['meta']['code'] == 200

def test_empty_tracking_number():
    invalid_params = {
        'tracking_number': '',
        'courier_code': 'usps',
    }
    with pytest.raises(exception.TrackingMoreException, match=const.ErrMissingTrackingNumber):
        tracking.create_tracking(invalid_params)

def test_empty_courier_code():
    invalid_params = {
        'tracking_number': '92612903029511573030094593',
        'courier_code': '',
    }
    with pytest.raises(exception.TrackingMoreException, match=const.ErrMissingCourierCode):
        tracking.create_tracking(invalid_params)

def test_get_tracking_results():
    test_params = {'tracking_numbers': '92612903029511573030094593', 'courier_code': 'usps'}
    response = tracking.get_tracking_results(test_params)
    assert response['meta']['code'] == 200

def test_valid_batch_tracking():
    valid_params = [
        {
            'tracking_number': '1234567890',
            'courier_code': 'UPS',
        },
    ]
    response = tracking.batch_create_trackings(valid_params)
    assert response['meta']['code'] == 200

def test_exceed_max_tracking_numbers():
    test_params = [
        {
            'tracking_number': '1234567890',
            'courier_code': 'UPS',
        },
    ]
    invalid_params = test_params * 50
    with pytest.raises(exception.TrackingMoreException, match=const.ErrMaxTrackingNumbersExceeded):
        tracking.batch_create_trackings(invalid_params)

def test_empty_tracking_number_in_batch():
    invalid_params = [
        {
            'tracking_number': '',
            'courier_code': 'UPS',
        },
    ]
    with pytest.raises(exception.TrackingMoreException, match=const.ErrMissingTrackingNumber):
        tracking.batch_create_trackings(invalid_params)


def test_empty_courier_code_in_batch():
    invalid_params = [
        {
            'tracking_number': '1234567890',
            'courier_code': '',
        },
    ]
    with pytest.raises(exception.TrackingMoreException, match=const.ErrMissingCourierCode):
        tracking.batch_create_trackings(invalid_params)

def test_valid_update_tracking():
    test_id_string = "9a2f732e29b5ed2071d4cf6b5f4a3d19" # Replace with a valid ID string
    test_params = {'customer_name': 'New name', 'note': 'New tests order note'}
    response =  tracking.update_tracking_by_id(test_id_string, test_params)
    assert response['meta']['code'] == 200

def test_empty_id_string():
    test_params = {'customer_name': 'New name', 'note': 'New tests order note'}
    with pytest.raises(exception.TrackingMoreException, match=const.ErrEmptyId):
        tracking.update_tracking_by_id("",test_params)

def test_valid_delete_tracking():
    test_id_string = "9a2f732e29b5ed2071d4cf6b5f4a3d19"  # Replace with a valid ID string
    response =  tracking.delete_tracking_by_id(test_id_string)
    assert response['meta']['code'] == 200

def test_empty_id_string():
    with pytest.raises(exception.TrackingMoreException, match=const.ErrEmptyId):
        tracking.delete_tracking_by_id("")

def test_valid_retrack_tracking():
    test_id_string = "9a2f8a77effe022aa296dea55d3ddaf3"  # Replace with expired tracking order number
    response = tracking.retrack_tracking_by_id(test_id_string)
    print(response)
    assert response['meta']['code'] == 200

def test_empty_id_string():
    with pytest.raises(exception.TrackingMoreException, match=const.ErrEmptyId):
        tracking.retrack_tracking_by_id("")