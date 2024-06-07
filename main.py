
from Classes.API_Requests import API_Requests


def main():
    url = "https://catfact.ninja/fact"

    url = "https://www.boredapi.com/api/activity"

    #url = "https://api.agify.io?name=meelad"

    #url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"content_type= "multipart/form-data"
    accessor = API_Requests()
    print(accessor.APICalls(
        method= "get",
        url= url,
        

        
        ))

    
    
if __name__ == "__main__":
    main()