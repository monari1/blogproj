"""
WSGI config for blogproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproj.settings')

application = get_wsgi_application()

# import os
# import africastalking
# from dotenv import load_dotenv

# load_dotenv()

# # Initialize SDK
# username = os.environ.get('AT_USERNAME')  
# api_key = os.environ.get('AT_APIKEY')      
# africastalking.initialize(username, api_key)


# # Initialize a service e.g. SMS
# sms = africastalking.SMS


# #Use it asynchronously
# def on_finish(error, response):
#     if error is not None:
#         raise error
#     print(response)

# sms.send("Hello Message!", ["+254711959117"], callback=on_finish)
