'''Downloads quotes from zenquotes based on your query'''

import requests

class Quote_Downloader:
    def __init__(self,query):
        self.query = query
        self.url = f"https://zenquotes.io/api/quotes/{self.query}"
        self.quote = requests.get(self.url).json()
    
    def getAuthor(self) -> list[str]:
        authors = list
        for author in self.quote:
            authors.append(author['a'])
        return authors
    
    def getQuote(self) -> list[str]:
        quotes = list
        for quote in self.quote:
            quotes.append(quote['q'])
        return quotes
    
    def getResults(self) -> list:
        results = []
        
        for result in self.quote:
            results.append({
                "author" : result['a'],
                "quote" : result['q']
            })
        return results