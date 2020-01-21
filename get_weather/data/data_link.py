class DataLink:

	web1 = 'weatherstack.com'
	web2 = 'openweathermap.org'
	web3 = 'worldweatheronline.com'

	dic_web_key = [
			web1,
			web2,
			web3
			]

	query_link = {	'after_web':{		web1:'current',
										web2:'data/2.5/weather',
										web3:'premium/v1/weather.ashx'},
					'query_key_name':{	web1:'access_key',
										web2:'APPID',
										web3:'format=json&key'},
					'query_city_name':{	web1:'query',
										web2:'q',
										web3:'q'},
					'key'		:{		web1:'719d3fe6203f73509524e0bca348cb53',
										web2:'55fc030a936d5e205ca578d8a03011ba',
										web3:'d48ab845d78e492081b192620202001'},
					'first_level':{		web1:'current',
										web2:'main',
										web3:'data'},
					'temperature':{		web1:'temperature',
										web2:'temp',
										web3:'current_condition'},
				}
