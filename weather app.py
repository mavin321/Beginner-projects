import requests
def weather_app():
    city = input("city: ")
    api_key="1837ef6a8ed195cc15e31f7f3176b2c7"
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response=requests.get(api_url)
    if response.status_code==200:
        data=response.json()
        city_name=data["name"]
        temperature=data["main"]["temp"]
        description=data['weather'][0]['description']
        print(f"weather in {city_name}:\n - temperature:{temperature}C\n - decription: {description.capitalize()}")
    elif response.status_code==404:
        print("City not found. Please check the name and try again.")
    else:
        print("Error fetching data. Please try again later.")


def main():
    print('''             Welcome to the weather app
             please enter your city to 
             get the current weather status
    ''')
    while True:
        choice=input("do you want to check the weather in any city across the world? ")
        if choice.lower()=="yes":
            weather_app()
        elif choice.lower()=="no":
            break
        else:
            print("invalid input")


if __name__=='__main__':
    main()

