import scrapy
from scrapy.loader import ItemLoader
from scraper.items import BreedItem
from scraper.utils.cleaning import clean_label, clean_value, extract_poids_taille

class WoopetsSpider(scrapy.Spider):
    name = "woopets"
    allowed_domains = ["woopets.fr"]
    start_urls = ["https://www.woopets.fr/chien/races/"]

    def parse(self, response):
        # Récupère tous les liens vers les pages de races
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

        # --- Extraction table poids/taille ---
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

        # --- Extraction des sections caractérisées par <h2 id="..."> ---
        sections = response.xpath('//h2[@id]')
        for section in sections:
            section_id = section.xpath('./@id').get()
            section_title = section.xpath('.//span/text()').get()

            # On cherche la première liste de notation qui suit ce <h2>
            ul = section.xpath('./following-sibling::*[self::ul[contains(@class, "notation-list")]][1]')
            stats = {}

            if ul:
                items = ul.xpath('./li')
                for item in items:
                    titre = item.xpath('.//p/text()').get()
                    if not titre:
                        continue
                    titre = titre.strip()
                    yes_icons = item.xpath('.//div[contains(@class, "notation-bar")]/i[contains(@class, "yes")]')
                    score = len(yes_icons)
                    stats[titre] = score

            # Ajouter au loader si stats trouvés
            if section_id and section_title and stats:
                loader.add_value(section_id, {
                    "resume": section_title.strip(),
                    "stats": stats
                })

        yield loader.load_item()
