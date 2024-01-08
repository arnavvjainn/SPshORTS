from crypt import methods
from distutils.log import debug
from multiprocessing import context
from urllib import response
from flask import Flask, render_template 
from newsapi import NewsApiClient
import config
import requests
from bs4 import BeautifulSoup
import cohere

co = cohere.Client(config.cohere_api_key)
app = Flask(__name__)



# @app.route('/', methods=['GET'])
# def index():
#     newsapi = NewsApiClient(api_key=config.api_key)
#     top_headlines = newsapi.get_top_headlines(category='sports', language='en')

#     articles = top_headlines['articles']

#     description = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         my_article = articles[i]
        
#         news.append(my_article['title'])
#         description.append(my_article['coneten'])
#         img.append(my_article['urlToImage']) 

        
#     my_list = zip(news, description, img) 

#     return render_template('index.html', context = my_list)

def summarize(text):
    response = co.summarize(
        text=text,
        model='command',
        length='medium',
        extractiveness='high'
    )
    return response.summary

@app.route('/', methods=['GET'])
def index():
    url = f"https://newsapi.org/v2/top-headlines?language=en&category=sports&apiKey={config.news_api_key}"
    #url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={config.news_api_key}"
    response = requests.get(url)
    data = response.json()

    # Lists to store article details
    titles = []
    contents = []
    image_urls = []

    # Loop through articles and store details
    for article in data['articles'][:2]:
        titles.append(article['title'])
        image_urls.append(article.get('urlToImage'))

        # Fetch the article content
        article_response = requests.get(article['url'])
        soup = BeautifulSoup(article_response.text, 'html.parser')

        article_content = soup.get_text()

        summarized_content = summarize(article_content)

        # Extract text and store
        contents.append(summarized_content)

    # Zip the lists together
    my_list = zip(titles, contents, image_urls)

    return render_template('index.html', context=my_list)

if __name__ == "main":
    app.run(debug=True)
