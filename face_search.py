import requests
import base64
from bs4 import BeautifulSoup
import json
import openai
from face import get_faces



def get_info(video):
    urls_main=[]
    faces=get_faces(video)
    api_key = "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"
    openai.api_key = api_key

    cookies = {
    'payment_gateway_new': 'transactioncloud',
    'ab_test_cookie_new': 'test_child_search_block_a_26_09',
    'uploadPermissions': '1696586830711',
    'XSRF-TOKEN': 'eyJpdiI6IlpsSjhRNzJoa2VMaVUva1plRHByNGc9PSIsInZhbHVlIjoiMklLM0F1Q0k0d2VqQlFaV2FyRWFEYXl1RUsxMjloWE1sZy9yZWZTVEtnRXdSTlJiWEJwVEFhbThMam92cFV2cE1SMnBjeFljMWJMYkN2SWI0cDJrOWtnenB4aFFid0N5VUFaWGlkK2YrMkpaam1Jdm1reDlrbk5ONkhUMlBZZ28iLCJtYWMiOiI0ZmZmNzc0Yjc3ODU4NmM1YTEwZmQwMjNlNjdiOTE2ODE0MzRjNTlkOGUzOWJlYTc0OWY0MWY1ZmI2OTAzMWIyIiwidGFnIjoiIn0%3D',
    'pimeyes_session': 'eyJpdiI6ImtkQklSbTdaUTdwWERqWXJZTFBZUVE9PSIsInZhbHVlIjoid1pWZzk5ZUJHWDQrcG85eCswcHM5QlRmbjlPaHp0YnNOTWFPMmtlVC84ZmhBb0tOdHhZSEcwYk9Nb1JKcHFYcmpPQ1NTbUROaGxyWCtESTA2Nkx4SjNRekM3NG16dVBlRVFld1dKaXBTUktUdTVnbEphd04zVGI3K3hPUDVXbmwiLCJtYWMiOiIxZjZiMjE5NTA5NzIwYzc0ZTRhZjJiMTA1ZTZkNGFiMTFjY2QwNzgyMjZiYTQ4MjY3MDBkMzM1ZDg4OTUxNjFiIiwidGFnIjoiIn0%3D',
    }

    headers = {
    'authority': 'pimeyes.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.8',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'payment_gateway_new=transactioncloud; ab_test_cookie_new=test_child_search_block_a_26_09; uploadPermissions=1696586830711; XSRF-TOKEN=eyJpdiI6IlpsSjhRNzJoa2VMaVUva1plRHByNGc9PSIsInZhbHVlIjoiMklLM0F1Q0k0d2VqQlFaV2FyRWFEYXl1RUsxMjloWE1sZy9yZWZTVEtnRXdSTlJiWEJwVEFhbThMam92cFV2cE1SMnBjeFljMWJMYkN2SWI0cDJrOWtnenB4aFFid0N5VUFaWGlkK2YrMkpaam1Jdm1reDlrbk5ONkhUMlBZZ28iLCJtYWMiOiI0ZmZmNzc0Yjc3ODU4NmM1YTEwZmQwMjNlNjdiOTE2ODE0MzRjNTlkOGUzOWJlYTc0OWY0MWY1ZmI2OTAzMWIyIiwidGFnIjoiIn0%3D; pimeyes_session=eyJpdiI6ImtkQklSbTdaUTdwWERqWXJZTFBZUVE9PSIsInZhbHVlIjoid1pWZzk5ZUJHWDQrcG85eCswcHM5QlRmbjlPaHp0YnNOTWFPMmtlVC84ZmhBb0tOdHhZSEcwYk9Nb1JKcHFYcmpPQ1NTbUROaGxyWCtESTA2Nkx4SjNRekM3NG16dVBlRVFld1dKaXBTUktUdTVnbEphd04zVGI3K3hPUDVXbmwiLCJtYWMiOiIxZjZiMjE5NTA5NzIwYzc0ZTRhZjJiMTA1ZTZkNGFiMTFjY2QwNzgyMjZiYTQ4MjY3MDBkMzM1ZDg4OTUxNjFiIiwidGFnIjoiIn0%3D',
    'origin': 'https://pimeyes.com',
    'referer': 'https://pimeyes.com/en',
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-user-id': '5498fe8ef97822b29b12f9e624d64fcf',
    'x-xsrf-token': 'eyJpdiI6IlpsSjhRNzJoa2VMaVUva1plRHByNGc9PSIsInZhbHVlIjoiMklLM0F1Q0k0d2VqQlFaV2FyRWFEYXl1RUsxMjloWE1sZy9yZWZTVEtnRXdSTlJiWEJwVEFhbThMam92cFV2cE1SMnBjeFljMWJMYkN2SWI0cDJrOWtnenB4aFFid0N5VUFaWGlkK2YrMkpaam1Jdm1reDlrbk5ONkhUMlBZZ28iLCJtYWMiOiI0ZmZmNzc0Yjc3ODU4NmM1YTEwZmQwMjNlNjdiOTE2ODE0MzRjNTlkOGUzOWJlYTc0OWY0MWY1ZmI2OTAzMWIyIiwidGFnIjoiIn0=',
}


    
    for face in faces:
        print(face,"\n")

        with open(face, 'rb') as file:
            image=file.read()

        base64image=base64.b64encode(image).decode('utf-8')

        json_data = {
            'g-recaptcha-response': None,
            'image': f'data:image/jpeg;base64,{base64image}',
        }

        response = requests.post('https://pimeyes.com/api/upload/file', cookies=cookies, headers=headers, json=json_data)

        soup = BeautifulSoup(response.text, 'html.parser')

        data=json.loads(soup.text)
        if(len(data["faces"])==0):
            print("Not Found\n")
            continue
        id=data["faces"][0]["id"]
        score=data["faces"][0]["score"]
        
        json_data = {
            'faces': [
                id,
            ],
            'time': 'any',
            'type': 'PREMIUM_SEARCH',
            'g-recaptcha-response': None,
        }

        response = requests.post('https://pimeyes.com/api/search/new', cookies=cookies, headers=headers, json=json_data)

        soup = BeautifulSoup(response.text, 'html.parser')

        data_j=json.loads(soup.text)
        shash=data_j["searchHash"]
        collhash=data_j["searchCollectorHash"]





        response=requests.get(f"https://pimeyes.com/en/results/{collhash}_{shash}?query={id}",headers=headers,cookies=cookies)

        soup=BeautifulSoup(response.text,"html.parser")
        api_url = soup.find('results-loader')['api-url']
        headers = {
            'authority': api_url,
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://pimeyes.com',
            'referer': 'https://pimeyes.com/',
            'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'x-user-id': '45fe33d669359dc662990a21ede33077',
            'x-xsrf-token': 'eyJpdiI6ImZtNnFsMld2OVJlekdoSnFVNkNWTVE9PSIsInZhbHVlIjoib3QzZkVrZjdpR0JVOTJubGJtUmNsQTNWRXFBT1ZtNnY2MGpqd283OTJTY2R2TERKZDNtTzZvajdJV04vRjJ1WmJkZUhqRWtnTVlESkN0a3lwdGtoQ0cweVA4Z0lzL0VDZHVGSzVnYTl6Z2M3NGM2MkJXak93SDZOcnpUY0lHVDIiLCJtYWMiOiJkM2U4MTcwZjE4ZWEzOGUyNThhOGYwNmFkOTAxYjEzZTY5ZGI4ZTRkYTNlM2ExOTk0ZGVjOGI1ZDBhOWE3NjUxIiwidGFnIjoiIn0=',
        }

        json_data = {
            'hash': shash,
            'limit': 250,
            'offset': 0,
            'retryCount': 0,
        }
        while True:
            try:
                response = requests.post(api_url,headers=headers , json=json_data)

                soup = BeautifulSoup(response.text, 'html.parser')
                data_j=json.loads(soup.text)
                print("Found Urls for This face")
                break
            except(json.decoder.JSONDecodeError) as e:
                continue
        
        count =0
        total_img=data_j["numberOfResults"]
        urls=[]
        for i in data_j["results"]: 
            url=i["sourceUrl"]
            if(url not in urls):
                count+=1
                urls.append(url)
            if(count==3):
                break
        texts=""
        urls_main.append(urls)
    return(urls_main)
        # for url in urls:
        #     response=requests.get(url)
        #     soup = BeautifulSoup(response.text, 'html.parser')
        #     all_text = soup.get_text()+"\n"
        #     texts+=all_text

        # response = openai.Completion.create(
        # engine="davinci",  
        # prompt=f"{texts}, What name occurs in all of these texts, Give only the name",
        # max_tokens=50,
        # )

    


