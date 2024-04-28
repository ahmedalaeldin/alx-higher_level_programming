import requests

def main():
    url = "https://alx-intranet.hbtn.io/status"
    
    # Send GET request
    response = requests.get(url)
    
    # Display the body of the response with required format
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    main()
