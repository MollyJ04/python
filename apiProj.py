# Molly Jain
# apiProj.py

import requests
response = ""
# what controls whether or not the program is running
running = True
# a list of questions that users can ask
questionList = ["What's the weather?", "What's the temperature?", "What's the humidity?", "Is it windy?", "Is it warm out?",
                "Is it cloudy?", "Is it cold out?"]


def location():
    # the user enters the city and state they want, adn the program sets the response to the api's page on that city
    global running
    city = input("Enter the city name:")
    # if the user enters quit the program stops running
    if (city.lower() == "quit") or (city.lower() == "q"):
        running = False
    else:
        state = input("Enter the state name:")
        # if the user enters quit the program stops running
        if (state.lower() == "quit") or (state.lower() == "q"):
            running = False
        else:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid=bbdc3694e31a2aefd1ae28866c0158d4"
            global response
            response = requests.get(url)
            if str(response) != "<Response [404]>":
                response = response.json()
                print(f"Your city was set as {response['name']}.")
            else:
                # if the city isn't part of the api's data, it tells the user and asks for another city
                while str(response) == "<Response [404]>":
                    print("Sorry, that city isn't available. Please enter another city.")
                    city = input("Enter the city name:")
                    state = input("Enter the state name:")
                    # checks if the user wants to quit, then running is set to false and breaks out of the loop
                    if (city.lower() == "quit") or (city.lower() == "q"):
                        running = False
                    if not running:
                        break
                    else:
                        if (state.lower() == "quit") or (state.lower() == "q"):
                            running = False
                    if not running:
                        break
                    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid=bbdc3694e31a2aefd1ae28866c0158d4"
                    response = requests.get(url)
                    response = response.json()
                    print(f"Your city was set as {response['name']}.")


def tempConvert(temp):
    # converts the kelvin output to celsius and fahrenheit
    celsius = round((temp - 273))
    fahrenheit = round(((celsius*(9/5)) + 32))
    return[celsius, fahrenheit]


# every potential question will have a function
# some questions are like this that just print information
# and the others will have if statements that checks things like if it is warm out
def weatherQuestion():
    # tells the general weather
    global response
    print(f"The weather today in {response['name']}:")
    print(response["weather"][0]["main"])
    print(f"Today there will be {response['weather'][0]['description']}.\n")


def tempQuestion():
    # tells the temperature (actual, feels like, max, min) and humidity
    print(f"Today's temperature in {response['name']}:")
    print(f"Actual temperature: {tempConvert(response['main']['temp'])[1]}°F / {tempConvert(response['main']['temp'])[0]}°C")
    print(f"Feels like {tempConvert(response['main']['feels_like'])[1]}°F / {tempConvert(response['main']['feels_like'])[0]}°C")
    print(f"Low: {tempConvert(response['main']['temp_min'])[1]}°F / {tempConvert(response['main']['temp_min'])[0]}°C")
    print(f"High: {tempConvert(response['main']['temp_max'])[1]}°F / {tempConvert(response['main']['temp_max'])[0]}°C")
    print(f"Humidity: {response['main']['humidity']}%\n")


def humidityQuestion():
    # tells the humidity
    print(f"Today's humidity: {response['main']['humidity']}%\n")


def windyQuestion():
    # decides if it is windy and tells the suer
    if response['wind']['speed'] < 20:
        print("No, it's not windy today.\n")
    elif response['wind']['speed'] < 60:
        print(f"Yes, it is windy today.\nWind speed: {response['wind']['speed']}\n")
    else:
        print(f"It is dangerously windy today.\nWind speed: {response['wind']['speed']}\n")


def warmQuestion():
    # decides if it is warm, hot, cold, etc
    if response['main']['temp'] < 263:
        print("It's dangerously cold today.")
    elif response['main']['temp'] < 280:
        print("It's cold out today.")
    elif response['main']['temp'] < 300:
        print("It's warm out today.")
    elif response['main']['temp'] < 314:
        print("It's hot out today.")
    else:
        print("It's dangerously hot today.")
    print(f"The temperature today is {tempConvert(response['main']['temp'])[1]}°F / {tempConvert(response['main']['temp'])[0]}°C.\n")


def cloudyQuestion():
    # checks if the general weather is clouds and then how cloudy it is
    if response['weather'][0]['main'] == "Clouds":
        print(f"Yes.")
        if response['clouds']['all'] < 26:
            print("It is a little cloudy today.")
        elif (response['clouds']['all'] > 25) and (response['clouds']['all'] < 51):
            print("It is cloudy.")
        else:
            print("It is very cloudy.")
        print(f"Today there will be {response['weather'][0]['description']}.\n")
    # if the general weather isn't clouds but it's still cloudy, tells the user
    elif response['clouds']['all'] > 49:
        print("Yes.\nIt is cloudy today.\n")
    else:
        print("No.\nIt is not cloudy today.\n")


def questionCheck(quest):
    # checks if the question is quit, switch city, or a valid question, and either calls the matching function or returns false
    global running
    if (quest.lower() == "quit") or (quest.lower() == "q"):
        running = False
    elif quest.lower() in "switch city.":
        location()
        if running:
            question()
    elif quest.lower() in "what's the weather?":
        weatherQuestion()
    elif quest.lower() in "what's the temperature?":
        tempQuestion()
    elif quest.lower() in "what's the humidity?":
        humidityQuestion()
    elif (quest.lower() in "is it warm out?") or (quest.lower() in "is it cold out?"):
        warmQuestion()
    elif quest.lower() in "is it cloudy?":
        cloudyQuestion()
    elif quest.lower() in "is it windy?":
        windyQuestion()
    else:
       return False


def question():
    # prints options for the questions users can ask
    print("What do you want to know about the weather? You can ask things like:")
    for i in questionList:
        print(i)
    print("Or, you can switch your city by saying \"Switch city.\"\nYou can also quit at any time.")
    global questionChoice
    # takes the user's input
    questionChoice = input()
    # checks that the question is valid, and if it is lets questionCheck call the appropriate function
    while questionCheck(questionChoice) == False:
        questionChoice = input("Sorry, that's not a question you can ask yet! Please enter another question.")


print("Welcome to Wild Weather! Where would like to see weather for?\n(Note: Wild Weather currently only works for locations in America.)")
# takes the user's locations
location()
while running:
    # while it's running, it lets users keep asking questions until running is false, then it breaks
    question()
    if not running:
        break
