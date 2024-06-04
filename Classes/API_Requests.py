import requests


class API_Requests:

    def __init__(self) -> None:
        self.no_url_given_error = "The url was not valid"

    def APICalls(self,
        url:str, 
        method: str = "get", 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):

        if url is None or url == "":
            return self.no_url_given_error

        if method == "get":
             return self.get(url , 
            authorization_token , 
            content_type,
            api_key)
        elif method == "post":
            return self.post(url , 
                authorization_token , 
                content_type,
                api_key)
    

    def get(self,
        url:str, 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):

        headers = {'Content-type': content_type}

        #if an access tokenwas given, adds it to the header
        if authorization_token is not None:
            headers["Authorization"] = "access_token " + authorization_token
        
        # makes sure an api key is sent only if it is given
        if api_key is None:
            
            returned_value = requests.get(
                url= url, 
                headers= headers,
                auth = (api_key,'')
                )
            return returned_value.text
        else:

            returned_value = requests.get(
                url= url, 
                headers= headers,
                )
            return returned_value.text

    def post(self,
        url:str, 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):

        headers = {'Content-type': content_type}

        #if an access tokenwas given, adds it to the header
        if authorization_token is not None:
            headers["Authorization"] = "access_token " + authorization_token
        
        # makes sure an api key is sent only if it is given
        if api_key is None:
            
            returned_value = requests.post( url= url, headers= headers,  )
            return returned_value.text
        else:

            returned_value = requests.get( url= url, headers= headers,auth = (api_key,'') )
            return returned_value.text