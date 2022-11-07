import webbrowser
import time

URLS = [
    "https://news.ycombinator.com/",
    "https://www.reddit.com/r/programming/",
    "https://www.theguardian.com/world",
    "https://edition.cnn.com/world",
    "https://www.bbc.com/news/world",
    "https://www.bbc.com/news/technology",
    "https://www.xe.com/currencycharts/?from=USD&to=TRY"
]

for url in URLS:
    webbrowser.open(url)
    time.sleep(1.5)
    
