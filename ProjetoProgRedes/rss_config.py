'''Esse arquivo contem as fontes RSS apenas'''

import feedparser

RSS_FEEDS = [
    "https://g1.globo.com/dynamo/rss2.xml",
    "http://www.bbc.co.uk/portuguese/index.xml",
    "http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml",
    "http://www.bbc.co.uk/portuguese/topicos/america_latina/index.xml",
    "http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml",
    "http://www.bbc.co.uk/portuguese/topicos/economia/",
    "http://www.bbc.co.uk/portuguese/topicos/saude/",
    "http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/",
    "http://www.bbc.co.uk/portuguese/topicos/cultura/",
    "http://www.bbc.co.uk/portuguese/especiais/index.xml"
]


"""
    Função para buscar notícias em feeds RSS que contenham a palavra-chave fornecida.

    Parâmetros:
        keyword (str): A palavra-chave a ser pesquisada nas notícias.

    Essa função utiliza a biblioteca feedparser para fazer a busca nas URLs RSS pré-configuradas.
    Para cada URL, ela obtém as últimas 10 notícias que contêm a palavra-chave fornecida.
    A função retorna uma lista contendo as notícias encontradas no formato (título, link).
 """
def noticia_rss(keyword):
    news_list = []
    for rss_feed in RSS_FEEDS:
        feed = feedparser.parse(rss_feed)
        for entry in feed.entries[:10]:
            if keyword.lower() in entry.title.lower():
                news_list.append(f"{entry.title}: {entry.link}")
    return news_list

