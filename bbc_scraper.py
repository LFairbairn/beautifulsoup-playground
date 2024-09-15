from base_scraper import HTMLScraper

class BbcScraper:
    def __init__(self) -> None:
        self.scraper = HTMLScraper("https://www.bbc.co.uk/news")

    def print_most_watched(self):
        most_watched = self.scraper.find_data_component("mostWatched")
        headlines = self.scraper.find_all_by_class(most_watched, "ssrcss-9n6uek-ColumnWrapper" )
        for headline in headlines:
            print(f"{headline.getText()}: {headline.get('href')}\n")

    def main():
        bbc_scraper = BbcScraper()
        bbc_scraper.print_most_watched()