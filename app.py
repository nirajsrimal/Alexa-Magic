#!/usr/bin/env python
from flask import Flask
from flask_ask import Ask, statement, question, session
import requests


app = Flask(__name__)
ask = Ask(app, '/')
  
def isMagic(n): 
    sum = 0; 
    while (n > 0 or sum > 9): 
        if (n == 0): 
            n = sum; 
            sum = 0; 
        sum = sum + n % 10; 
        n = int(n / 10); 
    
    return True if (sum == 1) else False; 

@app.route('/')
def homepage():
    return 'Welcome to MagicNmber'

@ask.launch
def start_skill():
    message = 'Hey.. Ask me whether a number is  magic number or not'
    return question(message)

@ask.intent("NumberIntent",convert = {"num" : int})
def number_intent(num):
	if isMagic(num):
		message = "Yes, " + str(num) + " is a Magic Number" 
        return statement(message)
    else:
        message = "No, " + str(num) + " is not a Magic Number" 
        return statement(message)

@ask.intent("NoIntent")
def no_Intent():
    message = 'Well that is fine...Maybe next time'
    return statement(message)

@ask.intent("AMAZON.CancelIntent")
def cancel_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.StopIntent")
def stop_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.HelpIntent")
def help_Intent():
    message = 'Say a number. A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1,then the number is a magic number.'
    return question(message)

if __name__ == '__main__':
    app.run(threaded = True)