def givePaymentInfo(items):
    payments = []
    for item in items:
        payment = {
                "uri": "string",
                "tl_method": "http/get",
                "params": {
                    "transaction_id": "string",
                    "transaction_status": "string",
                    "amount": "-466861782119716945067324221287091454.82379041836203319018",
                    "currency": "string",
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "type": "ON-ORDER",
                "status": "PAID",
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
                            "2024-08-08T15:11:59.008Z"
                        ],
                        "times": [
                            "2024-08-08T15:11:59.008Z"
                        ]
                    }
                },
                "collected_by": "BAP"
            }
        payments.append(payment)
    return payments