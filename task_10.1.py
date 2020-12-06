import requests

proxy = {'https': '207.180.238.252:8118'}
url = 'https://superheroapi.com/api/2619421814940190/search/'
hero_dict = {}
heroes = ['Thanos', 'Hulk', 'Captain America', 'Batman']
def get_hero_intelligence_dict(name):
      response = requests.get(url + name, proxies=proxy)
      hero_list = response.json()['results']

      for hero in hero_list:
          if name in hero.values():
              hero_intelligence = hero['powerstats']['intelligence']
              hero_dict.setdefault(name, int(hero_intelligence))
      return hero_dict

def main(heroes, max_number = 1):
    for name in heroes:
        dict = get_hero_intelligence_dict(name)

    max_intelligence_dict = {}

    max_intelligence_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print(max_intelligence_dict)
    for id, hero in enumerate(max_intelligence_dict):
       if id == max_number:
            break
       print(f'The most intelligent superhero is {hero[0]} with intelligence {hero[1]}.')


main(heroes)