#from crypt import methods
#from urllib.request import Request
from flask import Flask, request
import requests
from sqlalchemy import true
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h2> Hello World<h1/>"

@app.route("/sms", methods = ['GET', 'POST'])
def botnet():
    msg = request.form.get('Body').lower()
    resp = MessagingResponse()
    #mediacat = resp.message()
    responce = False

    if 'quote'in msg:
        results = requests.get("https://api.quotable.io/random")

        if results.status_code==200:

            results_object = results.json()
            quote = f'{results_object["content"]}'

        else:
            quote = 'Sorry, i could not fetch a quote'

        resp.message(quote)
        return str(resp)
        responce = True
        


    # if 'cat' in msg:
    #      mediacat.media("https://caatas.com/cat")
    #      return str(resp)
    #      responce = True

    if not responce:
        resp.message("Sorry i could not understad you, please try again")
        return str(resp)
       





if __name__ == '__main__':
    app.run()