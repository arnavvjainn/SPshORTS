from distutils.log import debug
from multiprocessing import context
from flask import Flask, render_template 
from newsapi import NewsApiClient

app = Flask(__name__)



@app.route("/")
def index():
    newsapi = NewsApiClient(api_key="")
    top_headlines = newsapi.get_top_headlines(category='sports', language='en')

    articles = top_headlines['articles']

    description = []
    news = []
    img = []

    for i in range(len(articles)):
        my_article = articles[i]
        
        news.append(my_article['title'])
        description.append(my_article['content'])
        img.append(my_article['urlToImage']) 

        
    my_list = zip(news, description, img) 

    return render_template('index.html', context = my_list)

if __name__ == "main":
    app.run(debug=True)
