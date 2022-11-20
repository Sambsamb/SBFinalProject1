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
import hashlib

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


def check_pass_function(mypass):
    base_url = 'https://api.pwnedpasswords.com/'
    api_call = 'range/'
    headers = {
        'User-Agent': Config.user_agent,
        'hibp-api-key': Config.api_key,
    }
    hash_object = hashlib.sha1(bytes(mypass, 'utf-8'))
    hex_dig = hash_object.hexdigest()
    response = requests.get(base_url + api_call + hex_dig[:5], headers=headers)
    if response.status_code == 200:
        hash_list = response.text.split('\r\n')
        found_match = None
        for myhash in hash_list:
            full_hash = hex_dig[:5] + myhash.strip().lower()
            if full_hash.split(':')[0] == hex_dig:
                found_match = full_hash
        data = found_match  # Formatted like: 7c4a8d09ca3762af61e59520943dc26494f8941b:37509543
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


def breaches_function():
    base_url = 'https://haveibeenpwned.com/api/v3/'
    api_call = 'breaches'
    headers = {
        'User-Agent': Config.user_agent,
        'hibp-api-key': Config.api_key,
    }
    response = requests.get(base_url + api_call, headers=headers)
    try:
        data = response.json()
        # keys: {'Title', 'ModifiedDate', 'Description', 'Domain', 'DataClasses',
        # 'Name', 'AddedDate', 'LogoPath', 'PwnCount', 'BreachDate',
        # 'IsFabricated', 'IsMalware', 'IsRetired', 'IsSensitive', 'IsSpamList', 'IsVerified'}

        # Comma format the numbers, count the totals:
        IsFabricatedCount = IsMalwareCount = IsRetiredCount = 0
        All = IsSensitiveCount = IsSpamListCount = IsVerifiedCount = 0
        for dic in data:
            dic.update({'PwnCount': '{:,}'.format(dic['PwnCount'])})
            All += 1
            if dic['IsFabricated'] == True:
                IsFabricatedCount += 1
            if dic['IsMalware'] == True:
                IsMalwareCount += 1
            if dic['IsRetired'] == True:
                IsRetiredCount += 1
            if dic['IsSensitive'] == True:
                IsSensitiveCount += 1
            if dic['IsSpamList'] == True:
                IsSpamListCount += 1
            if dic['IsVerified'] == True:
                IsVerifiedCount += 1

        # Add summaries at the end:
        data.append({
            'IsFabricatedCount': '{:,}'.format(IsFabricatedCount),
            'IsMalwareCount': '{:,}'.format(IsMalwareCount),
            'IsRetiredCount': '{:,}'.format(IsRetiredCount),
            'IsSensitiveCount': '{:,}'.format(IsSensitiveCount),
            'IsSpamListCount': '{:,}'.format(IsSpamListCount),
            'IsVerifiedCount': '{:,}'.format(IsVerifiedCount),
            'All': '{:,}'.format(All),
        })
    except:
        data = response.text
    return data


def breachedaccount_function(account):
    base_url = 'https://haveibeenpwned.com/api/v3/'
    api_call = 'breachedaccount/'
    headers = {
        'User-Agent': Config.user_agent,
        'hibp-api-key': Config.api_key,
    }
    parameters = '?truncateResponse=false'
    response = requests.get(base_url + api_call + account + parameters, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Add summary column
        for dic in data:
            dic.update({'PwnCount': '{:,}'.format(dic['PwnCount'])})
            summary = []
            if dic['IsVerified']:
                summary.append('Verified')
            if dic['IsFabricated']:
                summary.append('Fabricated')
            if dic['IsSensitive']:
                summary.append('Sensitive')
            if dic['IsRetired']:
                summary.append('Retired')
            if dic['IsSpamList']:
                summary.append('SpamList')
            if dic['IsMalware']:
                summary.append('Malware')
            dic['summary'] = ', '.join(summary)
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