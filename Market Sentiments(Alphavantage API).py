"""Market Sentiments API"""

"""
For this exercise, we will fetch news sentiment data about a given company from the `AlphaVantage API`
Then we display a news feed of articles that are relevant to that company.

It may be helpful to take a few minutes to consult the documentation for the 
[News and Sentiments API endpoint](https://www.alphavantage.co/documentation/#news-sentiment) 
to learn more, and make a plan, before developing a solution.
"""
## Requirements
"""
We define a function called `display_articles`. 
The function accepts a string parameter called `symbol` and a float parameter called `min_relevance` 
(with assumed value between 0 and 1). 
Within the function definition, assign your own desired default values for each of these parameters.

When invoked the function fetchs news sentiments data about the given company,
and displays summary information about all articles that have a high relevance for this company 
(i.e. **only those articles with a ticker-specific relevance score greater than the specified minimum value**).


For any article that meets the criteria, the function displays the following information about that article:
  + **Title**
  + **Source**
  + **Author** (just the first one)
  + **Image** (displayed using [`IPython.display`])
  + **Summary**
  + **URL**
  + **Ticker-Specific Sentiment Score** (for the selected company only)
  + **Ticker-Specific Relevance Score** (for the selected company only)

Here is an example output:


> NOTE: your results will look different depending on when you run the dashboard
"""
## Setup

### API Key
"""
Obtain a free AlphaVantage API Key. 
Your code should reference this `API_KEY` variable when making requests.
"""

from getpass import getpass
API_KEY = getpass("Please input your AlphaVantage API Key: ") or "demo"

"""
## Dashboard / Solution
"""

import requests
import json
from IPython.display import Image, display
from getpass import getpass

def fetchKey():
    return getpass("Please input your AlphaVantage API Key: ")


def display_articles(symbol="NFLX", min_relevance=0.5):
    print("NEWS FOR:", symbol)
    print("MIN RELEVANCE:", min_relevance)


###generating url and fetching data
    request_url = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers="+symbol+"&apikey="+fetchKey()
    page = requests.get(request_url)
    data = json.loads(page.text)



###filtering for required info
    articles = data['feed']
    shortlist_articles = [item for item in articles for i in item['ticker_sentiment'] if i['ticker'] == symbol and float(i['relevance_score'])>=min_relevance]
    print("There are",len(shortlist_articles),"articles fitting the above parameters" )
    print("--------------------------------------------------------------------------------------------------------------")


###printing necessary information
    for item in shortlist_articles:
        print("Article No.",articles.index(item)+1,"\n")
        if item['banner_image']:
            display(Image(url= item['banner_image'], height=200))
        print("  TITLE:\t",item['title'])
        print(" SOURCE:\t",item['source'])
        print("AUTHORS:\t",*item['authors'])
        print("SUMMARY:\t",item['summary'])
        print("   LINK:\t",item['url'])
        for i in item['ticker_sentiment']:
            if i['ticker'] == symbol:
                print("SENTIMENT SCORE: ", i['ticker_sentiment_score'],"(",i['ticker_sentiment_label'],")")
                print("RELEVANCE SCORE: ", i['relevance_score'])
        print("-------------------------------------------------------------------------------------------------------------------------\n")

"""### Stock Selection Form"""

#@markdown Select a stock and a minimum relevance threshold. Then run the cell to display news artices relevant to that company.
symbol = "NFLX"  #@param ['AAPL', 'GOOG', 'MSFT', 'NFLX']
min_relevance = 0.5  #@param {type: "slider", min: 0, max: 1, step: 0.05}

display_articles(symbol=symbol, min_relevance=min_relevance)

"""
The user to input a stock symbol (i.e. "NFLX") and store it in a variable called `symbol`. 
Then print the selected symbol. Assume the user inputs a valid symbol..
"""

symbol = str(input("Enter the stock symbol: ")).upper()
symbol

"""
After consulting the API docs, find the desired request URL for Market News and Sentiments,
and create a string variable called `request_url` to represent this URL. Use string concatenation 
or a format string to join the `symbol` variable from Part A with the prodived `API_KEY` variable from the setup cell. 
Assume the user has input a valid API Key.
"""

request_url = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&sort=LATEST&tickers="+symbol+"&apikey="+fetchKey()
#print(request_url)

"""
Using the `request_url` variable from Part B, make an HTTP request for the market news and sentiments about the given company, and store the  response in a variable called `response`. Then convert the resulting JSON-formatted response data into a Python variable called `data`. Access the "feed" property of the data and store this in a variable called `articles`. Then print the number of articles (i.e. 50).
"""

response = requests.get(request_url)
data = json.loads(response.text)
#type(data)
data.keys()
print("There are",data['items'],"articles")

"""
Loop through the first three articles and print the following information about each:
  + **Title**
  + **Author** (just the first one is fine)
  + **Image** (ideally displayed using [`IPython.display`])
  + **Summary**
  + **URL**
  + **Ticker-Specific Sentiment Score** (for the selected company only)
  + **Ticker-Specific Relevance Score** (for the selected company only)

"""

articles = data['feed']
#type(articles)
#type(articles[0])
#articles[0]


counter = 0
for item in articles:
    print("Title:",item['title'])
    print("Authors:",*item['authors'])
    print("Summary: ",item['summary'],"\nLink:",item['url'])
    if item['banner_image']:
        display(Image(url= item['banner_image'], height=100))
    for i in item['ticker_sentiment']:
        if i['ticker'] == symbol:
            print("Sentiment Score: ", i['ticker_sentiment_score'])
            print("Relevance Score: ", i['relevance_score'])
    print("-------------------------------------------------------------------------------------------------------------------------")
    counter = counter+1
    if counter>=3:
        break

shortlist_articles = []
for items in articles:
    for i in items['ticker_sentiment']:
        if i['ticker']==symbol and float(i['relevance_score']) >= 0.5:
            shortlist_articles.append(items)

len(shortlist_articles)

"""
Let's only display information for articles that have a high relevance for this company 
(i.e. those with a ticker-specific relevance score greater than 50%). Display information about all articles that meet this criteria.

"""

for item in shortlist_articles:
    print("Title:",item['title'])
    print("Authors:",*item['authors'])
    print("Summary: ",item['summary'],"\nLink:",item['url'])
    if item['banner_image']:
        display(Image(url= item['banner_image'], height=100))
    for i in item['ticker_sentiment']:
        if i['ticker'] == symbol:
            print("Sentiment Score: ", i['ticker_sentiment_score'])
            print("Relevance Score: ", i['relevance_score'])
