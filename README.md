trackingmore-sdk-python
=================

The Python SDK of Trackingmore API

Contact: <manage@trackingmore.org>

## Official document

[Document](https://www.trackingmore.com/docs/trackingmore/d5ac362fc3cda-api-quick-start)

Supported Python Versions
=========================

- 3.6
- 3.7
- 3.8
- 3.9
- 3.10
- pypy3

## Index
1. [Installation](https://github.com/TrackingMores/trackingmore-sdk-python#installation)
2. [Testing](https://github.com/TrackingMores/trackingmore-sdk-python#testing)
3. [Error Handling](https://github.com/TrackingMores/trackingmore-sdk-python#error-handling)
4. SDK
    1. [Couriers](https://github.com/TrackingMores/trackingmore-sdk-python#couriers)
    2. [Trackings](https://github.com/TrackingMores/trackingmore-sdk-python#trackings)
    3. [Air Waybill](https://github.com/TrackingMores/trackingmore-sdk-python#air-waybill)


## Installation

```
$ pip install trackingmore-sdk-python
```

## Via source code

Download the code archive, without unzip it, go to the
source root directory, then run:

```
$ pip install trackingmore-sdk-python.zip
```

## Quick Start

```python
import trackingmore

trackingmore.api_key = 'you api key'

couriers = trackingmore.courier.get_all_couriers()
```

## Testing
```
pytest
```

## Error handling

**Throw** by the new SDK client

```python
import trackingmore

trackingmore.api_key = ''

try:
  couriers = trackingmore.courier.get_all_couriers()
  print(couriers)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)

# API Key is missing
```

**Throw** by the parameter validation in function

```python
import trackingmore

trackingmore.api_key = 'you api key'

try:
  params = {'tracking_number': ''}
  couriers = trackingmore.courier.detect(params)
  print(couriers)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)

# Tracking number cannot be empty
```
## Examples

## Couriers
##### Return a list of all supported couriers.
https://api.trackingmore.com/v4/couriers/all
```python
try:
  result = trackingmore.courier.get_all_couriers()
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

##### Return a list of matched couriers based on submitted tracking number.
https://api.trackingmore.com/v4/couriers/detect
```python
params = {'tracking_number': '92612903029511573030094547'}
try:
  result = trackingmore.courier.detect(params)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

## Trackings
##### Create a tracking.
https://api.trackingmore.com/v4/trackings/create
```python
try:
  params = {'tracking_number': '92612903029511573030094547','courier_code':'usps'}
  result = trackingmore.tracking.create_tracking(params)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

##### Get tracking results of multiple trackings.
https://api.trackingmore.com/v4/trackings/get
```python
try:
  # Perform queries based on various conditions
  # params = {'tracking_numbers': '92612903029511573030094547', 'courier_code': 'usps'}
  # params = {'tracking_numbers': '92612903029511573030094547,92612903029511573030094548', 'courier_code': 'usps'}
  params = {'created_date_min': '2023-08-23T14:00:00+08:00', 'created_date_max': '2023-08-23T15:04:00+08:00'}
  result = trackingmore.tracking.get_tracking_results(params)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

##### Create multiple trackings (Max. 40 tracking numbers create in one call).
https://api.trackingmore.com/v4/trackings/batch
```python
try:
  params = [{'tracking_number': '92612903029511573030094593', 'courier_code': 'usps'},
              {'tracking_number': '92612903029511573030094594', 'courier_code': 'usps'}]
  result = trackingmore.tracking.batch_create_trackings(params)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

##### Update a tracking by ID.
https://api.trackingmore.com/v4/trackings/update/{id}
```python
params = {'customer_name': 'New name', 'note': 'New tests order note'}
id_string = "9a2f732e29b5ed2071d4cf6b5f4a3d19"
try:
  result = trackingmore.tracking.update_tracking_by_id(id_string, params)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

##### Delete a tracking by ID.
https://api.trackingmore.com/v4/trackings/delete/{id}
```python
id_string = "9a2f7d1e8b912b729388c5835c188c28"
try:
  result = trackingmore.tracking.batch_create_trackings(params)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

##### Retrack expired tracking by ID.
https://api.trackingmore.com/v4/trackings/retrack/{id}
```python
id_string = "9a2f7d1e8b912b729388c5835c188c28"
try:
  result = trackingmore.tracking.retrack_tracking_by_id(id_string)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```
## Air Waybill
##### Create an air waybill.
https://api.trackingmore.com/v4/awb
```python
params = {'awb_number': '235-69030430'}
try:
  result = trackingmore.air_waybill.create_an_air_waybill(params)
  print(result)
except trackingmore.exception.TrackingMoreException as ce:
  print(ce)
```

## Response Code

Trackingmore uses conventional HTTP response codes to indicate success or failure of an API request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error that resulted from the provided information (e.g. a required parameter was missing, a charge failed, etc.), and codes in the 5xx range indicate an TrackingMore's server error.


Http CODE|META CODE|TYPE | MESSAGE
----|-----|--------------|-------------------------------
200    |200     | <code>Success</code>        |    Request response is successful
400    |400     | <code>BadRequest</code>     |    Request type error. Please check the API documentation for the request type of this API.
400    |4101    | <code>BadRequest</code>     |    Tracking No. already exists.
400    |4102    | <code>BadRequest</code>     |    Tracking No. no exists. Please use 「Create a tracking」 API first to create shipment.
400    |4103    | <code>BadRequest</code>     |    You have exceeded the shipment quantity of API call. The maximum quantity is 40 shipments per call.
400    |4110    | <code>BadRequest</code>     |    The value of tracking_number is invalid.
400    |4111    | <code>BadRequest</code>     |    Tracking_number is required.
400    |4112    | <code>BadRequest</code>     |    Invalid Tracking ID.
400    |4113    | <code>BadRequest</code>     |    Retrack is not allowed. You can only retrack an expired tracking.
400    |4120    | <code>BadRequest</code>     |    The value of courier_code is invalid.
400    |4121    | <code>BadRequest</code>     |    Cannot detect courier.
400    |4122    | <code>BadRequest</code>     |    Missing or invalid value of the special required fields for this courier.
400    |4130    | <code>BadRequest</code>     |    The format of Field name is invalid.
400    |4160    | <code>BadRequest</code>     |    The awb_number is required or invaild format.
400    |4161    | <code>BadRequest</code>     |    The awb airline does not support yet.
400    |4190    | <code>BadRequest</code>     |    You are reaching the maximum quota limitation, please upgrade your current plan.
401    |401     | <code>Unauthorized</code>   |    Authentication failed or has no permission. Please check and ensure your API Key is correct.
403    |403     | <code>Forbidden</code>      |    Access prohibited. The request has been refused or access is not allowed.
404    |404     | <code>NotFound</code>       |    Page does not exist. Please check and ensure your link is correct.
429    |429     | <code>TooManyRequests</code>|    Exceeded API request limits, please try again later. Please check the API documentation for the limit of this API.
500    |511     | <code>ServerError</code>    |    Server error. Please contact us: service@trackingmore.org.
500    |512     | <code>ServerError</code>    |    Server error. Please contact us: service@trackingmore.org.
500    |513     | <code>ServerError</code>    |    Server error. Please contact us: service@trackingmore.org.