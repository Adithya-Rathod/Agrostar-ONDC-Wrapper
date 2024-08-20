def giveOffers(items):
    offers = []
    for item in items:
        if item["offers"] is None:
            continue
        offer = {
        "id" : "offer id of this offer ",
        "category_ids": ["which categories it belongs to"],
        "item_ids":["-- list of item ids(skucode) with which the offer is associated--"],
        "time" :{
                  "label": "--time details of the offer's validitly--",
                    "timestamp": "2024-08-08T15:11:59.006Z",
                    "duration": "string",
                    "range": {
                        "start": "2024-08-08T15:11:59.006Z",
                        "end": "2024-08-08T15:11:59.006Z"
                    },
                    "days": "string",
                    "schedule": {
                        "frequency": "string",
                        "holidays": [
                            "ISO 8061 fromat for date and hour"
                        ],
                        "times": [
                            "2024-08-08T15:11:59.006Z"
                        ]
                    }
                },
        "location_ids" : [{}]    
            }
        offers.append(offer)
        
    return offers
        
        