"""
INF601 - Advanced Programming in Python
Final Project - App relating to MPS concentration
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
12/4/2022
"""

import requests
import datetime


def check_url(url):
    try:
        get = requests.get(url)
        if get.status_code == 200:
            return f"{url}: is reachable"
        else:
            return f"{url}: is Not reachable, status_code: {get.status_code}"

    except requests.exceptions.RequestException as e:
        raise SystemExit(f"{url}: is Not reachable \nError details: {e}")


def check_pass(email):
    base_url = 'https://haveibeenpwned.com/api/v3/'
    api_call = 'pasteaccount/'
    headers = {
        'User-Agent': 'Lets Make Strong Passwords',
        'hibp-api-key': 'get your own'
    }

    try:
        response = requests.get(base_url + api_call + email, headers=headers)
        # print(f"The response is {response.text}")

        for result in response.json():
            print()
            for key in result.keys():
                # Convert Date fields from UTC to current time zone
                try:
                    print(str(key).ljust(12), datetime.datetime.strptime(str(result[key]), '%Y-%m-%dT%H:%M:%SZ'))
                except:
                    print(str(key).ljust(12), result[key])

    except BaseException as e:
        if response.status_code == 400:
            print('Bad request: The account does not comply with an acceptable format')
        elif response.status_code == 401:
            print('Unauthorized — the API key provided was not valid')
        elif response.status_code == 403:
            print('Forbidden: No user agent has been specified in the request')
        elif response.status_code == 404:
            print('Not found: The account could not be found (not pwned)')
        elif response.status_code == 429:
            print('Too many requests: The rate limit has been exceeded\n')
            print(response.text)


email = input('Please enter email address to check\n')
check_pass(email)

