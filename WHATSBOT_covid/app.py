#from crypt import methods
#from urllib.request import Request
from email import message
from flask import Flask, request
import requests
import json
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
    

    covid_list = []
    covid_infor = []
    
    covid_session = True

    if msg.lower() == 'hello':
        resp.message('Hi, Im your medical chatbot assistant \n Please select any of the following\n 1 covid Information')
        return str(resp)


    if msg.lower() == '1':
        resp.message('Getting global covid chatbot 19 statistics')
        resp.message('To get spesific results for a country, type *eg covid Zimbabwe*')

        url = 'https://covid19.mathdro.id/api/'

        response = requests.request('GET', url)
        data = json.loads(response.text)

        cofirmed_cases = 'Total Global Cases:' + str(data['confirmed']['value'])
        recoverd = 'Total Recovered: '+ str(data['recovered']['value'])

        covid_list.append(cofirmed_cases)
        covid_list.append(recoverd)

        for item in covid_list:
            resp.message(item)

        return str(resp)

    if 'covid' in msg.lower():
        message = msg.replace('covid', ' '). strip()


        url = 'https://covid19.mathdro.id/api/country/%s' %message


        response = requests.request('GET', url)
        data = json.loads(response.text)

        resp.message('Covid 19 results for: ' + message)

        confirmed_cases = 'Total Cases:' + str(data['confirmed']['value'])
        confirmed_deaths = 'Total Recovered in: '+ str(data['recovered']['value'])

        covid_infor.append(confirmed_cases)
        covid_infor.append(confirmed_deaths)

        for info in covid_infor:
            resp.message(info)
            return str(resp)







if __name__ == '__main__':
    app.run()