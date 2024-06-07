import requests

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
        if authorization_token is not None:
            headers["Authorization"] = authorization_token
        #In testing, I found that my test, companie house, wouldn't except this, so 
        #I have chosen to use auth=(api_key,"") instead
        #if api_key is not None :
            #headers["x-api-key"] = api_key
        result = requests.request(
            url= url,
            method= method,
            headers= headers,  
            auth=(api_key,''))
        json
        #if there was an error
        if not result:
            #I've used this method instead of json to restrict unsesesary imports
            if result.text.__contains__("error"):
                #returns the error thrown bye the API
                start_index_of_error = result.text.find("error") + 8
                end_index_of_error = result.text.find("\"", start_index_of_error, result.text.__len__())
                print("Reached API with error: " +result.text[start_index_of_error: end_index_of_error])
                return None
            
            elif result.text.__contains__("message"):
                #returns the fair
                start_index_of_error = result.text.find("message") + 10
                end_index_of_error = result.text.find("\"", start_index_of_error, result.text.__len__())
                print("failed to reach API, message: " +result.text[start_index_of_error: end_index_of_error])
                return None

            else:
                print("Unknown error: " + result.text)
                return None

        return result.text