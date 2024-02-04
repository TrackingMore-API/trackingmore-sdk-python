import trackingmore

trackingmore.api_key = 'your api key'

def create_tracking(params):
    try:
        result = trackingmore.tracking.create_tracking(params)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)
    except Exception as e:
        print("other error:", e)

def get_tracking_results(params):
    try:
        result = trackingmore.tracking.get_tracking_results(params)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)
    except Exception as e:
        print("other error:", e)

def batch_create_trackings(params):
    try:
        result = trackingmore.tracking.batch_create_trackings(params)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)
    except Exception as e:
        print("other error:", e)

def update_tracking_by_id(id_string, params):
    try:
        result = trackingmore.tracking.update_tracking_by_id(id_string, params)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)
    except Exception as e:
        print("other error:", e)

def delete_tracking_by_id(id_string):
    try:
        result = trackingmore.tracking.delete_tracking_by_id(id_string)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)
    except Exception as e:
        print("other error:", e)

def retrack_tracking_by_id(id_string):
    try:
        result = trackingmore.tracking.retrack_tracking_by_id(id_string)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)
    except Exception as e:
        print("other error:", e)

if __name__ == '__main__':
    params = {'tracking_number': '92612903029511573030094547','courier_code':'usps'}
    result = create_tracking(params)
    print(result)

    # params = {'tracking_numbers': '92612903029511573030094547', 'courier_code': 'usps'}
    # params = {'tracking_numbers': '92612903029511573030094547,92612903029511573030094548', 'courier_code': 'usps'}
    params = {'created_date_min': '2023-10-09T06:00:00+00:00', 'created_date_max': '2023-10-10T13:45:00+00:00'}
    result = get_tracking_results(params)
    print(result)

    params = [{'tracking_number': '92612903029511573030094593', 'courier_code': 'usps'},
              {'tracking_number': '92612903029511573030094594', 'courier_code': 'usps'}]
    result = batch_create_trackings(params)
    print(result)

    params = {'customer_name': 'New name', 'note': 'New tests order note'}
    id_string = "9a2f732e29b5ed2071d4cf6b5f4a3d19"
    result = update_tracking_by_id(id_string, params)
    print(result)

    id_string = "9a2f7d1e8b912b729388c5835c188c28"
    result = delete_tracking_by_id(id_string)
    print(result)

    id_string = "9a2f732e29b5ed2071d4cf6b5f4a3d19"
    result = retrack_tracking_by_id(id_string)
    print(result)