import json

class Iterator:

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='utf-8')
        self.countries_list = []

        with open('countries.json') as f:
            file = json.load(f)
            for c in file:
                self.countries_list.append(c['name']['common'])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            country_name = self.countries_list.pop(0)
            #print(country_name)
        except IndexError:
            raise StopIteration

        return country_name


with open('countries.txt', 'w') as upload:
    for country in Iterator('countries.json'):
        #print(country)
        upload.write(f"{country} : https://wikipedia.org/wiki/{country.replace(' ', '_')}\n")
        #print(f"{country} : https://wikipedia.org/wiki/{country.replace(' ', '_')}")
