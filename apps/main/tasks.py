from __future__ import absolute_import, unicode_literals
import urllib
from bs4 import BeautifulSoup
import urllib.request
from celery import shared_task

@shared_task
def web_scrapping_BCV():
    url = "http://www.bcv.org.ve/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    content_dollar = soup.find("div", {"id":"dolar"})
    #content_date = soup.find("span", {"class":"date-display-single"})
    #fecha = content_date.text
    price = content_dollar.div.strong.text.strip()
    value = float(price.replace('.','').replace(',','.'))
    return value