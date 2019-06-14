from requests import get
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for container in movie_containers:
  if container.find('div', class_ = 'ratings-metascore') is None:
    continue
  name = container.h3.a.text
  names.append(name)
  
  year = container.h3.find('span', class_ = 'lister-item-year').text
  years.append(year)

  imdb = float(container.strong.text)
  imdb_ratings.append(imdb)

  m_score = container.find('span', class_ = 'metascore').text
  metascores.append(int(m_score))
  
  vote = container.find('span', attrs = {'name': 'nv'})['data-value']
  votes.append(int(vote))

import pandas as pd
test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes})
print(test_df.info())