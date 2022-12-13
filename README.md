# Final Project - App relating to MPS concentration
>INF601 - Advanced Programming in Python
> 
>Sam Boutros
> 
> Prof. Zeller
> 
>FHSU - Fall 2022
>
>12/4/2022
>

## Installation

To install the needed packages use:
```python
pip install -r requirements.txt
```
To start the development server:
```python
python manage.py runserver
```
To change the port:
```python 
python manage.py runserver 8080
```
To deploy this Web App in Azure follow the [steps in this blog post](https://superwidgets.wordpress.com/2022/12/04/deploy-django-web-app-that-uses-sqlite-to-azure/) (skip the last steps to setup and configure the database).


#### Concept

This project will include the development of a Web App that will provide features related to identity security such as:

#### Check Email

This feature will find out if the email address and its associated password has appeared in previous security breaches (hacks). A finding does NOT necessarily mean that the email password is exposed. It could mean that a password associated with the email has been exposed. For example, when the email is used as the "user name" to access some Web App. This example is precisely why password reuse is a bad idea.

#### HIBP Data Classes

This feature will list the data classes observed in different exploits via Troy Hunt’s HIBP (Have I Been Pawned) service. 

#### Check Password

This feature will check to see if the provided password has been observed in past data breaches. Passwords are neither saved nor transmitted via API call. Instead, a range call of the first 5 characters of its SHA-1 hash is transmitted to the API to check for a match.

#### API

This web app will leverage the HIBP API version 3 at https://haveibeenpwned.com/API/v3.

#### Framework

The web app will be developed using the Django framework version 4.1.3.

#### Project Plan and features

The project will contain the following features:
* Easy branding via changes to the Config.py file. 
* API function calls in a central functions.py file.
* Use of Bootstrap from CDN in base.html file.
* Custom 404 and 500 pages.
* Anticipation and handling of API responses, other than code 200.
* Handling of multiple API calls in one form - see https://pass601a.azurewebsites.net/check_pass/
* Taking into account API limitations such as waiting 6 seconds between calls to avoid a 429 message. 








