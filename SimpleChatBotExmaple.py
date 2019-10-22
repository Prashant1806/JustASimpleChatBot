import random

from pip._vendor.distlib.compat import raw_input

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]

while True:
        userInput = raw_input(">>> ")
        if userInput in greetings:
                random_greeting = random.choice(greetings)
                print(random_greeting)
        elif userInput in question:
                random_response = random.choice(responses)
                print(random_response)
        else:
                print("I did not understand what you said")