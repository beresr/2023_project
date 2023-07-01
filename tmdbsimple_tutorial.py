import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

search = tmdb.Search()

response=search.movie(query='Prey')['results'][0]
print(response)

#'/ujr5pztc1oitbe7ViMUOilFaJ7s.jpg'
#https://image.tmdb.org/t/p/original/ujr5pztc1oitbe7ViMUOilFaJ7s.jpg
#https://image.tmdb.org/t/p/original/hYZhHMhQjITs9mziAH8gHsUA8Eb.jpg

from urllib.request import urlopen

#web_url = "https://image.tmdb.org/t/p/original"
#image_path = web_url + response['poster_path']

image_path = "https://image.tmdb.org/t/p/original/ujr5pztc1oitbe7ViMUOilFaJ7s.jpg"
image = urlopen(image_path).read()

print(image[0:100])  #a kép első 100 karaktere

with open('test.jpg', "wb") as poster:
    poster.write(image)