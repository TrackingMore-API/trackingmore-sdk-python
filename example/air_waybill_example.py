import trackingmore

trackingmore.api_key = 'you api key'

def create_an_air_waybill(params):
    try:
        result = trackingmore.air_waybill.create_an_air_waybill(params)
        return result
    except trackingmore.exception.TrackingMoreException as ce:
        print(ce)

if __name__ == '__main__':
    params = {'awb_number': '235-69030430'}
    result = create_an_air_waybill(params)
    print(result)
