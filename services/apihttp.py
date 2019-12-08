import json

def getInternalServerError(e):
        mainError = "{'errorMessage': 'Internal Server error','errors': [" + str(e) + "]}"
        return LambdaHttpResponse(500,mainError).returnResponse()

def _getBody(dataBody):
        responseBody = ''
        try:
                responseBody = json.dumps(dataBody)
        except:
                responseBody = json.dumps({
                      "errorMessage":  str(dataBody)
                })
        return responseBody

def clientError(errorBody):
        return LambdaHttpResponse(400, _getBody(errorBody)).returnResponse()

def returnResponse(dataBody,isError):
        if isError:
                return clientError(dataBody)
        return LambdaHttpResponse(200, _getBody(dataBody)).returnResponse()

class LambdaHttpResponse:
    def __init__(self,status,body):
        self.statusCode = status
        self.headers = {
            "access-control-allow-credentials": "*",
            "access-control-allow-headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "access-control-allow-methods": "OPTIONS,POST,GET",
            "access-control-allow-origin": "*",
            "content-type": "application/json"
        }
        self.body = body
        self.isBase64Encoded = False
    def returnResponse(self):
        return {
            "statusCode": self.statusCode,
            "headers": self.headers,
            "isBase64Encoded": self.isBase64Encoded,
            "body": self.body
        }

class LambdaHttpEvent:
    def __init__(self,event):
        self.event = event

    def getQueryParam(self,param):
        return self.getQueryParamWithDefault(param,'')
    def getQueryParamWithDefault(self,param,default):
        if not "multiValueQueryStringParameters" in self.event:
            self.event["multiValueQueryStringParameters"] = {}
        if not param in self.event["multiValueQueryStringParameters"]:
            return "" 
        return self.event["multiValueQueryStringParameters"][param][0]

    def getBody(self):
        return json.loads(self.event['body'])
    
    def getPathParam(self,param):
        return self.getPathParamWithDefault(param,'')
    def getPathParamWithDefault(self,param,default):
        if not "pathParameters" in self.event:
            self.event["pathParameters"] = {}
        if not param in self.event["pathParameters"]:
            return default
        return self.event["pathParameters"][param]

    def getContentType(self,default):
            return self.getHeaderWithDefault('content-type',default)
    
    def getHeader(self,param):
        return self.getHeaderWithDefault(param,'')
    def getHeaderWithDefault(self,param,default):
        if not param in self.event["headers"]:
            return "" 
        if not param in self.event["headers"]:
            return default 
        return self.event['headers'][param]
    