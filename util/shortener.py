
import math
import logging
import psycopg2
from . import models
from .log import CustomLogger

ENV = "dev"
class Shortener():
    memory_dict = {}
    num_of_urls = 100000
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    clLogger = CustomLogger(__name__)
    logger = clLogger.get_logger()
    # cur = con.cursor()

    @classmethod
    def encode(cls, id):
        digits = []

        while id > 0:
            val = id % cls.base
            digits.append(cls.characters[val])
            id = math.floor(id/cls.base)
        return "".join(digits[::-1])

    @classmethod
    def shorten(cls, url):
        shortened_url = None 
        if url in cls.memory_dict:
            current_id = cls.memory_dict[url]
            shortened_url = cls.encode(current_id)
        
        elif models.check_url(url):
            cid = models.return_id(url)
            cls.memory_dict[url] = cid
            shortened_url = cls.encode(cid)

        else:
            cls.logger.info("Adding it to the database")
            id = models.add_url(url)
            cls.logger.info("Added to the database")
            cls.memory_dict[url] = id
            shortened_url = cls.encode(id)
            cls.logger.info("The shortened URL is "+ shortened_url)
        if ENV == 'dev':
            return "localhost:5000/"+ shortened_url
        else:
            return "https://tinnieurl.herokuapp.com/"+ shortened_url
    
    @classmethod
    def resolve(cls,code):
        url = None
        base_numbers = []
        for c in code:
            base_numbers.append(cls.characters.index(c))
        base_numbers = base_numbers[::-1]
        cls.logger.info("Base numbers generate are: "+ str(base_numbers))
        base_10_sum = 0
        for index,num in enumerate(base_numbers):
            base_10_sum = base_10_sum + (int(num)*math.pow(int(cls.base), int(index)))

        cls.logger.info("The base sum is: " + str(base_10_sum))
        url = [url for url, i in cls.memory_dict.items() if i == int(base_10_sum)]
        if url == []:
            url = [models.get_url(int(base_10_sum))]
            if url[0] == None:
                cls.logger.exception("The url is unknown")
                raise Exception("URL is unknown")
            else: 
                cls.memory_dict[int(base_10_sum)] = url[0]

        cls.logger.info(f"The url that is being sent back is {str(url[0])}")
        return url[0]
