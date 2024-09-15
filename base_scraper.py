from bs4 import BeautifulSoup
import requests

class HTMLScraper:
    def __init__(self, url) -> None:
        response = requests.get(url)
        self.soup = BeautifulSoup(response.content, "html.parser")

    def find_data_component(self, value):
        return self.soup.find(attrs={"data-component": value})

    def find_data_component_by_content(self, content, value):
        return content.find(attrs={"data-component": value})

    def find_all_by_class(self, content, value):
        return content.find_all(class_= value)

       