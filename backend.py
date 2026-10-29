import asyncio
from nicegui import ui
import requests
import re
from bs4 import BeautifulSoup as bs

url = 'https://html.duckduckgo.com/html?q=puto'


#async def search(user_input, result):
def search(user_input, result):
    ui.notify('Hledám....')
    value = user_input.value
#    await asyncio.sleep(2)
    resultX, html= duck(url)
    print(value)
    result.content = html 
    ui.notify('hotovo')


def duck(url):
    filename = "DuckDuckGo.html"
    f = open(filename)
    soup = bs(f, "html.parser")
    #page = requests.get(url) 
    #soup = bs(page.content, "html.parser")
  
    txt = soup.find_all(attrs={"class": "result__a"})
    urls = soup.find_all(attrs={"class": "result__url"})
    excerpts = soup.find_all(attrs={"class": "result__snippet"})
    html_result = soup.find(attrs={"class": "serp__results"})


    print("====******====")
    urls = [u.text for u in urls]
    urls = [re.sub(r"\n +| +\n", "", u) for u in urls]

    print(urls)
     
    excerpts = [e.text for e in excerpts]
    print(excerpts)

    short_text = [t.text for t in txt]

    print(short_text)
    print("====")
    result = []

    for u, short_t, excerpt in zip(urls, short_text, excerpts):
      tmp = {"url": u, "short_text": short_t, "excerpt": excerpt}
      result.append(tmp)

    # print(result)
    #print(html_result)
    return result, str(html_result)


