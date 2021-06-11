
import math
import logging

class Shortener():
    memory_dict = {}
    num_of_urls = 100000
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)

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
        else:
            print("The current num of urls are ", cls.num_of_urls)
            cls.memory_dict[url] = cls.num_of_urls
            shortened_url = cls.encode(cls.num_of_urls)
            print("The shortened URL is "+ shortened_url)
            cls.num_of_urls = cls.num_of_urls + 1
        return "localhost:5000/"+ shortened_url
    
    @classmethod
    def resolve(cls,code):
        print("The code that has been sent is ", code)
        print("The in mem database is \n" )
        print(cls.memory_dict)
        print("The lenght of the base is ", len(cls.characters))
        base_numbers = []
        for c in code:
            print(c)
            base_numbers.append(cls.characters.index(c))
        print(base_numbers)
        base_numbers = base_numbers[::-1]

        base_10_sum = 0
        for index,num in enumerate(base_numbers):
            print("The number is ", num)
            print("The index is ",index)
            print("The base number is ", cls.base)
            base_10_sum = base_10_sum + (int(num)*math.pow(int(cls.base), int(index)))

        print("The base sum is: " + str(base_10_sum))
        keys = [url for url, i in cls.memory_dict.items() if i == int(base_10_sum)]
        print(keys)
        return keys[0]
