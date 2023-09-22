import trackingmore

trackingmore.api_key = 'you api key'

def get_all_couriers():
    try:
        result = trackingmore.courier.get_all_couriers()
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)

def detect(params):
    try:
        result = trackingmore.courier.detect(params)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)

if __name__ == '__main__':
    result = get_all_couriers()
    print(result)

    params = {'tracking_number': '92612903029511573030094547'}
    result = detect(params)
    print(result)