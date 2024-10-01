import requests
import logging

#x-api-key

class API_Requests:

    def __init__(self) -> None:
        self.url_error = "The url was not valid"
        self.authorization_error = "requried autherization not given"

    def APICalls(
        
        self,
        logger: logging.Logger,
        url:str, 
        method: str = "get", 
        authorization_token:str = None, 
        content_type: str ="application/json",
        api_key: str = None):
        #not sure what to do in this case
        if not logger:
            print("No logger given")
            
        if url is None or url == "":
            logger.error("No URL was given")
            return None

        headers = {}
        headers["Content-type"] = content_type

        if authorization_token:
            headers["Authorization"] = authorization_token
        result = requests.request(
            url= url,
            method= method,
            headers= headers,  
            auth=(api_key,''))
        
        #finds any errors
        try:    
            #baseline error message
            error_message = "url: {0} returned error code: {1}".format(url,str(result.status_code))

            if result.status_code >= 500:             
                logger.error(error_message) 
                return
            elif result.status_code >= 400:
                #400 errors are suposed to return a error message along with the status code
                logger.error(error_message + " with message/error: " + result.text) 
                if result.status_code == 401:
                    raise Exception("Error 401: Bad request")
                elif result.status_code == 404:
                    raise Exception("Error 404: client not found")
                elif result.status_code == 414:
                    raise Exception("Error 414: URL too long")
                else:
                    raise Exception("Error " + str(result.status_code))
            elif result.status_code >= 300:
                logger.error(error_message)  
                raise Exception("Error " + str(result.status_code))
            elif result.status_code < 200:
                logger.error(error_message)
        except Exception as ex:
                # prevents the program sending an error relating to the lack of a logger, 
                # if logger.error was exicuted without a viable logger
                if logger:
                    #stand in for return to user
                    print(ex)
                    return None
        #if there were no errors
        else:
            if result.status_code == 204:
                logger.info("url: {0} was reached with code 204".format(url))
            return result.text