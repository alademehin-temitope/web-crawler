
import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://ndb.nal.usda.gov/ndb/search'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'width': '100%'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&#39;', '')

        list_of_cells.append(text)

	list_of_rows.append(list_of_cells)

outfile = open("./data gotten.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Number", "food", "Nutritions"])
writer.writerows(list_of_rows)
