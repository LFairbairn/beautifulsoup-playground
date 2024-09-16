from base_scraper import HTMLScraper

class BbcScraper:
    def __init__(self) -> None:
        self.scraper = HTMLScraper("https://www.bbc.co.uk/news")

    def print_most_watched(self):
        most_watched = self.scraper.find_data_component("mostWatched")
        headlines = self.scraper.find_all_by_class(most_watched, "ssrcss-9n6uek-ColumnWrapper")
        for headline in headlines:
            link = self.scraper.find_link_by_content(headline)
            print(f"{headline.getText()}: {link.get('href')}\n")

    def print_most_read(self):
        most_read = self.scraper.find_data_component("mostRead")
        headlines = self.scraper.find_all_by_class(most_read, "ssrcss-9n6uek-ColumnWrapper")
        for headline in headlines:
            link = self.scraper.find_link_by_content(headline)
            print(f"{headline.getText()}: {link.get('href')}\n")
   
    def main():
        bbc_scraper = BbcScraper()
        bbc_scraper.print_most_watched()
        bbc_scraper.print_most_read()

if __name__ == "__main__":
    BbcScraper.main()