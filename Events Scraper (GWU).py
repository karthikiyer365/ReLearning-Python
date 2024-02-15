# -*- coding: utf-8 -*-
"""
## 📅 GWU Events Scraper 📅

This code will request the **HTML** page contents of https://calendar.gwu.edu/calendar.
It will then parse the page and loop through the events and **display** some information about each, including:
  + **Title** (e.g. "Annie Artist Gallery Opening")
  + **Date info** including date, day of week, start, and end times (e.g. "Mon, Oct 2, 2023 11am to 3pm" or "Mon, Oct 2, 2023", depending on whether or not the start and end times are present - some events don't have start and end)
  + **Location** (e.g. "Smith Hall of Art, Gallery 102")
  + **Image** (ideally displayed)
  + **Primary event type** / first tag (e.g. "Arts and Culture")

Instead of a single field for the date info including day of week, start, and end times, we attempt to decompose the date info into separate fields:
  + Date (e.g. "2023-09-08")
  + Day of week (e.g. "Friday")
  + Start time, as applicable (e.g. "12:30pm" or None)
  + End time, as applicable (e.g. "01:30pm" or None)

The loop from the scraper also collects the events as a list of dictionaries called `events`.

Then we convert the entire list of `events` to a `pandas.DataFrame` object called `events_df`.
We inspect by:
  + Printing the column names.
  + Printing the number of rows.
  + Showing the first few rows.
  + Printing the earliest start time and the latest end time.

We then store the `events_df` contents to CSV file called "events.csv" in the colab filesystem. 
Optionally download the CSV file into your computer and open with speadsheet software.

Further Exploration

Then we write a function called `fetch_events` that accepts a date string like "2023-10-20" as a parameter input called `selected_date`, and returns the first page of events on that day, formatted as a list of dictionaries. If the `selected_date` parameter is omitted, the function should return the current day's events.
HINT: when we select a different date in the browser, the url will be something like: https://calendar.gwu.edu/calendar/day/2023/10/20
HINT: use a default value of `None` for the `selected_date` parameter. Inside the function, check the parameter's value, and if one is present, adjust the request url to include something like "/day/2023/10/20" at the end

Also implement tests like these for your function, and make sure they pass:
"""

## Solution

#SETUP CELL
import regex as re
import requests
import json
from IPython.display import Image, display
from bs4 import BeautifulSoup

# --------  SOLUTION  ----------

#Generating URL
def fetch_url():
    url =  "https://calendar.gwu.edu/calendar/"
    if (input("Events by Date?(Y/N):").upper() == "Y"):
        month = int(input("Month No."))
        date =  int(input("Enter Date: "))
        year = int(input("Enter year:"))
        url = url+"day"+f"/{year}/{month}/{date}"
    return(url)


#Day Date Time Handling
def datetimesplit(datetime):

    x = re.split("[\s,.]", datetime)
    x.pop(1)
    x.pop(3)
    try:
        x.pop(5)
    except:
        x.append('')
        x.append('')


    return(x)

#fetch_url()

# ------- Part 1 -------
#Fetching Content from URL
def fetch_content():
    EVENTS_PAGE_URL = fetch_url()
    page = requests.get(EVENTS_PAGE_URL)

    data = BeautifulSoup(page.text)
    body = data.find("body")

    content = body.find_all("div",{"class":"em-card"})

    return content

#fetch_content()[0]

#----- Part 3 ------
#Fetching Events from Content

def fetch_events():
    events = []
    content = fetch_content()

    for item in content:
        item_dict = {}
        if(item.find("h3", {"class", "em-card_title"}).text):
            item_dict['Title'] = (item.find("h3", {"class", "em-card_title"}).text)
        else:
            item_dict['Title'] = '--TBD--'

        if(len(item.find_all("p",{"class":"em-card_event-text"})) > 1):
            item_dict['datetime'] = (item.find_all("p",{"class":"em-card_event-text"})[0]).text.replace("\n",'').strip()
            item_dict['Venue'] = (item.find_all("p",{"class":"em-card_event-text"})[1].text).replace("\n",'').strip()
        elif(len(item.find_all("p",{"class":"em-card_event-text"}))==1):
            item_dict['datetime'] = (item.find_all("p",{"class":"em-card_event-text"})[0]).text.replace("\n",'').strip()
            item_dict['Venue'] = '--TBD--'
        else:
            item_dict['datetime'] = '--TBD--'
            item_dict['Venue'] = '--TBD--'

        if(item.find("a",{"class":"em-card_tag"})):
            item_dict['Tag'] = item.find("a",{"class":"em-card_tag"}).text
        else:
            item_dict['Tag'] = '--TBD--'

        if(item.find("img", {"class": "img_card"})['src']):
            item_dict['Image'] = (item.find("img", {"class": "img_card"})['src'])
        else:
            item_dict['Image'] = None

        day_date_time = datetimesplit(item_dict['datetime'])
        item_dict['Day'] = day_date_time[0]
        item_dict['Date'] = " ".join(day_date_time[1:4])
        item_dict['Start Time'] = day_date_time[4]
        item_dict['End Time'] = day_date_time[5]
        item_dict.pop('datetime')
        events.append(item_dict)

    return events

fetch_events()[0]

# --------Part 2----------
def display_events():
    events = fetch_events()
    for event in events:
        print('---------------------- Event No:',events.index(event)+1,'------------------------\n')
        if event['Image']:
            display(Image(url= event['Image'], height=200))

        print("Title:\t\t",event['Title'])
        print("Primary Event Type:",event['Tag'])
        print("Venue: \t\t",event['Venue'])
        print("Day:\t\t", event['Day'])
        print("Date:\t\t",event['Date'])
        print("Start time:\t", event['Start Time'])
        print("End time:\t",event['End Time'])

        print('------------------------------------------------------------\n')

#display_events()

display_events()
# TODO: collect all the events as a list of dict (fetch_events() function is answer for Q3)
events = fetch_events()

from pandas import DataFrame

events_df = DataFrame(events)

columns = events_df.columns.tolist()
print("Columns are:", ", ".join(columns).title())

print("There are",len(events_df),"rows")

events_df.head()

times = []
for i in events_df['Start Time'].tolist():
    if i:
        print('Earliest Start Time:',i)
        break

for i in events_df['End Time'].tolist():
    if i:
        times.append(i)
print('Latest End Time:',times[-1])

events_df.to_csv("events.csv")

"""## Exploration / Scratch Work"""
def date_parser(date_info:str):
    # TODO: parse the date string
    return {
        "weekday": "TODO",
        "date": "TODO",
        "start": "TODO",
        "end": "TODO",
    }

d1 = "Mon, Oct 2, 2023 10am to 11:30am"

d2 = "Mon, Oct 2, 2023"


from datetime import date

events = fetch_events()
assert any(events)
assert events[0]["date"] == str(date.today())

events = fetch_events("2023-10-20")
assert any(events)
assert events[0]["date"] == "2023-10-20"

## Evaluation