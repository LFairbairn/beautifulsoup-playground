#Little project to scrape the "Most watched" and "Most Read" headline titles and associated internal links from BBC news website and save them to a text file. 

from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.co.uk/news"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

most_watched = soup.find(attrs={"data-component": "mostWatched"})

with open("most_watched.txt", "w") as file:
                pass # opening in w mode clears the file 

for headline in most_watched.find_all(class_="ssrcss-9n6uek-ColumnWrapper"):
        #print(headline.getText())
        with open("most_watched.txt", mode="a") as file:
                for title in headline:
                        file.write(f"{title.getText()}: {title.get('href')}\n")

most_read = soup.find(attrs={"data-component": "mostRead"})

with open("most_read.txt", "w") as file:
        pass

for headline in most_read.find_all(class_="ssrcss-9n6uek-ColumnWrapper"):
        #print(headline.getText())
        with open("most_read.txt", mode="a") as file:
                for title in headline:
                        file.write(f"{title.getText()}: {title.get('href')}\n")
                        




#TODO: How to move this into a class (webscraping class)(Beautifulsoup objet)
#TODO: Add methods etc find by attribute, find by class, find by href.
#TODO: Call a method for "write to file"
#TODO: add unit test to class with test response content. 