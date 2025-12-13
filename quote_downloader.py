'''Downloads quotes from zenquotes based on your query'''

import requests

class QuoteDownloader:
    '''
    
    :param query: determines the type of quote eg. `Motivational`, `fear`, `happiness` etc.
    :type query: str
    '''
    def __init__(self,query):
        self.query = query
        self.url = f"https://zenquotes.io/api/quotes/{self.query}"
        self.quote = requests.get(self.url).json()
    
    def getAuthor(self) -> list[str]:
        '''
        :return: Returns only the authors of the quotes received
        :rtype: list[str]
        '''
        authors = list
        for author in self.quote:
            authors.append(author['a'])
        return authors
    
    def storeQuotes(self, location : str = "quotes/quotes.txt") -> None:
        '''
        :param location: directory to store the quotes.
        :type location: str
        '''
        with open(location,"a+") as w:
            for result in self.getResults():
                w.write(f"{result["quote"]} - {result["author"]}")
                
                
    def getQuote(self) -> list[str]:
        '''
        :return: A list of `only` quotes
        :rtype: list[str]
        '''
        quotes = list
        for quote in self.quote:
            quotes.append(quote['q'])
        return quotes
    
    def getResults(self) -> list:
        '''
        :return: A list of quotes and their authors
        :rtype: list
        
        '''
        results = []
        
        for result in self.quote:
            results.append({
                "author" : result['a'],
                "quote" : result['q']
            })
        return results