import scrapy
from scrapy.loader import ItemLoader
from scraper.items import BreedItem

BASE_URL = "https://www.woopets.fr"

class WoopetsSpider(scrapy.Spider):
    name = "woopets"
    allowed_domains = ["woopets.fr"]
    start_urls = [f"{BASE_URL}/chien/races/"]

    def parse(self, response):
        links = response.css("div.racesList a::attr(href)").getall()
        for link in links:
            full_url = response.urljoin(link)
            yield scrapy.Request(url=full_url, callback=self.parse_breed)

    def parse_breed(self, response):
        loader = ItemLoader(item=BreedItem(), response=response)
        loader.add_css("nom", "h1::text")
        loader.add_value("url", response.url)
        loader.add_css("description", "section.description p::text")

        rows = response.css("table.race-characteristics tr")
        for row in rows:
            label = row.css("th::text").get("").strip().lower()
            value = row.css("td::text").get("").strip()
            if "origine" in label:
                loader.add_value("origine", value)
            elif "groupe" in label:
                loader.add_value("groupe", value)
            elif "taille" in label:
                loader.add_value("taille", value)
            elif "poids" in label:
                loader.add_value("poids", value)
            elif "activité" in label:
                loader.add_value("activite", value)
            elif "entretien" in label:
                loader.add_value("entretien", value)
            elif "appartement" in label:
                loader.add_value("appartement", value)
            elif "enfants" in label:
                loader.add_value("enfants", value)

        yield loader.load_item()
