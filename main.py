import logging
from Classes.API_Requests import API_Requests

def main():
    url = "https://catfact.ninja/fact"

    #url = "https://www.boredapi.com/api/activity"

    #url = "https://api.agify.io?name=meelad"

    #url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    logger = logging.getLogger(__name__)
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    try:
        accessor = API_Requests()
        print(accessor.APICalls(
        logger = logger,
        method= "get",
        url= url,
        content_type= "multipart/form-data",
        ))
    except:
        print("failed")


    
    
if __name__ == "__main__":
    main()