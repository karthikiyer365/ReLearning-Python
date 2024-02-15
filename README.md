<h2><b>Re-Learning Python</b></h2>

This folder is a collection of the various stepping stones in python that are essential in developing your python techstack right from the start towards a comprehensive understanding of Data Science and the various packages and libraries related with it.
The folder consists of numerous files detailed as below.

1. Nested Data Structures.
   The essential python data structures that are crucial and important to python are
   - Lists - Array of items
   - Dictionary - Key-Value pairs
   This file is an important example of handling such data structures and their nested forms

   #Nested Data Structures, #Dictionary, #List

2. Rock Paper Scissors.
   If Else statements and basic functions are demostrated in this simple terminal based gameplay.
   We represent the importance of packaging up our code in user-defined functions and its usability

   Additionally, it also shows the basic assert() function used to test our functionality for runtime complexities by providing sample test-cases.

   #IF Else statements #Error handling #assert() for testing

3. Market Sentiments API.
   In python API handling is one of the most crucial parts of Data Handling.
   In this file, we cover the basics of fetching and displaying data from a commonly used API i.e. AlphaVantage API.
   
   In APIs, the most important pass is passing a key to the API, which has to be done in such a manner that, in case of external interference the user key should not get leaked.
   We also touch upon that topic of safe key handling.



   APIs usually return data in JSON format. The JSON format looks something like this:
   {'Attribute1':'Info1',
    'Attribute2':['Info2.1', 'Info2.2', 'Info2.3'],
    'Attribute3':{'Attribute3.1':'Info3.1'
                  'Attribute3.2':['Info3.2.1', 'Info3.2.2', 'Info3.2.3']
                  },
                  and so on.......
    }

   We apply the knowledge of Nested Data Structures Handling, which is crucial when dealing with JSON files.

   Finally we use this knowledge to fetch the necessary columns of data and print and display them as we need.
   #API Hanlding, #IPython console image display, #getpass

4. Events Scraper (GWU).
   This file, is an example of handling the different types of data that can be fetch from any website. 
   For this example, we have utilized, the events page of George Washington Unniversity.

   The website will provide us with HTML page. We will parse this HTML data with the use of the BeautifulSoup package available in Python. 

   The fetch_url() function shows how a url can be customized based on user input. As shown, if we wish to fetch data for only some particular date/month/year we can do that by passing the necessary parameters to the link.


   Once we do that, we can fetch the content from the url. 
   The data returned is in html format. We use bs4 to help us look for data within the html page. 

   With this, we can use the classes, content tags, and more to search and fetch the necessary data.

   Finally, we apply our datastructures and data handling skills from previous experience to print the data as and how we need to.

   
