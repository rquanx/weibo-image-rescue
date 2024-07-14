# Constants
BASE_URL = "https://api.globalping.io/v1"
REQUEST_TIMEOUT = 15
GET_MEASUREMENT_INTERVAL = 5
GET_MEASUREMENT_OVERALL_TIMEOUT = 60

# Default headers
BASE_REQ_HEADERS = {
    "content-type": "application/json",
    "accept": "application/json",
    "accept-encoding": "br, gzip, deflate",
    "user-agent": "WeiboImageRescue/1.0 (miles/image-rescue)"
}

# Default regions
DEFAULT_REGIONS = ["Northern Africa", "Eastern Africa", "Middle Africa", "Southern Africa", "Western Africa", "Caribbean", 
                   "Central America", "South America", "Northern America", "Central Asia", "Eastern Asia", 
                   "South-eastern Asia", "Southern Asia", "Western Asia", "Eastern Europe", "Northern Europe", 
                   "Southern Europe", "Western Europe", "Australia and New Zealand", "Melanesia", "Micronesia", "Polynesia"]

# test retions
# DEFAULT_REGIONS = ["Northern Africa", "Eastern Africa","Northern America"]