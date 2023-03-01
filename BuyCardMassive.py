import requests
import csv
import bs4
# import pandas as pd


def writeResult(cars):
  with open('buyCard.csv', mode='w+', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['name','modelo', 'link', 'price', 'km', 'ciudad'])
    for car in cars:
      r = requests.get('https://carros.mercadolibre.com.co/{}/mecanica/valle-del-cauca/{}'.format(car["mark"],car["ref"]))
      soup = bs4.BeautifulSoup(r.text, 'html.parser')
      sections = soup.select('.ui-search-results ol')
      for section in sections:
          for article in section.children:
              name = article.select('.ui-search-item__title')[0].text
              link = (article.a['href'])
              price = article.select('.price-tag-fraction')[0].text
              modelo = (article.select('.ui-search-card-attributes__attribute')[0].text)
              km = (article.select('.ui-search-card-attributes__attribute')[1].text)
              ciudad = (article.select('.ui-search-item__location')[0].text)

              price = price.replace(".","").strip()
              km = km.replace(".","").replace("Km","").strip()

              writer.writerow([name, modelo, link,price, km, ciudad])

if __name__ == "__main__":
  cars = [
    {"mark":"renault", "ref":"clio"}, 
    {"mark":"kia", "ref":"rio"},
    {"mark":"chevrolet", "ref":"spark-gt"}, 
    {"mark":"kia", "ref":"cerato"}, 
    {"mark":"ford", "ref":"fiesta"}
    ]
  writeResult(cars)
