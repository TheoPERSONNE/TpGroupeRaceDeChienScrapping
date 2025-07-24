import scrapy
from itemloaders.processors import MapCompose, TakeFirst  # ✅ Correction ici

def clean_text(text):
    return text.strip()

class BreedItem(scrapy.Item):
    nom = scrapy.Field(input_processor=MapCompose(clean_text), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    origine = scrapy.Field(output_processor=TakeFirst())
    groupe = scrapy.Field(output_processor=TakeFirst())
    taille = scrapy.Field(output_processor=TakeFirst())
    poids = scrapy.Field(output_processor=TakeFirst())
    activite = scrapy.Field(output_processor=TakeFirst())
    entretien = scrapy.Field(output_processor=TakeFirst())
    appartement = scrapy.Field(output_processor=TakeFirst())
    enfants = scrapy.Field(output_processor=TakeFirst())
