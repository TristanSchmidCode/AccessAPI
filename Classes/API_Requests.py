import requests
import logging

#x-api-key

class API_Requests:

    def __init__(self) -> None:
        self.url_error = "The url was not valid"
        self.authorization_error = "requried autherization not given"

    def APICalls(self,
        url:str, 
        method: str = "get", 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):

        if url is None or url == "":
            print(self.url_error)
            return None

        headers = {}
        headers["Content-type"] = content_type

        if authorization_token:
            headers["Authorization"] = authorization_token
        #In testing, I found that my test, companie house, wouldn't except the api key in headers, so 
        #I have chosen to use auth=(api_key,"") instead
        result = requests.request(
            url= url,
            method= method,
            headers= headers,  
            auth=(api_key,''))
        
        #finds any errors
        try:    
            #baseline error log
            error_message = "url: {0} returned error code: {1}".format(url,str(result.status_code))
            
            if result.status_code >= 500:             
                logging.error(error_message) 

                return
            elif result.status_code >= 400:
                logging.error(error_message + "with message/error: " + result.text) 
                if result.status_code == 401:
                    raise Exception("Error 401: Bad request")
                elif result.status_code == 404:
                    raise Exception("Error 404: client not found")
                elif result.status_code == 414:
                    raise Exception("Error 414: URL too long")
                else:
                    raise Exception("Error " + str(result.status_code))
                
            elif result.status_code >= 300:
                logging.error(error_message)  
                raise Exception("Error " + str(result.status_code))
            elif result.status_code < 200:
                logging.error(error_message)
        except Exception as ex:
                #stand in for return to user
                print(ex)
        #if there were no errors
        else:
            if result.status_code == 204:
                logging.info("url: {} was reached with code 204".format(url))
            return result.text

        
        return result.text