def giveLocationForItem(items):
    locations = []
    for item in items:
        location = {
                            "id": "string",
                            "descriptor": {
                                "name": "string",
                                "code": "string",
                                "symbol": "string",
                                "short_desc": "string",
                                "long_desc": "string",
                                "images": [
                                    "string"
                                ],
                                "audio": "string",
                                "3d_render": "string"
                            },
                            "gps": "-8.171666890065335597377961327487783685162515737281252257377791140,        180",
                            "address": {
                                "door": "string",
                                "name": "string",
                                "building": "string",
                                "street": "string",
                                "locality": "string",
                                "ward": "string",
                                "city": "string",
                                "state": "string",
                                "country": "string",
                                "area_code": "string"
                            },
                            "station_code": "string",
                            "city": {
                                "name": "string",
                                "code": "string"
                            },
                            "country": {
                                "name": "string",
                                "code": "string"
                            },
                            "circle": {
                                "gps": "90,                                                                                                 -150.6860973953607131237579632121115837456644245441571569619101605087229062238970132",
                                "radius": {
                                    "type": "CONSTANT",
                                    "value": 0,
                                    "estimated_value": 0,
                                    "computed_value": 0,
                                    "range": {
                                        "min": 0,
                                        "max": 0
                                    },
                                    "unit": "string"
                                }
                            },
                            "polygon": "string",
                            "3dspace": "string",
                            "time": {
                                "label": "string",
                                "timestamp": "2024-08-08T15:11:59.008Z",
                                "duration": "string",
                                "range": {
                                    "start": "2024-08-08T15:11:59.008Z",
                                    "end": "2024-08-08T15:11:59.008Z"
                                },
                                "days": "string",
                                "schedule": {
                                    "frequency": "string",
                                    "holidays": [
                                        "2024-08-08T15:11:59.009Z"
                                    ],
                                    "times": [
                                        "2024-08-08T15:11:59.009Z"
                                    ]
                                }
                            },
                            "rateable": True
                        }
        locations.append(location)
    return locations