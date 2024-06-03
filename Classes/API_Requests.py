import requests


class API_Requests:

    def __init__(self) -> None:
        self.no_url_given_error = "The url was not valid"

    def APICalls(self,
        url:str, 
        method: str = "Get", 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):

        if url is not str | url == "":
            return self.no_url_given_error

        d=1
    

    def get(self,
        url:str, 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):

        headers = {'Content-type': content_type}

        if authorization_token is not None:
            headers["Authorization"] = "access_token " + authorization_token
        
        if api_key is None:
            
            returned_value = requests.get(
                url= url, 
                headers= headers,
                auth = (api_key,'')
                )
            return returned_value
        else:

            returned_value = requests.get(
                url= url, 
                headers= headers,
                )
            return returned_value

    def post(self,
        url:str, 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):

        headers = {'Content-type': content_type}

        if authorization_token is not None:
            headers["Authorization"] = "access_token " + authorization_token
        
        if api_key is None:
            
            returned_value = requests.post(
                url= url, 
                headers= headers,
                auth = (api_key,'')
                )
            return returned_value
        else:

            returned_value = requests.get(
                url= url, 
                headers= headers,
                )
            return returned_value