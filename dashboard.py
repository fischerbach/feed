import streamlit as st
import pandas as pd

import requests

import json


url = "https://totalbet.pl/rest/market/categories"


payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

categories = pd.DataFrame(response.json()['data'])
# st.write(categories)

category = st.selectbox("Wybierz kategorię", categories['categoryName'])

if category:
	category_id = categories.query(f"`categoryName` == '{category}'").values[0][0]
	# st.write(category_id)
	url = f"https://totalbet.pl/rest/market/categories/{category_id}/events"
	st.header("URL do JSONa z kursami wydarzeń z wybranej kategorii:")
	st.write(url);
	# response = requests.request("GET", url, headers=headers, data=payload)
	# events = pd.DataFrame(response.json()['data'])
	# events_choose = st.multiselect("Wybierz wydarzenia", events['eventName'])

	# if(events_choose):
			
	# 	# st.write(events_choose)
	# 	events.query(f"eventName in {events_choose}", inplace=True)
	# 	# st.write(events)

	# 	feed = response.json()['data']
	# 	def filter_feed (event):
	# 		return event['eventName'] in events_choose
	# 	feed = list(filter(filter_feed, feed))
	# 	# st.write(json.dumps(feed))
	# 	st.header("Feed")
	# 	st.write(f"var feed = {feed};",)