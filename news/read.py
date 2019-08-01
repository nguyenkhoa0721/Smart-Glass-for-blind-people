from newspaper import Article
from news.tomtat import TT
def READ(url,val):
    article = Article(url)
    article.download()
    article.parse()
    if (val==0):
    	return(str(article.text))
    else:
    	return(str(TT(article.text)))
