import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def clean_text(text):
    return text.strip()

class BreedItem(scrapy.Item):
    nom = scrapy.Field(input_processor=MapCompose(clean_text), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    origine = scrapy.Field(output_processor=TakeFirst())
    gabarit = scrapy.Field(output_processor=TakeFirst())
    tete = scrapy.Field(output_processor=TakeFirst())
    poil = scrapy.Field(output_processor=TakeFirst())
