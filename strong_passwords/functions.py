"""
INF601 - Advanced Programming in Python
Final Project - App relating to MPS concentration
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
12/4/2022
"""

import requests
import Config


def check_url(url):
    try:
        get = requests.get(url)
        if get.status_code == 200:
            return f"{url}: is reachable"
        else:
            return f"{url}: is Not reachable, status_code: {get.status_code}"

    except requests.exceptions.RequestException as e:
        raise SystemExit(f"{url}: is Not reachable \nError details: {e}")


def check_email_function(email):
    base_url = 'https://haveibeenpwned.com/api/v3/'
    api_call = 'pasteaccount/'
    headers = {
        'User-Agent': Config.user_agent,
        'hibp-api-key': Config.api_key,
    }
    response = requests.get(base_url + api_call + email, headers=headers)
    if response.status_code == 200:
        data = response.json()
    else:
        try:
            json = response.json()
        except:
            json = None
        data = {
            'code': response.status_code,
            'text': response.text,
            'json': json,
        }
    return data


def get_hibp_dataclasses_function():
    base_url = 'https://haveibeenpwned.com/api/v3/'
    api_call = 'dataclasses'
    headers = {
        'User-Agent': Config.user_agent,
        'hibp-api-key': Config.api_key,
    }
    response = requests.get(base_url + api_call, headers=headers)
    try:
        data = response.json()
    except:
        data = response.text
    return data
