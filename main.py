
from Classes.API_Requests import API_Requests


def main():
    url = "https://catfact.ninja/fact"

    url = "https://www.boredapi.com/api/activity"
    accessor = API_Requests()
    content_type= "multipart/form-data"
    print(accessor.APICalls(
        method= "get",
        url= url,
        
        
        ))

    
    
if __name__ == "__main__":
    main()