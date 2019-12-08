import json
from services.apihttp import LambdaHttpEvent, LambdaHttpResponse
from services.datasource import getWord

def get_easy_word(event, context):
    lambdaHttp = LambdaHttpEvent(event)
    word = getWord("easy")
    return LambdaHttpResponse(200,json.dumps(word)).returnResponse()

def get_medium_word(event, context):
    lambdaHttp = LambdaHttpEvent(event)
    word = getWord("medium")
    return LambdaHttpResponse(200,json.dumps(word)).returnResponse()

def get_hard_word(event, context):
    lambdaHttp = LambdaHttpEvent(event)
    word = getWord("hard")
    return LambdaHttpResponse(200,json.dumps(word)).returnResponse()