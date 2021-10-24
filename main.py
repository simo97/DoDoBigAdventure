import csv
import requests
from bs4 import BeautifulSoup


GOOGLE_BOT_UA = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
headers = {'User-Agent': GOOGLE_BOT_UA}

response: requests.Response = requests.get("https://digg.com/", headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    post_blocks = soup.find_all('article', attrs={'class': 'fp-vertical-story'})
    results = list()
    for block in post_blocks:
        results.append({
            'title': block.find('h2', class_='headline').text,
            'description': block.find('p').text,
            'count': block.find('div', class_='digg-count').text,
            'link': block.find('a', class_='block relative')['href']
        })
    # print("There is ",len(results), " Of articles onthe frontpage of https://digg.com/")
    _file = open("digg.com.csv", "w")
    writer = csv.writer(_file)
    writer.writerow(["title", 'description', 'count', 'link' ])
    for r in results:
        # print(r)
        writer.writerow([
            r['title'],
            r['description'],
            r['count'],
            r['link']
        ])
    _file.close()
    print("The CSV is created !!!")

        
    # print(post_blocks, " >>>>> the len here" )
else:
    print("There was an issue")

