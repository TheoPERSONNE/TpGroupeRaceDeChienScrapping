import scrapy
from scrapy.loader import ItemLoader
from scraper.items import BreedItem
from scraper.utils.cleaning import clean_label, clean_value, extract_poids_taille

class WoopetsSpider(scrapy.Spider):
    name = "woopets"
    allowed_domains = ["woopets.fr"]
    start_urls = ["https://www.woopets.fr/chien/races/"]

    def parse(self, response):
        links = response.css("div.racesList a::attr(href)").getall()
        for link in links:
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_breed)

    def parse_breed(self, response):
        loader = ItemLoader(item=BreedItem(), response=response)
        loader.add_css("nom", "h1::text")
        loader.add_value("url", response.url)
        loader.add_css("description", "div.chapo strong::text")

        # Extraction table 1
        field_map = {
            "type_de_poil": "poil",
            "origine": "origine",
            "gabarit": "gabarit",
            "forme_de_la_tete": "tete",
        }
        rows_infos = response.xpath('//table[contains(@class, "tableInfosRace1")]//tr')
        for row in rows_infos:
            label_raw = ''.join(row.xpath('.//th//text()').getall())
            label = clean_label(label_raw)
            value = ''.join(row.xpath('.//td//text()').getall()).strip()
            if label in field_map:
                loader.add_value(field_map[label], clean_value(value))

        # Extraction table poids/taille
        rows_poids_taille = response.xpath('//table[contains(@class, "tableRacePoidsTaille")]//tr')
        for row in rows_poids_taille:
            label_raw = ''.join(row.xpath('.//th//text()').getall())
            label = clean_label(label_raw)
            value = ''.join(row.xpath('.//td//text()').getall()).strip()

            poids, taille = extract_poids_taille(value)
            if poids:
                loader.add_value(f"poids_{label}", poids)
            if taille:
                loader.add_value(f"taille_{label}", taille)

        yield loader.load_item()
