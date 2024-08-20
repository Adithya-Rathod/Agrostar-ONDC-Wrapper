from service.itemService import getItems
from service.offerService import giveOffers
from service.paymentService import givePaymentInfo
from service.locationService import giveLocationForItem
from datetime import datetime

def transform_search_request(catalog, req):
    context = req.get("context", {})
    context.update({"bpp_id" : "agrostar.in", "bpp_uri" : "--the url of this wrapper when it is hosted on the server--", "timestamp" : str(datetime.now())})
    
    descriptor = {
    "name" : "Agrostar",
    "symbol": "--url--",
    "short_desc" : "Online Ecommerce for AgriTech",
    "long_desc" : "",
    "images" : ["--url--"],
    }
    
    provider= [{
    "id" : "1234567890",
    "time": {
        "label": "disable",
        "timestamp": str(datetime.now()),
        },
    "descriptor" : descriptor,
    "@ondc/org/fssai_license_no": "--somenumber licence number for agrostar--",
    "ttl" : "P1D",
    "location" : giveLocationForItem(catalog),
    "fulfillments" : [{}],
    "offers" : giveOffers(catalog),
    "payments" :  givePaymentInfo(catalog),
    "items": getItems(catalog),
    
        }
    ]
    return {
        "context" : context,
        "message" : {
            "catalog" : {
                "bpp/descriptor" : descriptor,
                "bpp/categories" :[{}],
                "bpp/fulfilments" : [{}],
                "bpp/payments" :[{}],
                "bpp/offers" : [{}],
                "bpp/providers" : provider,
                "exp" : "--time-after-which-catalog-has-to-be-refreshed--"
                },
            "error" : {}                
            }
        }
    