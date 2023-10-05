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
        'ab_test_cookie_new': 'control_group_child_search_block_a_26_09',
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6ImRBT0NZbFJGazY0ek03WmhIVkN2M3c9PSIsInZhbHVlIjoiNENBaHlybXpCRFV0d21UbTkvRG5WRFNwWVRTbm5rWEhhenVIVzY3anlnc2VQMHFpRW4rY256OFo1TXJpdkJDbDNZb0wwTlNoSkZ4TjVYVlhmNzg0TnFIVXl1anVVWUJMLzVNUENyZnRtTlc1UVN0akRYZERkRGxxam1PRG1FWlU5UkVRNHpXbkUzcU1sL1Q2MDBNM0ptT1Q1T2cvYTdQbWVkTEZWT0pyOTh6ZllrNmJ3eUdiYk5tOVlIQVpHT2xHdnJ0Yzg3Nm4yTE1KR2RESWVCM3hJMW5jcjR1TW1GN0RJR0JKY0h2R1VHWT0iLCJtYWMiOiI2ZDVhY2M5ODliZjU5ZTY4NmU1ZjkxN2FhZmVlMThkZTM1NTViOTVlODQ0MWMxMDgzNjJiYjhjOTJiMzIxZDViIiwidGFnIjoiIn0%3D',
        'uploadPermissions': '1696499556181',
        'XSRF-TOKEN': 'eyJpdiI6ImZtNnFsMld2OVJlekdoSnFVNkNWTVE9PSIsInZhbHVlIjoib3QzZkVrZjdpR0JVOTJubGJtUmNsQTNWRXFBT1ZtNnY2MGpqd283OTJTY2R2TERKZDNtTzZvajdJV04vRjJ1WmJkZUhqRWtnTVlESkN0a3lwdGtoQ0cweVA4Z0lzL0VDZHVGSzVnYTl6Z2M3NGM2MkJXak93SDZOcnpUY0lHVDIiLCJtYWMiOiJkM2U4MTcwZjE4ZWEzOGUyNThhOGYwNmFkOTAxYjEzZTY5ZGI4ZTRkYTNlM2ExOTk0ZGVjOGI1ZDBhOWE3NjUxIiwidGFnIjoiIn0%3D',
        'pimeyes_session': 'eyJpdiI6IjBYUlMxdjdXeWFJRHBHaElLenFYQXc9PSIsInZhbHVlIjoiMEVrdTBWc1RYQmtvNmNzbTRUejQ0cU5QVkZ4MTAxYUs2NWJZeVdhOUZSUjF0aEtBeVZFUERyVVlTenVUSE5qYVR3MEpteEtvYmEvbk1Ga3NOVWpra252cHdzbTIwVWcwUXI4WGZmM0lVKy9iWk01czBnSlREeDhnbkZyL1pTWDUiLCJtYWMiOiI2ODUxYjA2ZWNmZGQwNTdkZTQzYTgyMzQxZmMzNmExOWI0ZTRmNzhhYmZhZDE2ZTJjMzhjNmJmMDc5ODhiZGExIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'authority': 'pimeyes.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.6',
        'content-type': 'application/json',
        # 'cookie': 'payment_gateway_new=transactioncloud; ab_test_cookie_new=control_group_child_search_block_a_26_09; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImRBT0NZbFJGazY0ek03WmhIVkN2M3c9PSIsInZhbHVlIjoiNENBaHlybXpCRFV0d21UbTkvRG5WRFNwWVRTbm5rWEhhenVIVzY3anlnc2VQMHFpRW4rY256OFo1TXJpdkJDbDNZb0wwTlNoSkZ4TjVYVlhmNzg0TnFIVXl1anVVWUJMLzVNUENyZnRtTlc1UVN0akRYZERkRGxxam1PRG1FWlU5UkVRNHpXbkUzcU1sL1Q2MDBNM0ptT1Q1T2cvYTdQbWVkTEZWT0pyOTh6ZllrNmJ3eUdiYk5tOVlIQVpHT2xHdnJ0Yzg3Nm4yTE1KR2RESWVCM3hJMW5jcjR1TW1GN0RJR0JKY0h2R1VHWT0iLCJtYWMiOiI2ZDVhY2M5ODliZjU5ZTY4NmU1ZjkxN2FhZmVlMThkZTM1NTViOTVlODQ0MWMxMDgzNjJiYjhjOTJiMzIxZDViIiwidGFnIjoiIn0%3D; uploadPermissions=1696499556181; XSRF-TOKEN=eyJpdiI6ImZtNnFsMld2OVJlekdoSnFVNkNWTVE9PSIsInZhbHVlIjoib3QzZkVrZjdpR0JVOTJubGJtUmNsQTNWRXFBT1ZtNnY2MGpqd283OTJTY2R2TERKZDNtTzZvajdJV04vRjJ1WmJkZUhqRWtnTVlESkN0a3lwdGtoQ0cweVA4Z0lzL0VDZHVGSzVnYTl6Z2M3NGM2MkJXak93SDZOcnpUY0lHVDIiLCJtYWMiOiJkM2U4MTcwZjE4ZWEzOGUyNThhOGYwNmFkOTAxYjEzZTY5ZGI4ZTRkYTNlM2ExOTk0ZGVjOGI1ZDBhOWE3NjUxIiwidGFnIjoiIn0%3D; pimeyes_session=eyJpdiI6IjBYUlMxdjdXeWFJRHBHaElLenFYQXc9PSIsInZhbHVlIjoiMEVrdTBWc1RYQmtvNmNzbTRUejQ0cU5QVkZ4MTAxYUs2NWJZeVdhOUZSUjF0aEtBeVZFUERyVVlTenVUSE5qYVR3MEpteEtvYmEvbk1Ga3NOVWpra252cHdzbTIwVWcwUXI4WGZmM0lVKy9iWk01czBnSlREeDhnbkZyL1pTWDUiLCJtYWMiOiI2ODUxYjA2ZWNmZGQwNTdkZTQzYTgyMzQxZmMzNmExOWI0ZTRmNzhhYmZhZDE2ZTJjMzhjNmJmMDc5ODhiZGExIiwidGFnIjoiIn0%3D',
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
        'x-user-id': '45fe33d669359dc662990a21ede33077',
        'x-xsrf-token': 'eyJpdiI6ImZtNnFsMld2OVJlekdoSnFVNkNWTVE9PSIsInZhbHVlIjoib3QzZkVrZjdpR0JVOTJubGJtUmNsQTNWRXFBT1ZtNnY2MGpqd283OTJTY2R2TERKZDNtTzZvajdJV04vRjJ1WmJkZUhqRWtnTVlESkN0a3lwdGtoQ0cweVA4Z0lzL0VDZHVGSzVnYTl6Z2M3NGM2MkJXak93SDZOcnpUY0lHVDIiLCJtYWMiOiJkM2U4MTcwZjE4ZWEzOGUyNThhOGYwNmFkOTAxYjEzZTY5ZGI4ZTRkYTNlM2ExOTk0ZGVjOGI1ZDBhOWE3NjUxIiwidGFnIjoiIn0=',
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

    


