import datetime
from dateutil import parser
from isodate import parse_duration 
import pytz
def calculate_expiry_time(timestamp, ttl):

  parsed_timestamp = parser.parse(timestamp)
  parsed_ttl = parse_duration(ttl)  
  expiryTime = parsed_timestamp + parsed_ttl
  # print(parsed_timestamp)
  # print(" ADD ", parsed_ttl)
  # print(" = ", expiryTime)
  return expiryTime.isoformat()

# print(datetime.datetime.now())
# print(calculate_expiry_time(datetime.datetime.now().isoformat(), "PT24H"))
