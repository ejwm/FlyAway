import requests
from flask import Flask
from flask import render_template
import uuid
from skyscanner.skyscanner import FlightsCache

my_id = uuid.uuid1()
apikey = 'fl615316188794647941972788886631'

app = Flask("MyApp")

@app.route("/")
def get_data():
	return render_template('Fly.html')

@app.route("/query", methods=['POST'])
def query_handler():

	# api_query = requests.post('http://partners.api.skyscanner.net/apiservices/pricing/v1.0').content
	flights_cache_service = FlightsCache(apikey)
	result = flights_cache_service.get_cheapest_quotes(
    	market='UK',
    	country='UK',
    	currency='GBP',
    	locale='en-GB',
    	originplace='SIN-sky',
    	destinationplace='KUL-sky',
    	outbounddate='2017-05-28',
    	inbounddate='2017-05-31',
    	adults=1).parsed
	# return requests.get('http://partners.api.skyscanner.net/apiservices/pricing/v1.0/{my_id}?apiKey={apikey}').content
	# form_data = requests.form
	# print form_data['name']
	# requests.form()
	return render_template("results.html", results=result)



app.run(debug=True)