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
    poids_male = scrapy.Field(output_processor=TakeFirst())
    poids_femelle = scrapy.Field(output_processor=TakeFirst())
    taille_male = scrapy.Field(output_processor=TakeFirst())
    taille_femelle = scrapy.Field(output_processor=TakeFirst())
    caractere = scrapy.Field()
    comportementautres = scrapy.Field()
    education = scrapy.Field()
    conditionsvie = scrapy.Field()
    sante = scrapy.Field()
    # vie = scrapy.Field()
    entretien = scrapy.Field()
    budget = scrapy.Field()
    activite = scrapy.Field()
    autres = scrapy.Field(output_processor=TakeFirst())
    