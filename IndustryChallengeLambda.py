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
