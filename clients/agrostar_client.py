import requests

class AgrostarAPIClient:

    def searchProducts(search_string):
        url = "https://test-saathi-api.agrostar.in/shopaggregator/v2/products"
        
        params = {
            "language": "en",
            "searchString": search_string,
            "pageNo": 1,
            "pageSize": 30,
            "farmerId": 1906490,
            "excludePrefixSearch": True
        }

        headers = {
            
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'origin': 'https://test-saathi.agrostar.in',
            'priority': 'u=1, i',
            'referer': 'https://test-saathi.agrostar.in/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'source': 'APPMH',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-authorization-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IlRCMCJ9.eyJzdWIiOjIwNDczMDUsInB3ZCI6InBia2RmMl9zaGEyNTYkMjAwMDAkZllUUzBPWlR1bnRGJHU4akhLVkhTZVZtU0E0djNDY2Z2SXNFSGlheExDQVRVc01xREhjZVNzbzA9IiwiaWF0IjoxNzIxNjUxMDgzLCJleHBhdCI6bnVsbCwidHlwIjoiU0FUIiwiZ3JwIjpbXX0.LKhuOlS_vHxeiUvrbKWjVgFGFsnxwutZ1sWLmALCpoE'
        }

        
        response = requests.get(url, params=params, headers=headers)
        # return response.json().get("responseData", {}).get("productGists", [])
        return response.json().get("responseData", {}).get("productGists", [])