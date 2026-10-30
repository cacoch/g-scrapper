import asyncio
from nicegui import ui,app
import requests
import re
from bs4 import BeautifulSoup as bs


#async def search(user_input, result):
def search(user_input, res_html ):
    ui.notify('Hledám....')
    str2search = user_input.value
#    await asyncio.sleep(2)

    res_dict, html=  duck(str2search)
    res_html.content = html 
    ui.notify('hotovo')


def duck(query):
    
    #filename = "DuckDuckGo.html"
    #f = open(filename)
    #soup = bs(f, "html.parser")

    query  = query.strip()
    #headers = {
    #        "User-Agent": "w3m/0.5.6",
    #        "Accept" : "text/html, text/*;q=0.5, image/*, application/*",
    #        "Accept-Encoding" : "gzip, compress, bzip, bzip2, deflate, br",
    #        "Accept-Language" : "en;q=1.0"
    #        }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    base_url = "https://html.duckduckgo.com/html/"
    params = {"q": query}

    
    page = requests.get(base_url, params=params, headers=headers)

    if page.status_code != 200:
        print(f"Error: Received status code {response.status_code}")

    page.raise_for_status() 



    # Check what encoding requests thinks it should use
    print(page.encoding)


    # Check the Content-Type header
    print(page.headers.get("Content-Type"))
    print(page.status_code)

    soup = bs(page.content, "html.parser")

  
    txt = soup.find_all(attrs={"class": "result__a"})
    urls = soup.find_all(attrs={"class": "result__url"})
    excerpts = soup.find_all(attrs={"class": "result__snippet"})
    html_result = soup.find(attrs={"class": "serp__results"})


    urls = [u.text for u in urls]
    urls = [re.sub(r"\n +| +\n", "", u) for u in urls]

    excerpts = [e.text for e in excerpts]
    short_text = [t.text for t in txt]

    result = []

    # create dictionary from parsed result
    for u, short_t, excerpt in zip(urls, short_text, excerpts):
      tmp = {"url": u, "short_text": short_t, "excerpt": excerpt}
      result.append(tmp)

    # print(result)
    # print(html_result)
    return result, str(html_result)


