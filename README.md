# SPshORTS ⚽🏏🏉🎾
 A sports news app that summarizes an article to 60 words
 - The application is currently development since i am fighting the BUG demons


### A small explanation of how the app works
- I am using the NewsAPI to get the top sport headlines, then I use BeautifulSoup 🍜 to webscrape the webpage for the article content.
- This retrieved article content is then sent to a function that uses the CohereAI API's Text Sumarization to summarize the article into 3-5 sentences. 



### Limitations 
- EFFICIENCY - Currently this 💩 is not efficient at all. I am focusing right now to get the app working and afterwards I will make it faster. (Source: Trust me)
- As with any work building atop statistical large language models, there is the risk that the output contains facts not present in the original document. These hallucinations might be innocuous.
- The control parameters of length and extractivenesss have an impact on the final output, but are not absolute.
