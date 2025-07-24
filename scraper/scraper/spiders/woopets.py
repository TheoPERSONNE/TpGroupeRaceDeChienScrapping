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

        rows = response.xpath('//table[contains(@class, "tableInfosRace1")]//tr')

        # Champs que l'on veut extraire
        field_map = {
            "type de poil": "poil",
            "origine": "origine",
            "gabarit": "gabarit",
            "forme de la tête": "tete"
        }

        for row in rows:
            # On récupère tout le texte dans le <th>, même s'il est mélangé (ex: texte + image)
            raw_label = row.xpath('.//th//text()').getall()
            label = ''.join(raw_label).strip().lower()

            value = ''.join(row.xpath('.//td//text()').getall()).strip()

            for key, field in field_map.items():
                if key in label:
                    loader.add_value(field, value)
                    break

        yield loader.load_item()
