# -*- coding: utf-8 -*-
"""Simple fact sample app."""

import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


# =========================================================================================================================================
# TODO: The items below this comment need your attention.
# =========================================================================================================================================
SKILL_NAME = "Space Facts"
GET_FACT_MESSAGE = "Hello, and welcome, to the marriott hotel "
HELP_MESSAGE = "You can say tell me a space fact, or, you can say exit... What can I help you with?"
HELP_REPROMPT = "What can I help you with?"
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "The Space Facts skill can't help you with that.  It can help you discover facts about space if you say tell me a space fact. What can I help you with?"
FALLBACK_REPROMPT = 'What can I help you with?'
EXCEPTION_MESSAGE = "Sorry. I cannot help you with that."

# =========================================================================================================================================
# TODO: Replace this data with your own.  You can find translations of this data at http://github.com/alexa/skill-sample-python-fact/lambda/data
# =========================================================================================================================================

def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

#    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
#    print(url)
    return response.json()


def search(api_key, term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': 50
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


import argparse
import json
import pprint
import requests
import sys
import urllib

# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode


# Yelp Fusion no longer uses OAuth as of December 7, 2017.
# You no longer need to provide Client ID to fetch Data
# It now uses private keys to authenticate requests (API Key)
# You can find it on
# https://www.yelp.com/developers/v3/manage_app
API_KEY= "bX-0JbMtPZr796pdD-2lVwUgQDcSnJluQsWZb56-qWdTve8A2gC3xVpScikhmvks263_NKA4I4O4oUJNTbPTqTEs_LWl7gEDDph6VB3Fs4q7Ackih0G_IYChgmMWXXYx"


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
CATEGORIES_PATH = "/v3/categories/"

# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 10

def categories(api_key,term):
    url_params = {
        'term': term.replace(' ', '+'),
        'limit': 50
    }
    return request(API_HOST, CATEGORIES_PATH, api_key, url_params = url_params)

def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)        

def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location)

    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    print(u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id))
    response = get_business(API_KEY, business_id)

    print(u'Result for business "{0}" found:'.format(business_id))
    pprint.pprint(response, indent=2)
    
Locations = ["Chicago","New York","LA","Boulder","San Fransico","Austin","Toronto","Atlanta","Miami","Paris","London","Berlin"]
location_data = {}
for l in Locations:
#    print(l)
    r = search(API_KEY, "",l)
    businesses = []
    
    for b in r['businesses']:
        temp_dict={}
        if 'price' in b.keys():
            temp_dict = {'name': b['name'],'price':b['price'],'rating':b['rating'],"categories":[x['alias'] for x in b['categories']]}
        else:
            temp_dict = {'name': b['name'],'rating':b['rating'],"categories":[x['alias'] for x in b['categories']]}
            
        businesses.append(temp_dict)
    location_data[l] = businesses



data = [
  'John Smith. I see that you went to the aqurium in san diego last week. Might I suggest checking out the Shed Aquarium in downtown chicago?',
  'Becky Budro. Welcome to Chi Town! I know you love art museums! We are about two blocks from the MFA, you should go check it out!'
  'Bob Rubelstein. How about some barbeque tonight? There is a great place down the road.',
  'Gene Cunnington. Some sailing this weekend? The marina is only a 15 minute drive from here',
  'Frank Floyed. Up for some live music tonight? One of your favorite bands is playing at the house of blues. Want me to book you a ride',
]

JohnSmith = [
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
]

BeckyBudro = [
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
]

SirKitBoard = [
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
]


people = [JohnSmith, BeckyBudro, SirKitBoard]


Chicago = [
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
]

NewYork = [
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
]

LA = [
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
  ["Name", "key2", "key3", "key4", "key5", "key6", "key7"],
]

cities = [Chicago, NewYork, LA]

# =========================================================================================================================================
# Editing anything below this line might break your skill.
# =========================================================================================================================================

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Built-in Intent Handlers
class GetNewFactHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or
                is_intent_name("GetNewSpaceFactIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewFactHandler")

        random_fact = random.choice(data)

        #!!!!!!!!!!!!!!!!!!!!!!!!! Edit this to change response
        speech = GET_FACT_MESSAGE + random_fact #LA[0][0] <-- Gives the name of the fist activity in the "LA" array

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, random_fact))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(HELP_MESSAGE).ask(
            HELP_REPROMPT).set_card(SimpleCard(
                SKILL_NAME, HELP_MESSAGE))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(
            FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(GetNewFactHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
# sb.add_global_request_interceptor(RequestLogger())
# sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()