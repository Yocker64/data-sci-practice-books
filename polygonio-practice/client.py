from polygon import RESTClient
import config
import json
from typing import cast
from urllib3 import HTTPResponse


client = RESTClient(config.API_KEY)
aggs = cast(
  HTTPResponse,
  client.getaggs(
    'AAPL',1,'day','2022-05-20','2022-11-11',raw=true
  )
)

data = json.loads(aggs.data)
print(data)
