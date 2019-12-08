import json
import boto3
import os
import base64
from datetime import datetime
from decimal import Decimal
from boto3.dynamodb.conditions import Key, Attr
from services.apihttp import LambdaHttpEvent, LambdaHttpResponse
import random

DYNAMO_DB_REGION=os.environ['REGION']
TABLE_NAME=os.environ['DATA_SOURCE_TABLE']

def _convertAllIntsToStr(element):
        if isinstance(element, dict):
            for key in element:
                element[key] = _convertAllIntsToStr(element[key])
        elif isinstance(element, list):
            for index,value in enumerate(element):
                element[index] = _convertAllIntsToStr(value)
        elif isinstance(element, int):
            element = str(element)
        elif isinstance(element, float):
            element = str(element)
        elif isinstance(element, Decimal):
            element = str(element)
        return element

def getWord(type):
    dynamodb = boto3.resource('dynamodb', region_name=DYNAMO_DB_REGION)
    idnTable = dynamodb.Table(TABLE_NAME)
    dataBody = idnTable.query(
            TableName=TABLE_NAME,
            IndexName="data_source_type_index",
            Select='ALL_ATTRIBUTES',
            KeyConditionExpression=Key("data_source_type").eq(type),
    )
    item = random.choice(dataBody['Items'])
    print(item)
    return _convertAllIntsToStr(item)